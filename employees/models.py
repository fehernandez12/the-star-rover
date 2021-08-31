import uuid

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

# Create your models here.
class Employee(models.Model):
	"""
	Base class for all employees in the application.
	This class should never be created standalone, but
	only when creating a RegularEmployee or DirectiveEmployee
	instance as well.
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, blank=True, null=True)
	phone_number = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['created']

	def get_type(self):
		try:
			obj = RegularEmployee.objects.get(employee=self)
			if obj:
				return 'Raso'
		except ObjectDoesNotExist as e:
			try:
				obj = DirectiveEmployee.objects.get(employee=self)
				if obj:
					return 'Directivo'
			except ObjectDoesNotExist as e:
				return 'N/A'

	def save(self, *args, **kwargs):
		name = self.first_name + ' ' + self.last_name
		self.slug = slugify(name)
		super().save(*args, **kwargs)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class RegularEmployee(models.Model):
	"""
	Regular Employee model. This kind of employee will be
	tasked with loading Events into the application.
	"""
	employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
	salary = models.PositiveBigIntegerField()

class DirectiveEmployee(models.Model):
	"""
	Directive Employee model. This kind of employee will be
	assigned to each event and gets paid for directing said
	event.
	"""
	employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=True)
	graduated_from = models.CharField(max_length=256)
