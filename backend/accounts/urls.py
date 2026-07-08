from django.urls import path

from accounts.api.views.register import StudentRegisterView

urlpatterns = [
    path(
        "register/student/",
        StudentRegisterView.as_view(),
        name="student-register",
    ),
]