# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_perfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='NomeCreen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=24)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
