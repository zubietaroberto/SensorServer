'''
Created on Apr 20, 2013

@author: zubietaroberto
@license: (CDDL-1.0)
'''

from Temperature.Common import serialize_t_measure
from Temperature.models import Station, TemperatureMeasurement, \
    HumidityMeasurement
from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'Temperature/index.html', {"title": "Index"})

def display_station(request, station_id):
    
    station = get_object_or_404(Station, value=station_id)
        
    dictionary =  {
                    'title': station.name, 
                    'head': station.name,
                    'value': station.value,
                    'data': serialize_t_measure(station),
                   }
    return render(request, 
                  'Temperature/station.html',
                  dictionary)

def put(request, temperature, humidity, station_id):
    
    #Get temperature_measurement Data
    temperature_measurement = TemperatureMeasurement()
    temperature_measurement.temperature = temperature
    
    #Get Humidity measurement data
    humidity_measurement = HumidityMeasurement()
    humidity_measurement.humidity = humidity
        
    #Find the station
    station = get_object_or_404(Station, value=station_id)
    temperature_measurement.source = station
    humidity_measurement.source = station
    
    #Save Data
    temperature_measurement.save()
    humidity_measurement.save()
    
    return HttpResponse('datos de ' + station.value + ' salvados')

def get_stations(request):
    data = serializers.serialize('json', Station.objects.all())
    return HttpResponse(data, content_type="application/json")

def get_station_t_measurements(request, station_id):
    station = get_object_or_404(Station, value=station_id)
    return HttpResponse(serialize_t_measure(station), content_type="application/json")