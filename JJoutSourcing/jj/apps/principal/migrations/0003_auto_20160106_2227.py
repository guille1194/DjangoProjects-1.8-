# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_instalacion_tecnico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacion',
            name='tipo_servicio',
            field=models.ManyToManyField(related_name='payment', to='principal.Tipo_servicio'),
        ),
    ]
