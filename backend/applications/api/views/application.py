from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema, OpenApiResponse

from common.utils.response import success_response, error_response

from jobs.models import Job

from applications.api.serializers.application import (
    ApplicationCreateSerializer,
    ApplicationListSerializer,
)

from applications.services.application import (
    ApplicationService,
)


class ApplicationView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        applications = ApplicationService.get_student_applications(
            request.user
        )

        serializer = ApplicationListSerializer(
            applications,
            many=True,
        )

        return success_response(
            data=serializer.data,
            message="Applications fetched successfully",
            status_code=status.HTTP_200_OK,
        )
    @extend_schema(
    request=ApplicationCreateSerializer,
    responses={
        201: OpenApiResponse(description="Application submitted successfully"),
        400: OpenApiResponse(description="Validation failed"),
    },
)

    def post(self, request):

        serializer = ApplicationCreateSerializer(
            data=request.data,
        )

        if not serializer.is_valid():

            return error_response(
                errors=serializer.errors,
                message="Validation failed",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        job = Job.objects.get(
            id=serializer.validated_data["job"].id
        )

        application = ApplicationService.apply(
            request.user,
            job,
        )

        if application is None:

            return error_response(
                message="You have already applied for this job.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        return success_response(
            message="Application submitted successfully",
            status_code=status.HTTP_201_CREATED,
        )