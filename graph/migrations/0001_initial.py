# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tjros',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('battery_voltage', models.FloatField(blank=True, null=True)),
                ('dissolved_oxygen', models.FloatField(blank=True, null=True)),
                ('dissolved_oxygen_saturation', models.FloatField(blank=True, null=True)),
                ('salinity', models.FloatField(blank=True, null=True)),
                ('sea_water_electrical_conductivity', models.FloatField(blank=True, null=True)),
                ('sea_water_ph_reported_on_total_scale', models.FloatField(blank=True, null=True)),
                ('sea_water_temperature', models.FloatField(blank=True, null=True)),
                ('turbidity', models.FloatField(blank=True, null=True)),
                ('water_level', models.FloatField(blank=True, null=True)),
                ('site', models.CharField(blank=True, max_length=6, null=True)),
                ('flag', models.SmallIntegerField()),
                ('ts_input', models.DateTimeField()),
            ],
            options={
                'db_table': 'tjros',
                'managed': False,
            },
        ),
    ]