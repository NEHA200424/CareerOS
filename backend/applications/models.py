from django.db import models

from accounts.models import User
from jobs.models import Job


class Application(models.Model):

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Reviewed", "Reviewed"),
        ("Shortlisted", "Shortlisted"),
        ("Interview", "Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Applied",
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "job")

    def __str__(self):
        return f"{self.student.email} -> {self.job.title}"