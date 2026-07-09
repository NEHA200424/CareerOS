from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.utils.response import success_response
from profiles.api.serializers.profile import StudentProfileSerializer
from profiles.services.profile import ProfileService


class MyProfileView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        profile = ProfileService.get_profile(request.user)

        serializer = StudentProfileSerializer(profile)

        return success_response(
            data=serializer.data,
            message="Profile fetched successfully",
            status_code=status.HTTP_200_OK,
        )