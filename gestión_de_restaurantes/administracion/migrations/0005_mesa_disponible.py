# Generated by Django 5.1 on 2024-08-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administracion", "0004_alter_empleado_options_alter_menu_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mesa",
            name="disponible",
            field=models.BooleanField(default=True),
        ),
    ]
