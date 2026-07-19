from django.db import IntegrityError

from applications.models import Application


class ApplicationService:

    @staticmethod
    def apply(student, job):

        try:
            return Application.objects.create(
                student=student,
                job=job,
            )

        except IntegrityError:
            return None

    @staticmethod
    def get_student_applications(student):

        return (
            Application.objects
            .filter(student=student)
            .select_related("job", "job__company")
            .order_by("-applied_at")
        )

    @staticmethod
    def update_status(application, status):

        application.status = status
        application.save()

        return application