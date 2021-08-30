from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from rest_framework.parsers import JSONParser

from .models import ModelAgency, Model
from .serializers import ModelAgencySerializer
from .forms import ModelAgencyForm, ModelsForm

# Create your views here.
class CreateAgencyView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = ModelAgency
	form_class = ModelAgencyForm
	success_message = f'¡La agencia ha sido registrada!'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['create'] = True
		return context

class UpdateAgencyView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = ModelAgency
	form_class = ModelAgencyForm
	success_message = f'¡La agencia ha sido actualizada!'

class AgencyDetailView(LoginRequiredMixin, DetailView):
	model = ModelAgency

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['models'] = Model.objects.filter(
			agency=self.object).filter(active=True)
		return context

class AgencyListView(LoginRequiredMixin, ListView):
	model = ModelAgency

class AgencyDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = ModelAgency
	success_url = reverse_lazy('models:agency_list')
	success_message = '¡La agencia ha sido eliminada exitosamente!'

class CreateModelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Model
	form_class = ModelsForm
	success_message = f'¡La modelo ha sido registrada!'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['create'] = True
		return context

class UpdateModelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	pass

class ModelDetailView(LoginRequiredMixin, DetailView):
	pass

class ModelListView(LoginRequiredMixin, ListView):
	pass

class ModelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	pass