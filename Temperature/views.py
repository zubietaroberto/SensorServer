from Temperature.models import TemperatureMeasurement, Station
from django.http.response import HttpResponse


def index(request):
    return HttpResponse('Index OK')

def put(request):
        
    #Get measurement Data
    measurement = TemperatureMeasurement()
    measurement.temperature = request.GET['temp']
        
    #Find the station
    station_id = request.GET['id']
    station = Station.objects.get(value=station_id)
    measurement.source = station
        
    measurement.save()
    return HttpResponse('datos de ' + station.value + ' salvados')