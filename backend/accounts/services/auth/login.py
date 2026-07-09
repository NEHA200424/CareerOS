from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from common.exceptions.custom import InvalidCredentials


class LoginService:

    @staticmethod
    def login(email, password):

        user = authenticate(
            email=email,
            password=password,
        )

        if user is None:
            raise InvalidCredentials(
                "Invalid email or password."
            )

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "role": user.role,
            },
        }