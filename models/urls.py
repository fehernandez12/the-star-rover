from django.urls import path
from .views import CreateAgencyView

app_name = 'models'

urlpatterns = [
	path('agency/create', CreateAgencyView.as_view(), name='create_agency'),
]