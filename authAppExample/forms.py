from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('habitaciones', 'banios', 'alimentacion','valoracion','precio','descripcion','ubicacion','lastChangeDate','isAvailable')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }