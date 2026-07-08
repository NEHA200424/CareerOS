from rest_framework import serializers


class StudentRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    first_name = serializers.CharField(max_length=100)

    last_name = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
    )

    phone_number = serializers.CharField(
        max_length=15,
        required=False,
        allow_blank=True,
    )