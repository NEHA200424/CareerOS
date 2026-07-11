from django.shortcuts import get_object_or_404

from jobs.models import Job


class JobService:

    @staticmethod
    def create_job(data, recruiter):

        return Job.objects.create(
            recruiter=recruiter,
            company=recruiter.company,
            **data,
        )

    @staticmethod
    def get_all_jobs():

        return Job.objects.select_related(
            "company",
            "recruiter",
            "recruiter__user",
        ).order_by("-created_at")

    @staticmethod
    def get_job(job_id):

        return get_object_or_404(
            Job,
            id=job_id,
        )

    @staticmethod
    def update_job(job, data):

        for key, value in data.items():
            setattr(job, key, value)

        job.save()

        return job

    @staticmethod
    def delete_job(job):

        job.delete()