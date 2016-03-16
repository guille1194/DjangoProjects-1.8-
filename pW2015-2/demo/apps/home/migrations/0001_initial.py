# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employ_code', models.IntegerField()),
                ('employ_name', models.CharField(max_length=48)),
                ('employ_edad', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
