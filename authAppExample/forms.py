from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('habitaciones', 'banios', 'alimentacion','valoracion','precio','descripcion','ubicacion','lastChangeDate','isAvailable')

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email')