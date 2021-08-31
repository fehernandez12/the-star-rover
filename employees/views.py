from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import  Employee, RegularEmployee, DirectiveEmployee
from .forms import RegularEmployeeForm, DirectiveEmployeeForm
# Create your views here.

class EmployeeListView(LoginRequiredMixin, ListView):
	model = Employee

	def get_queryset(self, **kwargs):
		return Employee.objects.all()

class EmployeeDetailView(LoginRequiredMixin, DetailView):
	model = Employee

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		try:
			obj = RegularEmployee.objects.get(employee=self.object)
		except ObjectDoesNotExist as e:
			try:
				obj = DirectiveEmployee.objects.get(employee=self.object)
			except ObjectDoesNotExist as e:
				return None
		context['detail'] = obj
		return context

def create_employee(request, emp_type):
	if request.method == 'POST':
		data = request.POST
		employee = Employee(
			first_name=data['first_name'],
			last_name=data['last_name'],
			phone_number=data['phone_number']
		)
		employee.save()
		if data.get('salary'):
			RegularEmployee.objects.create(employee=employee, salary=data['salary'])
		elif data.get('graduated_from'):
			DirectiveEmployee.objects.create(employee=employee, graduated_from=data['graduated_from'])
		messages.success(request, '¡El empleado ha sido registrado!')
		return HttpResponseRedirect(reverse('employees:employee_detail', kwargs={'slug': employee.slug}))
	else:
		if emp_type == 'regular':
			form = RegularEmployeeForm()
			return render(request, 'employees/employee_form.html', {'form': form, 'type': 'regular'})
		elif emp_type == 'directive':
			form = DirectiveEmployeeForm()
			return render(request, 'employees/employee_form.html', {'form': form, 'type': 'directive'})

def edit_employee(request, slug):
	employee = Employee.objects.get(slug=slug)
	emp_type = ''
	if request.method == 'POST':
		data = request.POST
		salary = data.get('salary')
		graduated_from = data.get('graduated_from')
		if salary:
			emp_form = RegularEmployeeForm(instance=employee, data=request.POST)
		elif graduated_from:
			emp_form = DirectiveEmployeeForm(instance=employee, data=request.POST)
		if emp_form.is_valid():
			if data.get('salary'):
				obj = RegularEmployee.objects.get(employee=employee)
				employee.first_name = data['first_name']
				employee.last_name = data['last_name']
				employee.phone_number = data['phone_number']
				employee.save()
				obj.salary = data['salary']
				obj.save()
			elif data.get('graduated_from'):
				obj = DirectiveEmployee.objects.get(employee=employee)
				employee.first_name = data['first_name']
				employee.last_name = data['last_name']
				employee.phone_number = data['phone_number']
				employee.save()
				obj.graduated_from = data['graduated_from']
				obj.save()
			messages.success(request, '¡El empleado ha sido actualizado!')
			return HttpResponseRedirect(reverse('employees:employee_detail', kwargs={'slug': employee.slug}))
	else:
		try:
			obj = DirectiveEmployee.objects.get(employee=employee)
			emp_type = 'directive'
		except ObjectDoesNotExist as e:
			try:
				obj = RegularEmployee.objects.get(employee=employee)
				emp_type = 'regular'
			except ObjectDoesNotExist as e:
				return None
		if emp_type == 'directive':
			emp_form = DirectiveEmployeeForm(instance=employee)
			emp_form.fields['graduated_from'].initial = obj.graduated_from
		elif emp_type == 'regular':
			emp_form = RegularEmployeeForm(instance=employee)
			emp_form.fields['salary'].initial = obj.salary
		return render(request, 'employees/employee_form.html', {'form': emp_form, 'type': emp_type})


class EmployeeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Employee

	def get_success_url(self):
		messages.success(self.request, '¡El empleado ha sido eliminado exitosamente!')
		return reverse_lazy('employees:employees_list')