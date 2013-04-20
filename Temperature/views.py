from Temperature.models import TemperatureMeasurement, Station
from django.http.response import HttpResponse


def index(request):
    return HttpResponse('Index OK')

def put(request, temperature, station_id):
    #Get measurement Data
    measurement = TemperatureMeasurement()
    measurement.temperature = temperature
        
    #Find the station
    station = Station.objects.get(value=station_id)
    measurement.source = station
        
    measurement.save()
    return HttpResponse('datos de ' + station.value + ' salvados')