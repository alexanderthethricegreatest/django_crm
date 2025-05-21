from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    last_contacted = models.DateField(blank=True, null=True)
    next_step = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=[
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed')
    ], default='New')
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name