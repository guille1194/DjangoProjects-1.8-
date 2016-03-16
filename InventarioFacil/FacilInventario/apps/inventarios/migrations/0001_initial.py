# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=64)),
                ('numero_piezas', models.IntegerField()),
                ('unidad_medida', models.CharField(max_length=2)),
                ('gramaje', models.FloatField()),
                ('familia', models.CharField(max_length=24)),
                ('precio_lista', models.FloatField()),
                ('descuento_oferta', models.FloatField()),
                ('precio_factura', models.FloatField()),
                ('margen_ganancia_sugerido', models.FloatField()),
                ('precio_sugerido', models.FloatField()),
                ('fecha_entrada', models.DateField(auto_now_add=True)),
                ('fecha_caducidad', models.DateField()),
            ],
        ),
    ]
