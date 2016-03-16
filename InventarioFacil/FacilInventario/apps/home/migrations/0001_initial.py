# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=48)),
                ('direccion', models.CharField(max_length=120)),
                ('telefono', models.CharField(max_length=13)),
                ('nss', models.CharField(max_length=11)),
            ],
        ),
    ]
