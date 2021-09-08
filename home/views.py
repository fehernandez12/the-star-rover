from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from events.models import Event
from .models import Profile
from .forms import UserEditForm, ProfileEditForm


# Create your views here.
class AuthenticateView(LoginView):
	redirect_authenticated_user = True

class PasswordView(SuccessMessageMixin, PasswordChangeView):
	success_message = '¡Tu password ha sido cambiado exitosamente!'
	success_url = reverse_lazy('dashboard')

@login_required
def dashboard(request):
	return render(request, 'home/home.html', {'section': 'dashboard'})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,
			data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
			data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.add_message(request, messages.SUCCESS, 'Tu perfil ha sido editado exitosamente.')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'home/edit.html', {
		'user_form': user_form,
		'profile_form': profile_form
		})