from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=64, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=64, blank=True)
    last_contacted = models.CharField(max_length=64, blank=True)
    next_step = models.CharField(max_length=128, blank=True)
    status = models.CharField(max_length=64, blank=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="leads_created")

    def __str__(self):
        return self.name
