from django.contrib import admin
from .models import DirectiveEmployee, RegularEmployee, Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'phone_number']

@admin.register(RegularEmployee)
class RegularAdmin(admin.ModelAdmin):
	list_display = ['employee', 'salary']

@admin.register(DirectiveEmployee)
class DirectiveAdmin(admin.ModelAdmin):
	list_display = ['employee', 'graduated_from']