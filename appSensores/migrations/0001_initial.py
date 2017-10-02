# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 19:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sensorAcelerometro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejeX', models.FloatField()),
                ('ejeY', models.FloatField()),
                ('ejeZ', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='sensorActuador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actuadorUno', models.BooleanField(default=False)),
                ('actuadorDos', models.BooleanField(default=False)),
                ('actuadorTres', models.BooleanField(default=False)),
                ('actuadorCuatro', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='sensorDistancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distancia', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='sensorHumedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humedad', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
        migrations.CreateModel(
            name='sensorMovimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimiento', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='sensorMuestreo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaMuestreo', models.DateField()),
                ('origenMuestreo', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='sensorTemperatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('idMuestreo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSensores.sensorMuestreo')),
            ],
        ),
        migrations.AddField(
            model_name='sensormovimiento',
            name='idMuestreo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSensores.sensorMuestreo'),
        ),
        migrations.AddField(
            model_name='sensorhumedad',
            name='idMuestreo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSensores.sensorMuestreo'),
        ),
        migrations.AddField(
            model_name='sensordistancia',
            name='idMuestreo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSensores.sensorMuestreo'),
        ),
        migrations.AddField(
            model_name='sensoractuador',
            name='idMuestreo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSensores.sensorMuestreo'),
        ),
        migrations.AddField(
            model_name='sensoracelerometro',
            name='idMuestreo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSensores.sensorMuestreo'),
        ),
    ]
