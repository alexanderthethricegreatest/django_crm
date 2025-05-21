from django.urls import path
from .views import dashboard, leads_list
from . import rep_views

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("leads/", leads_list, name="leads_list"),
    path("rep/", rep_views.rep_home, name="rep_home"),
    path("rep/add/", rep_views.rep_add_lead, name="rep_add_lead"),
    path("rep/edit/<int:lead_id>/", rep_views.rep_edit_lead, name="rep_edit_lead"),
]
