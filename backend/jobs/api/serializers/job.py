from rest_framework import serializers

from jobs.models import Job


class JobCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        exclude = (
            "company",
            "recruiter",
            "created_at",
            "updated_at",
        )


class JobUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        exclude = (
            "company",
            "recruiter",
            "created_at",
            "updated_at",
        )


class JobListSerializer(serializers.ModelSerializer):

    company = serializers.CharField(
        source="company.name",
        read_only=True,
    )

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "company",
            "location",
            "employment_type",
            "salary",
            "experience",
            "is_active",
        ]


class JobDetailSerializer(serializers.ModelSerializer):

    company = serializers.CharField(
        source="company.name",
        read_only=True,
    )

    recruiter = serializers.CharField(
        source="recruiter.user.email",
        read_only=True,
    )

    class Meta:
        model = Job
        fields = "__all__"