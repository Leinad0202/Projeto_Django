import re  # Importe a biblioteca re (expressões regulares)

from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario

def validate_age(value):
    if not re.match(r'^\d{2}$', value):
        raise ValidationError('A idade deve conter exatamente dois dígitos.')

def validate_name(value):
    if not re.match(r'^[A-Za-z\s]*$', value):
        raise ValidationError('O nome deve conter apenas letras e espaços.')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade']

    idade = forms.CharField(validators=[validate_age])
    nome = forms.CharField(validators=[validate_name])
