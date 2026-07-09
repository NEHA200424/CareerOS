from profiles.models import StudentProfile


class ProfileService:

    @staticmethod
    def get_profile(user):

        profile, created = StudentProfile.objects.get_or_create(
            user=user,
            defaults={
                "college": "",
                "degree": "B.Tech",
                "branch": "",
                "graduation_year": 2027,
            },
        )

        return profile
    