from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from customAuth.models import User


def loginView(request):
    if request.method == 'GET':
        return render(request, 'customAuth/login.html')
    elif request.method == 'POST':
        auth = authenticate(username=request.POST['username'], password=request.POST['password'])
        if auth is not None:
            login(request, auth)
        return HttpResponseRedirect(reverse('tribes:index'))


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth:login'))


def registerView(request):
    if request.method == 'GET':
        return render(request, 'customAuth/register.html')
    elif request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return HttpResponseRedirect(reverse('tribes:index'))
