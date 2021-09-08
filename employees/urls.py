from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
	path('<str:emp_type>/create', views.create_employee, name='employee_create'),
	path('create/<slug:slug>', views.edit_employee, name='employee_edit'),
	path('<slug:slug>/delete', views.EmployeeDeleteView.as_view(), name='employee_delete'),
	path('all', views.EmployeeListView.as_view(), name='employees_list'),
	path('<slug:slug>', views.EmployeeDetailView.as_view(), name='employee_detail'),
]