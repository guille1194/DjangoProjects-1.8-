# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=64)),
                ('cantidad', models.IntegerField()),
                ('costo_compra', models.FloatField()),
                ('costo_venta', models.FloatField()),
                ('minimal_stock', models.IntegerField()),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Populares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('nombre', models.ForeignKey(to='principal.Inventarios')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('cantidad', models.IntegerField()),
                ('costo_venta', models.FloatField()),
                ('fecha', models.DateField(auto_now=True)),
                ('codigo', models.ForeignKey(to='principal.Inventarios')),
            ],
        ),
    ]
