from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema, OpenApiResponse

from common.utils.response import success_response, error_response

from profiles.api.serializers.profile import (
    StudentProfileSerializer,
    StudentProfileUpdateSerializer,
)

from profiles.services.profile import ProfileService

class MyProfileView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
    responses=StudentProfileSerializer
)

    def get(self, request):

        profile = ProfileService.get_profile(request.user)

        serializer = StudentProfileSerializer(profile)

        return success_response(
            data=serializer.data,
            message="Profile fetched successfully",
            status_code=status.HTTP_200_OK,
        )
    @extend_schema(
        request=StudentProfileUpdateSerializer,
        responses=StudentProfileSerializer,
    )

    def put(self, request):

        profile = ProfileService.get_profile(request.user)

        serializer = StudentProfileUpdateSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        if not serializer.is_valid():

            return error_response(
                errors=serializer.errors,
                message="Validation failed",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        updated_profile = ProfileService.update_profile(
            request.user,
            serializer.validated_data,
        )

        response_serializer = StudentProfileSerializer(
            updated_profile
        )

        return success_response(
            data=response_serializer.data,
            message="Profile updated successfully",
            status_code=status.HTTP_200_OK,
        )