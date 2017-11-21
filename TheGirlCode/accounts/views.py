# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def login(request):

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':  # when submit button is clicked with the user details
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:  # GET method, i.e. user is requesting the page
        form = RegistrationForm()

    return render(request, 'accounts/sign_up.html', {'form': form})


def view_profile(request):

    return render(request, 'accounts/profile.html', {'user': request.user})


def settings_profile(request):

    return render(request, 'accounts/settings.html')


def edit_profile(request):

    if request.method == 'POST':  # When user is submitting the updated info
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:  # When the user wants to view the page
        form = EditProfileForm(instance=request.user)

        return render(request, 'accounts/editprofile.html', {'form': form})


def change_password(request):

    if request.method == 'POST':  # When user is submitting the updated info
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Doesn't logout the user after pw change
            return redirect('/account/profile')

        else:  # If form is not valid, redirects to the same page
            return redirect('/account/settings/edit/change_password')

    else:
        form = PasswordChangeForm(user=request.user)

        return render(request, 'accounts/changepassword.html', {'form': form})
