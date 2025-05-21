from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone', 'email', 'address', 'city', 'state', 'zip', 'country',
                  'last_contacted', 'next_step', 'status', 'notes']
        widgets = {
            'last_contacted': forms.DateInput(attrs={'type': 'date'}),
        }