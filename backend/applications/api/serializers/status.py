from rest_framework import serializers

from applications.models import Application


class ApplicationStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = [
            "status",
        ]