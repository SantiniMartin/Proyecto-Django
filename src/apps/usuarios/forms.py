from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class FormUsuario(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'is_active', 'dni']
        
class FormUser(UserCreationForm):
    
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre de usuario'}))
    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'dni']
        
    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs['class'] = 'form-control'
        self.fields["last_name"].widget.attrs['class'] = 'form-control'
        self.fields["email"].widget.attrs['class'] = 'form-control'
        self.fields["dni"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].widget.attrs['class'] = 'form-control'        
        
    def clean_dni(self):
        dni = self.cleaned_data["dni"]
        print(dni)
        if not ( 7 <= len(str(dni)) <= 8):
            raise ValidationError("El DNI debe tener entre 7 a 8 digitos numericos")
        print(dni.__class__.__name__)
        return dni