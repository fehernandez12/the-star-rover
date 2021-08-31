from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse

from .models import  Employee, RegularEmployee, DirectiveEmployee
from .forms import RegularEmployeeForm, DirectiveEmployeeForm
# Create your views here.

class EmployeeListView(LoginRequiredMixin, ListView):
	model = Employee

	def get_queryset(self, **kwargs):
		return Employee.objects.filter(active=True)

class CreateRegularEmployeeView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = RegularEmployee
	form_class = RegularEmployeeForm
	success_message = f'¡El empleado raso ha sido registrado!'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['create'] = True
		return context


class UpdateRegularEmployeeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = RegularEmployee
	form_class = RegularEmployeeForm
	success_message = f'¡La información del empleado raso ha sido actualizada!'


class RegularEmployeeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = RegularEmployee
	success_url = reverse_lazy('models:RegularEmployee_list')
	success_message = '¡El empleado raso ha sido eliminado exitosamente!'


class CreateDirectiveEmployeeView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = DirectiveEmployee
	form_class = DirectiveEmployeeForm
	success_message = f'¡El empleado directivo ha sido registrado!'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['create'] = True
		return context


class UpdateDirectiveEmployeeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = DirectiveEmployee
	form_class = DirectiveEmployeeForm
	success_message = f'¡La información del empleado directivo ha sido actualizada!'


class DirectiveEmployeeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = DirectiveEmployee
	success_url = reverse_lazy('models:DirectiveEmployee_list')
	success_message = '¡El empleado directivo ha sido eliminado exitosamente!'
