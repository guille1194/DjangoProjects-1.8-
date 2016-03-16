# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacion',
            name='tecnico',
            field=models.ForeignKey(default=1, to='principal.Personal'),
            preserve_default=False,
        ),
    ]
