from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_by', 'created_at')
    search_fields = ('name', 'email', 'status', 'created_by__username')