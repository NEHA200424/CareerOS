from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema, OpenApiResponse

from common.utils.response import success_response, error_response

from recruiters.models import RecruiterProfile

from jobs.api.serializers.job import (
    JobCreateSerializer,
    JobUpdateSerializer,
    JobListSerializer,
    JobDetailSerializer,
)

from jobs.services.job import JobService


class JobListCreateView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={
            200: OpenApiResponse(description="Jobs fetched successfully"),
        }
    )
    def get(self, request):

        jobs = JobService.get_all_jobs()

        serializer = JobListSerializer(
            jobs,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Jobs fetched successfully",
            status_code=status.HTTP_200_OK,
        )

    @extend_schema(
        request=JobCreateSerializer,
        responses={
            201: OpenApiResponse(description="Job created successfully"),
        },
    )
    def post(self, request):

        try:
            recruiter = request.user.recruiter_profile

        except RecruiterProfile.DoesNotExist:

            return error_response(
                message="Only recruiters can create jobs.",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        serializer = JobCreateSerializer(data=request.data)

        if not serializer.is_valid():

            return error_response(
                errors=serializer.errors,
                message="Validation failed",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        job = JobService.create_job(
            serializer.validated_data,
            recruiter,
        )

        return success_response(
            data=JobDetailSerializer(job).data,
            message="Job created successfully",
            status_code=status.HTTP_201_CREATED,
        )


class JobDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={
            200: OpenApiResponse(description="Job fetched successfully"),
        }
    )
    def get(self, request, pk):

        job = JobService.get_job(pk)

        serializer = JobDetailSerializer(job)

        return success_response(
            data=serializer.data,
            message="Job fetched successfully",
            status_code=status.HTTP_200_OK,
        )

    @extend_schema(
        request=JobUpdateSerializer,
        responses={
            200: OpenApiResponse(description="Job updated successfully"),
        },
    )
    def put(self, request, pk):

        job = JobService.get_job(pk)

        serializer = JobUpdateSerializer(
            job,
            data=request.data,
            partial=True,
        )

        if not serializer.is_valid():

            return error_response(
                errors=serializer.errors,
                message="Validation failed",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        updated = JobService.update_job(
            job,
            serializer.validated_data,
        )

        return success_response(
            data=JobDetailSerializer(updated).data,
            message="Job updated successfully",
            status_code=status.HTTP_200_OK,
        )

    @extend_schema(
        responses={
            200: OpenApiResponse(description="Job deleted successfully"),
        }
    )
    def delete(self, request, pk):

        job = JobService.get_job(pk)

        JobService.delete_job(job)

        return success_response(
            message="Job deleted successfully",
            status_code=status.HTTP_200_OK,
        )