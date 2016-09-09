# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models

class Tjros(models.Model):
    time = models.DateTimeField(primary_key=True)
    battery_voltage = models.FloatField(blank=True, null=True)
    dissolved_oxygen = models.FloatField(blank=True, null=True)
    dissolved_oxygen_saturation = models.FloatField(blank=True, null=True)
    salinity = models.FloatField(blank=True, null=True)
    sea_water_electrical_conductivity = models.FloatField(blank=True, null=True)
    sea_water_ph_reported_on_total_scale = models.FloatField(blank=True, null=True)
    sea_water_temperature = models.FloatField(blank=True, null=True)
    turbidity = models.FloatField(blank=True, null=True)
    water_level = models.FloatField(blank=True, null=True)
    site = models.CharField(max_length=6, blank=True, null=True)
    flag = models.SmallIntegerField()
    ts_input = models.DateTimeField()

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        assert isinstance(self.time, object)
        return str(self.time)

    class Meta:
        managed = False
        db_table = 'tjros'
