# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_nomecreen'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiles',
            name='image',
            field=models.ImageField(default=1, upload_to=b'user_image'),
            preserve_default=False,
        ),
    ]
