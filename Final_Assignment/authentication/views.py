from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from . import forms
from django.contrib import messages
from .import models

# Create your views here.

#User signup Funtionality....
def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            registration_form = forms.RegisterForm(request.POST)
            if registration_form.is_valid():
                messages.success(request, 'Account Created Successfully!')
                registration_form.save()
                return redirect('login')
        else:
            registration_form = forms.RegisterForm()
        return render(request, './register.html', context={'form': registration_form})
    else:
        return redirect('profile')


# User Login Funtionality.....
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                name = login_form.cleaned_data['username']
                userpass = login_form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    messages.success(request, 'User Login Successfully!')
                    login(request, user)
                    return redirect('profile')
        else:
            login_form = AuthenticationForm()
        return render(request, './login.html', context={'form': login_form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        profile = models.UserProfile.objects.all()
        return render(request, './profile.html', context={'user': request.user, 'profile':profile})
    else:
        return redirect('login')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('registration')
    
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, './passchange.html', context={'form': form})
    else:
        return redirect('login')

def forgot_pass(request):
    if request.user.is_authenticated or not request.user.is_authenticated :
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, './forgotpass.html', context={'form': form})
    else:
        return redirect('login')

def userDataUpdate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.UserDetailsChange(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account Updatede Successfully!')
                form.save()
                return redirect('profile')
        else:
            form = forms.UserDetailsChange(instance = request.user)
        return render(request, './userDetailsChange.html', context={'form': form})
    else:
        return redirect('registration')