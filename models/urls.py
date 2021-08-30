from django.urls import path
from . import views

app_name = 'models'

urlpatterns = [
	path('models/create', views.CreateModelView.as_view(), name='create_model'),
	path('agencies/create', views.CreateAgencyView.as_view(), name='create_agency'),
	path('agencies/all', views.AgencyListView.as_view(), name='agency_list'),
	path('agencies/<slug:slug>', views.AgencyDetailView.as_view(), name='agency_detail'),
	path('agencies/<slug:slug>/update', views.UpdateAgencyView.as_view(), name='agency_update'),
	path('agencies/<slug:slug>/delete', views.AgencyDeleteView.as_view(), name='agency_delete'),
]