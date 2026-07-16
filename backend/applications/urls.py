from django.urls import path

from applications.api.views.application import ApplicationView

urlpatterns = [
    path("", ApplicationView.as_view()),
]