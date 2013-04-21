'''
Created on Apr 20, 2013

@author: zubietaroberto
@license: (CDDL-1.0)
'''
from Temperature import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^put/(?P<temperature>\d+\.\d+)/(?P<humidity>\d+\.\d+)/(?P<station_id>\w+)/$', views.put, name='put'),
    url(r'^ajax/station/$', views.get_stations, name='ajax_station_all'),
)