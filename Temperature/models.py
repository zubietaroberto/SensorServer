'''
Created on Apr 20, 2013

@author: zubietaroberto
@license: (CDDL-1.0)
'''

from datetime import datetime
from django.db import models

# Create your models here.
class Station(models.Model):
    
    value = models.CharField('Identificador', max_length=255)
    name = models.TextField('Nombre', default='');
    latitude = models.FloatField('Latitud', default=0);
    longitude = models.FloatField('Longitud', default=0);
    
    def __unicode__(self):
        return self.name;
    
    
class TemperatureMeasurement(models.Model):
    
    temperature = models.FloatField('Temperatura');
    date = models.DateTimeField('Fecha de registro', default=datetime.now(), blank=False);
    source = models.ForeignKey(Station);
    
    def parseDate(self):
        
        date_format = "%Y/%m/%d/%H/%M/%S"
        return self.date.strftime(date_format)
    
    
    def __unicode__(self):
        return self.source.name
    

class HumidityMeasurement(models.Model):
    
    humidity = models.FloatField('Porcentaje de Humedad', blank=False)
    date = models.DateTimeField('Fecha de registro', default=datetime.now(), blank=False)
    source = models.ForeignKey(Station)
    
    def __unicode__(self):
        return self.source.name
    
    
    
