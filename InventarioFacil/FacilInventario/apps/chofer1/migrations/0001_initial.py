# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rechazo_chofer1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_r', models.CharField(max_length=8)),
                ('cantidad_r', models.IntegerField()),
                ('fecha_r', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salida_chofer1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_s', models.CharField(max_length=8)),
                ('cantidad_s', models.IntegerField()),
                ('fecha_s', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
