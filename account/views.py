from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login, logout as dj_logout

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate


def account(request):
    user = request.user
    return render(request, "login.html", {'user': user})


def login(request):
    context = {}

    if request.method == "POST":
        user = authenticate(request, username=request.POST['user'], password=request.POST['password'])
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('account:login'))
        else:
            context = {
                'error': 'Bad username or password.'
            }
    return render(request, 'account/login.html', context)


def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('account:login'))


def sign_up(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_name = request.POST['user']
        email = request.POST['email']
        if password == confirm_password:
            if User.objects.create_user(user_name, email, password):
                return HttpResponseRedirect(reverse('account:login'))
            else:
                context = {
                    'error': 'Could not create user account - please try again.'
                }
        else:
            context = {
                'error': 'Passwords did not match. Please try again.'
            }

    return render(request, 'account/sign_up.html', context)
