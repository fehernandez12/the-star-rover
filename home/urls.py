from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('home/', views.dashboard, name='dashboard'),
	path('password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('edit/', views.edit, name='edit'),
]