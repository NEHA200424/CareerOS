from rest_framework import serializers


class RecruiterDashboardSerializer(serializers.Serializer):

    total_jobs = serializers.IntegerField()
    active_jobs = serializers.IntegerField()
    total_applications = serializers.IntegerField()
    applied = serializers.IntegerField()
    reviewed = serializers.IntegerField()
    shortlisted = serializers.IntegerField()
    interview = serializers.IntegerField()
    selected = serializers.IntegerField()
    rejected = serializers.IntegerField()