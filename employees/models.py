import uuid

from django.db import models

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
	phone_number = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['created']

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
	graduated_from = models.CharField(max_length=256)
