# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='employ_image',
            field=models.ImageField(default=1, upload_to=b'employ_image'),
            preserve_default=False,
        ),
    ]
