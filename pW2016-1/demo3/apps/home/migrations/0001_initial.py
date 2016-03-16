# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('user_perfil', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_code', models.IntegerField()),
                ('student_name', models.CharField(max_length=64)),
                ('student_age', models.IntegerField()),
                ('student_semester', models.IntegerField()),
                ('student_career', models.CharField(max_length=64)),
                ('student_image', models.ImageField(null=True, upload_to='student_perfil/', blank=True)),
            ],
        ),
    ]
