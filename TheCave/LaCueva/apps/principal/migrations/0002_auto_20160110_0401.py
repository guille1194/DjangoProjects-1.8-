# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventarios',
            old_name='minimal_stock',
            new_name='stock',
        ),
    ]
