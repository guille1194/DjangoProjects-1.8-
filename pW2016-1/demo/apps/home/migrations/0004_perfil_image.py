# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='image',
            field=models.ImageField(upload_to='user_image', blank=True),
        ),
    ]
