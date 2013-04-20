'''
Created on Apr 20, 2013

@author: RobertoEduardo
'''
from Temperature.models import Station, TemperatureMeasurement
from django.contrib import admin



class StationAdmin(admin.ModelAdmin):
    fields = ['value', 'name', 'latitude', 'longitude',]
    
class TemperatureAdmin(admin.ModelAdmin):
    fields = ['temperature', 'date', 'source']

admin.site.register(Station, StationAdmin)
admin.site.register(TemperatureMeasurement, TemperatureAdmin)