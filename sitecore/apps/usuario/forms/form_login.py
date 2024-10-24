from django import forms
from django.contrib.auth.forms import AuthenticationForm

from usuario.models import CustomUser

class TenantLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
