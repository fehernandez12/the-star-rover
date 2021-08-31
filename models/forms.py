from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import ModelAgency, Models, Measurements
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
		choices=Models.EYE_COLORS
	)
	skin_color = forms.ChoiceField(
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2'
			}
		),
		label='Color de piel',
		choices=Models.SKIN_COLORS
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
	active = forms.BooleanField(
		required=False,
		widget=forms.CheckboxInput(
			attrs={
				'class': 'form-check-input'
			}
		),
		label='Activa'
	)
	
	class Meta:
		model = Models
		fields = ['first_name', 'last_name', 'country', 'birthday',
			'eye_color', 'skin_color', 'height', 'shoe_size', 'weight',
			'particularities', 'salary', 'agency', 'active']

class MeasurementsForm(forms.ModelForm):
	chest = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Medida del busto en cm'
			}
		),
		label='Medida del busto en cm'
	)
	waist = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Medida de la cintura en cm'
			}
		),
		label='Medida de la cintura en cm'
	)
	hips = forms.IntegerField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Medida de la cadera en cm'
			}
		),
		label='Medida de la cadera en cm'
	)
	measured_model = forms.ModelChoiceField(
		queryset=Models.objects.filter(active=True),
		widget=forms.Select(
			attrs={
				'class': 'form-control select2',
				'data-toggle': 'select2',
				'disabled': 'true'
			}
		),
		label='Modelo',
		required=False
	)
	class Meta:
		model = Measurements
		fields = ['chest', 'waist', 'hips', 'measured_model']