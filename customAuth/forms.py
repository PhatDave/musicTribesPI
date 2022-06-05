from django import forms
from django.contrib.auth import authenticate
from .models import User


class LoginForm(forms.ModelForm):
	username = forms.CharField(
		widget=forms.TextInput(attrs={
			'name': 'email',
			'class':'form-control form-control',
			'placeholder':'Username',
			'autofocus':'true',
			'required': 'true',
			}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'name': 'password1',
			'class':'form-control form-control',
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
