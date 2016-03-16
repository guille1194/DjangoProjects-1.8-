# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_perfiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='image',
            field=models.ImageField(upload_to=b'user_image', blank=True),
        ),
    ]
