from django.shortcuts import render
from events.models import Event
from django.utils import timezone

# Create your views here.
def index_view(request):
	events = Event.objects.filter(
		start_date__gte=timezone.now()).order_by('start_date')
	return render(request, 'home/index.html', {'events': events})