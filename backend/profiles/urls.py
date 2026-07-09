from django.urls import path

from profiles.api.views.profile import MyProfileView

urlpatterns = [
    path(
        "me/",
        MyProfileView.as_view(),
        name="my-profile",
    ),
]