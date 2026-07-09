from django.urls import path

from accounts.api.views.register import StudentRegisterView
from accounts.api.views.login import LoginView

urlpatterns = [
    path(
        "register/student/",
        StudentRegisterView.as_view(),
        name="student-register",
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
]