# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from validate_email import validate_email
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect

def save_user(UserModel, username, password, email):
    pass

def register(request):
    if request.method == 'GET':
        return render(request, 'website/user/register.html', {})

    if request.method == 'POST':

        #TODO clean data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        #data validation
        if not username and not email and not password and not confirm_password:
            return render(request, 'website/user/register.html', {
                'message': 'Registration fields are required'
                })

        if not username:
            return render(request, 'website/user/register.html', {
                'message': 'username is required'
                })

        if not email:
            return render(request, 'website/user/register.html', {
                'message': 'email is required',
                })

        if not validate_email(email):
            return render(request, 'website/user/register.html', {
                'message': 'a valid email address is required'
                })

        if not password:
            return render(request, 'website/user/register.html', {
                'message': 'password is required'
                })

        if not confirm_password:
            return render(request, 'website/user/register.html', {
                'message': 'confirm password is required'
                })
            
        if password != confirm_password:
            return render(request, 'website/user/register.html', {
                'message': 'passwords do not match'
                })


        #check if username already exits
        username_exists = False
        try:
             exists = User.objects.get(username=username)
        except User.DoesNotExist:
            username_exists = True 

        if not username_exists:
            return render(request, 'website/user/register.html', {
                'message': 'username already exists'
                })

        #check if email already exists
        email_exists = False
        try:
             exists = User.objects.get(email=email)
        except User.DoesNotExist:
            email_exists = True 

        if not email_exists:
            return render(request, 'website/user/register.html', {
                'message': 'email already exists'
                })

        #save user
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.save()

        if user.id > 0:
            #add all registering users to the members role
            group = Group.objects.get(name='member')
            group.user_set.add(user);

            return HttpResponseRedirect('/user/profile/')

        return render(request, 'website/user/register.html', {'message':''})

