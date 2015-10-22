__author__ = 'Arpit Gang'
from django.conf.urls import url
from django.conf.urls import *


from . import views

urlpatterns = [


    url(r'^$', views.index, name='home'),
    url(r'^/form/', views.form, name='form'),
]

