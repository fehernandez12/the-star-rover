from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import ModelAgency

class ModelAgencySerializer(CountryFieldMixin, serializers.ModelSerializer):
	class Meta:
		model = ModelAgency
		fields = ('id', 'name', 'country', 'creation_year', 
			'email', 'owner_name', 'parent_agency')