from django.db import models

from accounts.models import User
from companies.models import Company


class RecruiterProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="recruiter_profile",
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="recruiters",
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.user.email} - {self.company.name}"