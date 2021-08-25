from django.urls import path

app_name = 'home'

urlpatterns = [
	path('', views.index_view, name='index'),
]