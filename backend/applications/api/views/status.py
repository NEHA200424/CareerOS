from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema, OpenApiResponse

from applications.models import Application
from applications.api.serializers.status import ApplicationStatusSerializer
from applications.services.application import ApplicationService

from recruiters.models import RecruiterProfile

from common.utils.response import success_response, error_response


class ApplicationStatusView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ApplicationStatusSerializer,
        responses={
            200: OpenApiResponse(
                description="Application status updated successfully"
            ),
            400: OpenApiResponse(
                description="Validation failed"
            ),
            403: OpenApiResponse(
                description="Only recruiters can update status"
            ),
            404: OpenApiResponse(
                description="Application not found"
            ),
        },
    )
    def patch(self, request, pk):

        try:
            request.user.recruiter_profile

        except RecruiterProfile.DoesNotExist:

            return error_response(
                message="Only recruiters can update application status.",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        try:

            application = Application.objects.get(id=pk)

        except Application.DoesNotExist:

            return error_response(
                message="Application not found.",
                status_code=status.HTTP_404_NOT_FOUND,
            )

        serializer = ApplicationStatusSerializer(
            application,
            data=request.data,
            partial=True,
        )

        if not serializer.is_valid():

            return error_response(
                errors=serializer.errors,
                message="Validation failed",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        status_value = serializer.validated_data.get("status")

        if status_value is None:

            return error_response(
                message="Status field is required.",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        updated = ApplicationService.update_status(
            application,
            status_value,
        )

        return success_response(
            data=ApplicationStatusSerializer(updated).data,
            message="Application status updated successfully",
            status_code=status.HTTP_200_OK,
        )