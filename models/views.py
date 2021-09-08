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

from .models import ModelAgency, Models, Photo, Portfolio, Measurements
from .forms import ModelAgencyForm, ModelsForm, MeasurementsForm, PhotoForm

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
		context['models'] = Models.objects.filter(
			agency=self.object).filter(active=True)
		return context

class AgencyListView(LoginRequiredMixin, ListView):
	model = ModelAgency

class AgencyDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = ModelAgency
	success_url = reverse_lazy('models:agency_list')
	success_message = '¡La agencia ha sido eliminada exitosamente!'

class CreateModelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Models
	form_class = ModelsForm
	success_message = f'¡La modelo ha sido registrada!'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['create'] = True
		return context

class UpdateModelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Models
	form_class = ModelsForm
	success_message = f'¡La información de la modelo ha sido actualizada!'

class ModelDetailView(LoginRequiredMixin, DetailView):
	model = Models

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		portfolio = Portfolio.objects.get(model=self.object)
		context['portfolio'] = portfolio
		context['photos'] = Photo.objects.filter(portfolio=portfolio)
		context['measures'] = Measurements.objects.get(measured_model=self.object)
		return context

class ModelListView(LoginRequiredMixin, ListView):
	model = Models

	def get_queryset(self, **kwargs):
		return Models.objects.filter(active=True)

class MeasuresUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Measurements
	form_class = MeasurementsForm
	success_message = f'¡Los datos han sido actualizados!'

	def get_success_url(self):
		slug = self.object.measured_model.slug
		return reverse_lazy('models:model_detail', kwargs={'slug': slug})

	def form_valid(self, form):
		obj = Measurements.objects.get(id=self.object.id)
		self.object.measured_model = obj.measured_model
		return super(MeasuresUpdateView, self).form_valid(form)

class PortfolioDetailView(LoginRequiredMixin, DetailView):
	model = Portfolio

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['photos'] = Photo.objects.filter(portfolio=self.object)
		return context

class PhotoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Photo
	form_class = PhotoForm
	success_message = '¡Foto subida exitosamente!'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['portfolio'] = Portfolio.objects.get(id=self.kwargs['pk'])
		return context

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.portfolio = Portfolio.objects.get(id=self.kwargs['pk'])
		return super(PhotoCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('models:portfolio_detail', kwargs={'pk': self.kwargs['pk']})

class PhotoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Photo
	success_message = '¡La foto fue borrada exitosamente!'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super(PhotoDeleteView, self).post(request, *args, **kwargs)

	def get_success_url(self):
		portfolio = self.object.portfolio
		messages.success(self.request, '¡La foto fue borrada exitosamente!')
		return reverse_lazy('models:portfolio_detail', kwargs={'pk': portfolio.id})