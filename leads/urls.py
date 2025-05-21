from django.urls import path
from .views import dashboard, leads_list

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("leads/", leads_list, name="leads_list"),
]
