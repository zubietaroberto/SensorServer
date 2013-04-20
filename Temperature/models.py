from datetime import datetime
from django.contrib import admin
from django.db import models

# Create your models here.
class Station(models.Model):
    
    value = models.TextField();
    name = models.TextField();
    latitude = models.FloatField();
    longitude = models.FloatField();
    
    def __unicode__(self):
        return self.name;
    
    
class TemperatureMeasurement(models.Model):
    
    temperature = models.FloatField('Temperatura');
    date = models.DateTimeField('Fecha de registro', default=datetime.now(), blank=False);
    source = models.ForeignKey(Station);
    
    def __unicode__(self):
        return "Temperatura: " + self.temperature 
        + " Fecha: " + self.date 
        + " Fuente: " + self.source

admin.site.register(Station)
admin.site.register(TemperatureMeasurement)
    
    
    
