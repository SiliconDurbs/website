# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'GET':
        return render(request, 'website/user/register.html', {})

    if request.method == 'POST':
        return render(request, 'website/user/register.html', {})
