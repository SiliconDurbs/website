# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def founders(request):
    if request.method == 'GET':
        return render(request, 'website/founders/founders.html', {})

    if request.method == 'POST':
        return render(request, 'website/founders/founders.html', {})

@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'website/founders/create.html', {})

    if request.method == 'POST':
        return render(request, 'website/founders/create.html', {})
