from django.contrib import admin
from .models import Event, Parade

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'start_date', 'end_date']
	prepopulated_fields = {'slug': ('name',)}