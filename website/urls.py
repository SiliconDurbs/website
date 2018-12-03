from django.conf.urls import url, include
from django.contrib import admin
from views.views import index, contactus, events, aboutus
from views.founders import founders
from views.user import register

urlpatterns = [
    url(r'founders/', founders, name='founders'),
    url(r'register/', register.register, name='register'),
    url(r'', index, name='index'),
]
