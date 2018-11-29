from django.conf.urls import url, include
from django.contrib import admin
from views import index, contactus, events, aboutus

urlpatterns = [
    url(r'', index, name='index'),
]
