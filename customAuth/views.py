from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout


def login_view(request):
	user = request.user
	if user.is_authenticated:
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
				if next_url:
					return HttpResponseRedirect(next_url)
				else:
					return redirect('tribes:index')
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