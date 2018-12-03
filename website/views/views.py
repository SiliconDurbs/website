# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    if request.method == 'GET':
        return render(request, 'website/index.html', {})

    if request.method == 'POST':
        return render(request, 'website/index.html', {})

def aboutus(request):
    if request.method == 'GET':
        return render(request, 'website/aboutus.html', {})

    if request.method == 'POST':
        return render(request, 'website/aboutus.html', {})

def contactus(request):
    if request.method == 'GET':
        return render(request, 'website/contactus.html', {})

    if request.method == 'POST':
        return render(request, 'website/contactus.html', {})

def events(request):
    if request.method == 'GET':
        return render(request, 'website/events.html', {})

    if request.method == 'POST':
        return render(request, 'website/events.html', {})
