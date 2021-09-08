from .models import Event
from django.utils import timezone

def next_events(request):
	events = Event.objects.filter(
		start_date__gte=timezone.now()).order_by('start_date')[:5]
	return {'events': events}