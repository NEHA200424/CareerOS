from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiResponse

from accounts.api.serializers.login import LoginSerializer
from accounts.services.auth.login import LoginService

from common.exceptions.custom import InvalidCredentials
from common.utils.response import success_response, error_response


@extend_schema(
    request=LoginSerializer,
    responses={
        200: OpenApiResponse(description="Login successful"),
        401: OpenApiResponse(description="Invalid credentials"),
    },
)
class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return error_response(
                errors=serializer.errors,
                message="Validation failed",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        try:

            data = LoginService.login(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )

            return success_response(
                data=data,
                message="Login successful",
                status_code=status.HTTP_200_OK,
            )

        except InvalidCredentials as e:

            return error_response(
                message=str(e),
                status_code=status.HTTP_401_UNAUTHORIZED,
            )