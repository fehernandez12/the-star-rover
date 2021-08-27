from django.shortcuts import render
from events.models import Event
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
	return render(request, 'home/home.html', {'section': 'dashboard'})