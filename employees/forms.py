from django import forms
from .models import RegularEmployee, DirectiveEmployee
class RegularEmployeeForm(forms.ModelForm):
	use_required_attribute = False
	id = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Id'
			}
		),
		label='Id'
	)
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
        salary = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Salario en pesos (COP)'
			}
		),
		label='Salario en pesos (COP)'
	)
class DirectiveEmployeeForm(forms.ModelForm):
        use_required_attribute = False
        id = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Id'
                }
            ),
            label='Id'
        )
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