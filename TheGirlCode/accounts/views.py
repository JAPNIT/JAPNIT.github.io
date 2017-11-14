# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm

def login(request):

    return render(request, 'accounts/login.html' )

def profile(request):

    return render(request, 'accounts/profile.html' )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/sign_up.html' , {'form' : form})