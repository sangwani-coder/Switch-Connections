# forms.py
from django import forms
from .models import ContactFormSubmissions

class ContactFormSubmissionsForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmissions
        fields = ['first_name', 'last_name', 'email', 'mobile', 'message']
