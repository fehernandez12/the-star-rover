from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import ModelAgency, Model
class ModelAgencyForm(forms.ModelForm):
	use_required_attribute = False
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Nombre de la agencia'
			}
		),
		label='Nombre de la agencia'
	)
	country = CountryField().formfield(
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2'
			}
		),
		label='País de origen',
	)
	creation_year = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'data-provide': 'datepicker',
				'data-date-autoclose': 'true',
				'data-date-container': '#creation_date',
				'data-date-format': 'yyyy-mm-d',
				'placeholder': 'Fecha de creación'
			}
		),
		label='Fecha de creación'
	)
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Dirección de Correo Electrónico'
			}
		),
		label='Dirección de Correo Electrónico'
	)
	owner_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Nombre del dueño'
			}
		),
		label='Nombre del dueño'
	)
	parent_agency = forms.ModelChoiceField(
		queryset=ModelAgency.objects.all(),
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2'
			}
		),
		label='Agencia padre',
		required=False,
		empty_label='Selecciona una agencia...'
	)

	class Meta:
		model = ModelAgency
		fields = ['name', 'country', 'creation_year', 'email', 'owner_name', 'parent_agency']

class ModelsForm(forms.ModelForm):
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
	country = CountryField().formfield(
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2'
			}
		),
		label='País de origen',
	)
	birthday = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'data-provide': 'datepicker',
				'data-date-autoclose': 'true',
				'data-date-container': '#birthday',
				'data-date-format': 'yyyy-mm-d',
				'placeholder': 'Fecha de nacimiento'
			}
		),
		label='Fecha de nacimiento'
	)
	eye_color = forms.ChoiceField(
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2'
			}
		),
		label='Color de ojos',
		choices=Model.EYE_COLORS
	)
	skin_color = forms.ChoiceField(
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2'
			}
		),
		label='Color de piel',
		choices=Model.SKIN_COLORS
	)
	height = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Altura en cm.'
			}
		),
		label='Altura en cm.'
	)
	shoe_size = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Talla de zapatos'
			}
		),
		label='Talla de zapatos'
	)
	weight = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Peso en kg.'
			}
		),
		label='Peso en kg.'
	)
	particularities = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': 'form-control'
			}
		),
		label='Particularidades'
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
	agency = forms.ModelChoiceField(
		queryset=ModelAgency.objects.all(),
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2'
			}
		),
		label='Agencia de modelaje',
		required=False,
		empty_label='Selecciona una agencia...'
	)
	
	class Meta:
		model = Model
		fields = ['first_name', 'last_name', 'country', 'birthday',
			'eye_color', 'skin_color', 'height', 'shoe_size', 'weight',
			'particularities', 'salary', 'agency']