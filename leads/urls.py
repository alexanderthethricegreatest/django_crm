from django.urls import path
from . import views

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('add/', views.lead_add, name='lead_add'),
    path('edit/<int:pk>/', views.lead_edit, name='lead_edit'),
]