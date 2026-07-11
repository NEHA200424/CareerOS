from django.urls import path

from jobs.api.views.job import (
    JobListCreateView,
    JobDetailView,
)

urlpatterns = [
    path("", JobListCreateView.as_view()),
    path("<int:pk>/", JobDetailView.as_view()),
]