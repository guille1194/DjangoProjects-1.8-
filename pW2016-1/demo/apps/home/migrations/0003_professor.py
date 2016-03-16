# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('professor_name', models.CharField(max_length=64)),
                ('class_room', models.IntegerField()),
                ('students', models.ManyToManyField(to='home.Student')),
            ],
        ),
    ]
