# Generated by Django 5.1 on 2024-08-20 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administracion", "0007_alter_venta_mesa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venta",
            name="mesa",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="administracion.mesa",
            ),
            preserve_default=False,
        ),
    ]
