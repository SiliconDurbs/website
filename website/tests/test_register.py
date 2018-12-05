# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User, Group 

class TestRegistration(TestCase):

    def setUp(self):
        self.reg_data = {
                'username': 'test',  
                'password': 'test',  
                'confirm_password': 'test',  
                'email':'test@test.co.za'}
        
        grp = Group()
        Group.objects.create(name='member')

    def tearDown(self):
        pass

    def test_empty_fields_should_return_error_message(self):
        c = Client()
        self.reg_data['username'] = ''
        self.reg_data['email'] = ''
        self.reg_data['password'] = ''
        self.reg_data['confirm_password'] = ''
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'Registration fields are required')

    def test_empty_username_should_return_error_message(self):
        c = Client()
        self.reg_data['username'] = ''
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'username is required')

    def test_empty_email_should_return_error_message(self):
        c = Client()
        self.reg_data['email'] = ''
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'email is required')

    def test_invalid_email_should_return_error_message(self):
        c = Client()
        self.reg_data['email'] = '123'
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'a valid email address is required')

    def test_empty_password_should_return_error_message(self):
        c = Client()
        self.reg_data['password'] = ''
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'password is required')

    def test_empty_confirm_password_should_return_error_message(self):
        c = Client()
        self.reg_data['confirm_password'] = ''
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'confirm password is required')

    def test_password_and_confirm_password_matches(self):
        c = Client()
        self.reg_data['confirm_password'] = 'boo'
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'passwords do not match')

    def test_register_saves_user(self):
        c = Client()
        res = c.post('/register/', self.reg_data)
        
        user = User.objects.get(username=self.reg_data['username'])

        self.assertGreater(user.id, 0)

    def test_registered_user_is_saved_to_member_group(self):
        c = Client()
        res = c.post('/register/', self.reg_data)

        user = User.objects.get(username=self.reg_data['username'])

        group = Group.objects.get(name='member')
        
        self.assertTrue(group in user.groups.all())

    def test_succesful_user_registration_should_redirects_to_profile(self):
        c = Client()
        res = c.post('/register/', self.reg_data)
        
        self.assertRedirects(res,'/user/profile/')

    def test_if_username_already_exists_should_return_error_message(self):
        c = Client()

        user = User.objects.create(username=self.reg_data['username'],
                email=self.reg_data['email'],
                password=self.reg_data['password'])
        
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'username already exists')

    def test_if_username_already_exists_should_not_redirect(self):
        c = Client()

        user = User.objects.create(username=self.reg_data['username'],
                email=self.reg_data['email'],
                password=self.reg_data['password'])
        
        res = c.post('/register/', self.reg_data)

        self.assertNotEqual(res.status_code, 301)

    def test_if_email_already_exists_should_return_error_message(self):
        c = Client()

        user = User.objects.create(username='test_123',
                email=self.reg_data['email'],
                password=self.reg_data['password'])
        
        res = c.post('/register/', self.reg_data)

        self.assertEqual(res.context['message'], 'email already exists')

    def test_if_email_already_exists_should_not_redirect(self):
        c = Client()

        user = User.objects.create(username='test_123',
                email=self.reg_data['email'],
                password=self.reg_data['password'])
        
        res = c.post('/register/', self.reg_data)

        self.assertNotEqual(res.status_code, 301)

