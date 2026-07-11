from rest_framework import serializers

from profiles.models import StudentProfile


class StudentProfileSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )

    first_name = serializers.CharField(
        source="user.first_name",
        read_only=True,
    )

    last_name = serializers.CharField(
        source="user.last_name",
        read_only=True,
    )

    class Meta:
        model = StudentProfile

        fields = [
            "email",
            "first_name",
            "last_name",
            "college",
            "degree",
            "branch",
            "graduation_year",
            "cgpa",
            "bio",
            "github",
            "linkedin",
            "portfolio",
        ]


class StudentProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile

        fields = [
            "college",
            "degree",
            "branch",
            "graduation_year",
            "cgpa",
            "bio",
            "github",
            "linkedin",
            "portfolio",
        ]