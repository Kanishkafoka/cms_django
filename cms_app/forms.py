from django import forms
from .models import Admin
from django.contrib.auth.forms import AuthenticationForm


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['username', 'email', 'phone', 'address', 'city', 'state', 'country', 'pincode', 'password']

    
class LoginForm(AuthenticationForm):
    class Meta:
        model = Admin
        fields = ['username', 'password']