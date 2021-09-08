from django import forms
from .models import RegularEmployee, DirectiveEmployee
class RegularEmployeeForm(forms.ModelForm):
	use_required_attribute = False
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
	phone_number = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Número de telofono'
			}
		),
		label='Número de teléfono'
	)
	salary = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Salario en pesos (COP)'
			}
		),
		label='Salario en pesos (COP)'
	)

	class Meta:
		model = RegularEmployee
		fields = ['first_name', 'last_name', 'phone_number', 'salary']

class DirectiveEmployeeForm(forms.ModelForm):
	use_required_attribute = False
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
	phone_number = forms.CharField(
	widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Número de telofono'
			}
		),
		label='Número de telofono'
	)
	graduated_from = forms.CharField(
	widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Graduado de'
			}
		),
		label='Graduado de'
	)

	class Meta:
		model = DirectiveEmployee
		fields = ['first_name', 'last_name', 'phone_number', 'graduated_from']