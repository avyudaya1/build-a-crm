from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()
class AgentModelForm(forms.ModelForm):
  field_order = ['first_name', 'last_name', 'username', 'email']
  class Meta:
    model = User
    fields = {
      'email',
      'username',
      'first_name',
      'last_name'
    }