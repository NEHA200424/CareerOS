from django.urls import path

from applications.api.views.application import ApplicationView
from applications.api.views.status import ApplicationStatusView

urlpatterns = [
    path("", ApplicationView.as_view()),
    path("<int:pk>/status/", ApplicationStatusView.as_view()),
]