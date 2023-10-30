from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_idade(value):
    if not (0 <= value <= 99):
        raise ValidationError('Idade deve ter no máximo 2 dígitos numéricos.')

def validate_nome(value):
    if not re.match("^[A-Za-z]*$", value):
        raise ValidationError('Nome deve conter apenas letras.')

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255,blank=True, validators=[validate_nome])
    idade = models.PositiveSmallIntegerField(validators=[validate_idade])
