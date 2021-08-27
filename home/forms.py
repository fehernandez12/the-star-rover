from django import forms
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm):
	first_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Nombres'
			}
		),
		label='Nombres'
	)
	last_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Apellidos'
			}
		),
		label='Apellidos'
	)
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Dirección de e-mail'
			}
		),
		label='Dirección de e-mail'
	)
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
	birthday = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'data-provide': 'datepicker',
				'data-date-autoclose': 'true',
				'data-date-container': '#birthday',
				'data-date-format': 'yyyy-mm-d'
			}
		),
		label='Fecha de nacimiento'
	)
	photo = forms.ImageField(
		widget=forms.FileInput(
			attrs={
				'class': 'form-control'
			}
		)
	)
	class Meta:
		model = Profile
		fields = ('birthday', 'photo')