from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout


def login_view(request):
	if request.user.is_authenticated:
		return redirect('tribes:index')
	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				next_url = request.GET.get('next', False)
				return HttpResponseRedirect(next_url) if next_url else redirect('tribes:index')
	else:
		form = LoginForm()
	context = {
        'form': form,
        'nav': 'login',
    }
	return render(request, 'customAuth/login.html', context)


def logout_view(request):
	logout(request)
	return redirect('tribes:index')


def register_view(request):
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('tribes:index')
	else:
		form = RegistrationForm()
	context = {
		'form': form,
		'nav': 'register',
	}
	return render(request, 'customAuth/register.html', context)