from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from time import sleep

from django.contrib.auth.models import User

class Login(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get('password')
        isRemember = request.POST.get('isRemember')
        user = authenticate(username=username, password=password)
        if(user and user.is_active):
            login(request, user)
            ''' If remember login, use global expire time, 2 weeks as a default '''
            if(isRemember):
                request.session.set_expiry(None)
            else:
                request.session.set_expiry(0) # Set expire time to 0 as not remember
            request.session['username'] = username
            request.session['password'] = password
            messages.error(request, "Login successfully! Redirect to user page in 2s.")
            ''' Redirect to user info page '''
            sleep(2)
            return redirect(reverse('userinfo'))
        else:
            ''' Login failed, refresh login page '''
            messages.error(request, 'Wrong user name or password! Please try again after 2s.')
            sleep(2)
            return redirect(reverse('login'))
        
class Register(View):
    def get(self, request):
        return render(request, "register.html")
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get('password')
        result = self.add_new_user(username=username, password=password)
        if(result):
            messages.error(request, 'Successfully registered! Please login.')
            sleep(2)
            return redirect(reverse('login'))
        else:
            messages.error(request, 'User and password already exist!')
            sleep(2)
            return redirect(reverse('register'))
    def add_new_user(self, username, password):
        user = authenticate(username=username, password=password)
        if(user):
            ''' User and password already exist '''
            return False
        User.objects.create_user(username=username, password=password)
        return True
