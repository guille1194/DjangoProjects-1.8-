# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_nomecreen_male'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestMultiDataSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
