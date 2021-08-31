from django.urls import path
from . import views

app_name = 'models'

urlpatterns = [
	path('create', views.CreateModelView.as_view(), name='create_model'),
	path('<slug:slug>/update', views.UpdateModelView.as_view(), name='update_model'),
	path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
	path('portfolio/<int:pk>/upload', views.PhotoCreateView.as_view(), name='create_photo'),
	path('photo/<uuid:pk>/delete', views.PhotoDeleteView.as_view(), name='photo_delete'),
	path('measures/<int:pk>', views.MeasuresUpdateView.as_view(), name='update_measures'),
	path('all', views.ModelListView.as_view(), name='model_list'),
	path('detail/<slug:slug>', views.ModelDetailView.as_view(), name='model_detail'),
	path('agencies/create', views.CreateAgencyView.as_view(), name='create_agency'),
	path('agencies/all', views.AgencyListView.as_view(), name='agency_list'),
	path('agencies/<slug:slug>', views.AgencyDetailView.as_view(), name='agency_detail'),
	path('agencies/<slug:slug>/update', views.UpdateAgencyView.as_view(), name='agency_update'),
	path('agencies/<slug:slug>/delete', views.AgencyDeleteView.as_view(), name='agency_delete'),
]