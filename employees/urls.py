from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
path('create', views.CreateRegularEmployeeView.as_view(), name='create_RegularEmployee'),
path('create', views.CreateDirectiveEmployeeView.as_view(), name='create_DirectiveEmployee'),
path('RegularEmployee/update', views.UpdateRegularEmployeeView.as_view(), name='RegularEmployee_update'),
path('DirectiveEmployee/update', views.UpdateDirectiveEmployeeView.as_view(), name='DirectiveEmployee_update'),
path('RegularEmployee/delete', views.RegularEmployeeDeleteView.as_view(), name='RegularEmployee_delete'),
path('DirectiveEmployee/delete', views.DirectiveEmployeeDeleteView.as_view(), name='DirectiveEmployee_delete'),
path('all', views.EmployeeListView.as_view(), name='Employee_list'),

]