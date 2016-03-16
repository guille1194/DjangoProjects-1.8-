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
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('ciudad', models.ForeignKey(to='principal.Ciudad')),
                ('compania', models.ForeignKey(to='principal.Compania')),
            ],
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.CharField(max_length=64)),
                ('direccion', models.CharField(max_length=240)),
                ('cantidad_equipo', models.IntegerField(blank=True)),
                ('cantidad_tv', models.IntegerField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('fecha_instalacion', models.DateField(auto_now_add=True)),
                ('contrato', models.ForeignKey(to='principal.Contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Inventarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(blank=True)),
                ('nombre', models.CharField(max_length=48)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('ciudad', models.ForeignKey(to='principal.Ciudad')),
                ('compania', models.ForeignKey(to='principal.Compania')),
                ('nombre', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=256)),
                ('pago', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='instalacion',
            name='equipo_instalado',
            field=models.ManyToManyField(to='principal.Inventarios'),
        ),
        migrations.AddField(
            model_name='instalacion',
            name='tipo_servicio',
            field=models.ManyToManyField(to='principal.Tipo_servicio'),
        ),
    ]
