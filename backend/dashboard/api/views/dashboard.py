from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from dashboard.api.serializers.dashboard import RecruiterDashboardSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse

from recruiters.models import RecruiterProfile

from dashboard.services.dashboard import DashboardService

from common.utils.response import success_response, error_response


class RecruiterDashboardView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
    responses={
        200: RecruiterDashboardSerializer,
        403: OpenApiResponse(
            description="Only recruiters can access dashboard"
        ),
    }
)
    def get(self, request):

        try:
            recruiter = request.user.recruiter_profile

        except RecruiterProfile.DoesNotExist:

            return error_response(
                message="Only recruiters can access this dashboard.",
                status_code=status.HTTP_403_FORBIDDEN,
            )

        dashboard = DashboardService.recruiter_dashboard(
            recruiter
        )

        return success_response(
            data=dashboard,
            message="Dashboard fetched successfully",
            status_code=status.HTTP_200_OK,
        )