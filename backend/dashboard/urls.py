from django.urls import path

from dashboard.api.views.dashboard import RecruiterDashboardView

urlpatterns = [
    path("", RecruiterDashboardView.as_view()),
]