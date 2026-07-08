from accounts.models import User
from common.exceptions.custom import UserAlreadyExists


class RegisterService:

    @staticmethod
    def register_student(data):

        email = data["email"]

        if User.objects.filter(email=email).exists():
            raise UserAlreadyExists(
                "Email already exists."
            )

        user = User.objects.create_user(
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data.get("last_name", ""),
            phone_number=data.get("phone_number", ""),
            role=User.STUDENT,
        )

        return user