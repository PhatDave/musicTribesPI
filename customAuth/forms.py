from django import forms
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):	
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={
			'name': 'email',
			'class':'form-control px-4',
			'placeholder':'Electronic mail',
			'autofocus': 'true',
			'required': 'true',
			}))
	username = forms.CharField(max_length=16,
		widget=forms.TextInput(attrs={
			'name': 'username',
			'class':'form-control px-4',
			'placeholder':'Username',
			'required': 'true',
			}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'name': 'password1',
			'class':'form-control px-4',
			'placeholder':'Password',
			'required': 'true',
			}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'name': 'password2',
			'class':'form-control px-4',
			'placeholder':'Repeat password',
			'required': 'true',
			}))
	
	class Meta:
		model = User
		fields = ('email', 'username', 'password1', 'password2')


class LoginForm(forms.ModelForm):
	username = forms.CharField(
		widget=forms.TextInput(attrs={
			'name': 'email',
			'class':'form-control px-4',
			'placeholder':'Username',
			'autofocus':'true',
			'required': 'true',
			}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'name': 'password1',
			'class':'form-control px-4',
			'placeholder':'Password',
			'required': 'true',
			}))

	class Meta:
		model = User
		fields = ('username', 'password')

	def clean(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			if not authenticate(username=username, password=password):
				raise forms.ValidationError('Invalid login.')
