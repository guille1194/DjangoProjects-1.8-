# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20151010_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomecreen',
            name='male',
            field=models.BooleanField(default=True),
        ),
    ]
