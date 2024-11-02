from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class FormUsuario(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'dni']
        
class FormUser(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'dni']