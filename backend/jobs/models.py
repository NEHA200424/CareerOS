from django.db import models

from recruiters.models import RecruiterProfile
from companies.models import Company


class Job(models.Model):

    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"
    INTERNSHIP = "Internship"
    CONTRACT = "Contract"

    EMPLOYMENT_TYPES = [
        (FULL_TIME, "Full Time"),
        (PART_TIME, "Part Time"),
        (INTERNSHIP, "Internship"),
        (CONTRACT, "Contract"),
    ]

    title = models.CharField(max_length=255)

    description = models.TextField()

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    recruiter = models.ForeignKey(
        RecruiterProfile,
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    location = models.CharField(
        max_length=255,
    )

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPES,
    )

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    experience = models.PositiveIntegerField(
        help_text="Experience in years",
    )

    skills = models.TextField(
        help_text="Comma separated skills",
    )

    deadline = models.DateField()

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title