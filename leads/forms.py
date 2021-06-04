from django import forms
from django.forms import fields
from .models import Lead
class LeadModelForm(forms.ModelForm):
  field_order = ['first_name', 'last_name', 'age', 'agent']
  
  class Meta:
    model = Lead
    fields = {
      'first_name',
      'last_name',
      'age',
      'agent'
    }