from rest_framework import status
from rest_framework.views import APIView

from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from accounts.api.serializers.register import StudentRegisterSerializer
from accounts.services.auth.register import RegisterService

from common.exceptions.custom import UserAlreadyExists
from common.utils.response import (
    success_response,
    error_response,
)
@extend_schema(
    request=StudentRegisterSerializer,
    responses={
        201: OpenApiResponse(description="Student registered successfully"),
        400: OpenApiResponse(description="Validation Error"),
    },
)


class StudentRegisterView(APIView):

    def post(self, request):

        serializer = StudentRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return error_response(
                errors=serializer.errors,
                message="Validation failed",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        try:
            RegisterService.register_student(
                serializer.validated_data
            )

            return success_response(
                message="Student registered successfully",
                status_code=status.HTTP_201_CREATED,
            )

        except UserAlreadyExists as e:
            return error_response(
                message=str(e),
                status_code=status.HTTP_400_BAD_REQUEST,
            )