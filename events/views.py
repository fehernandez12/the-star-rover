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

from .models import Event, Designer
# Create your views here.
class CreateDesignerView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Designer
	form_class = DesignerForm
	success_message = f'¡El diseñador ha sido registrado!'

	def get_context_data(self):
		context = super().get_context_data(**kwargs)
		context['create'] = True
		return context

class UpdateDesignerView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Designer
	form_class = DesignerForm
	success_message = '¡El diseñador ha sido actualizado!'

class DesignerListView(LoginRequiredMixin, ListView):
	model = Designer