'''
Created on Apr 20, 2013

@author: zubietaroberto
@license: (CDDL-1.0)
'''

from Temperature.models import TemperatureMeasurement, Station, \
    HumidityMeasurement
from django.core import serializers
from django.core.serializers import json
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def put(request, temperature, humidity, station_id):
    
    #Get temperature_measurement Data
    temperature_measurement = TemperatureMeasurement()
    temperature_measurement.temperature = temperature
    
    #Get Humidity measurement data
    humidity_measurement = HumidityMeasurement()
    humidity_measurement.humidity = humidity
        
    #Find the station
    station = Station.objects.get_or_create(value=station_id)
    temperature_measurement.source = station
    humidity_measurement.source = station
    
    #Save Data
    temperature_measurement.save()
    humidity_measurement.save()
    
    return HttpResponse('datos de ' + station.value + ' salvados')

def get_stations(request):
    data = serializers.serialize('json', Station.objects.all())
    return HttpResponse(data, content_type="application/json")