from jobs.models import Job
from applications.models import Application


class DashboardService:

    @staticmethod
    def recruiter_dashboard(recruiter):

        jobs = Job.objects.filter(recruiter=recruiter)

        total_jobs = jobs.count()
        active_jobs = jobs.filter(is_active=True).count()

        applications = Application.objects.filter(
            job__recruiter=recruiter
        )

        return {
            "total_jobs": total_jobs,
            "active_jobs": active_jobs,
            "total_applications": applications.count(),
            "applied": applications.filter(status="Applied").count(),
            "reviewed": applications.filter(status="Reviewed").count(),
            "shortlisted": applications.filter(status="Shortlisted").count(),
            "interview": applications.filter(status="Interview").count(),
            "selected": applications.filter(status="Selected").count(),
            "rejected": applications.filter(status="Rejected").count(),
        }