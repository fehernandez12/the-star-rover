from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import ModelAgency
from .serializers import ModelAgencySerializer

# Create your views here.
@csrf_exempt
def agency_list(request):
	if request.method == 'GET':
		agencies = ModelAgency.objects.all()
		serializer = ModelAgencySerializer(agencies, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ModelAgencySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def agency_detail(request):
	# To do later
	pass


class CreateAgencyView(LoginRequiredMixin, CreateView):
	model = ModelAgency
	fields = ['name', 'country', 'creation_year', 
		'email', 'owner_name', 'parent_agency']