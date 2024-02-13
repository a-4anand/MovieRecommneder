# custom_admin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard")


    # Define your custom admin URLs here
]
