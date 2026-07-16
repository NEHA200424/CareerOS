from rest_framework import serializers

from applications.models import Application


class ApplicationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = [
            "job",
        ]


class ApplicationListSerializer(serializers.ModelSerializer):

    job_title = serializers.CharField(
        source="job.title",
        read_only=True,
    )

    company = serializers.CharField(
        source="job.company.name",
        read_only=True,
    )

    class Meta:
        model = Application
        fields = [
            "id",
            "job_title",
            "company",
            "status",
            "applied_at",
        ]