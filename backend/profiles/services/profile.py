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

    @staticmethod
    def update_profile(user, data):

        profile = ProfileService.get_profile(user)

        for key, value in data.items():
            setattr(profile, key, value)

        profile.save()

        return profile