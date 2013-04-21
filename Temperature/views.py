'''
Created on Apr 20, 2013

@author: zubietaroberto
@license: (CDDL-1.0)
'''

from Temperature.models import TemperatureMeasurement, Station, \
    HumidityMeasurement
from django.http.response import HttpResponse


def index(request):
    return HttpResponse('Index OK')

def put(request, temperature, humidity, station_id):
    
    #Get temperature_measurement Data
    temperature_measurement = TemperatureMeasurement()
    temperature_measurement.temperature = temperature
    
    #Get Humidity measurement data
    humidity_measurement = HumidityMeasurement()
    humidity_measurement.humidity = humidity
        
    #Find the station
    station = Station.objects.get(value=station_id)
    temperature_measurement.source = station
    humidity_measurement.source = station
    
    #Save Data
    temperature_measurement.save()
    humidity_measurement.save()
    
    return HttpResponse('datos de ' + station.value + ' salvados')