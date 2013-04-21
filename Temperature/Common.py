'''
Created on Apr 21, 2013

@author: zubietaroberto
'''
from Temperature.models import TemperatureMeasurement
from django.core import serializers

""" 
Sensacion Termica, cortesia de Luis Jordan 
"""
def sensacion_termica(temp_c, humedad):
    
    RH = humedad;
    Tf = temp_c  *  9/5 + 32; 
    
    return -42.379+2.049*Tf+10.143*RH-0.22476*Tf*RH-6.8378E-3*(Tf^2)-5.4817E-2*RH^2+1.2287E-3*(Tf^2)*RH+ 8.5282E-4*RH^2*(Tf)-1.99E-6*Tf^2*RH^2

def serialize_t_measure(station):
    measurements = TemperatureMeasurement.objects.filter(source=station)
    return serializers.serialize('json', measurements)