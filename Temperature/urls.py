'''
Created on Apr 20, 2013

@author: RobertoEduardo
'''
from Temperature import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^put/$', views.put, name='put'),
)