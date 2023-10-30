# Generated by Django 4.2.5 on 2023-10-30 19:42

import app_cad_usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_cad_usuarios", "0004_alter_usuario_idade_alter_usuario_nome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="nome",
            field=models.CharField(
                blank=True,
                max_length=255,
                validators=[app_cad_usuarios.models.validate_nome],
            ),
        ),
    ]