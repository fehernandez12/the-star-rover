from django.contrib import admin
from .models import ModelAgency, Model, Measurements, Portfolio, Photo

# Register your models here.
@admin.register(Model)
class ModelsAdmin(admin.ModelAdmin):
	list_display = ['id', 'last_name', 'first_name',
		'country', 'active', 'salary']
	list_display_links = ['id']
	list_filter = ['last_name', 'salary']
	list_editable = ['active', 'salary']

@admin.register(ModelAgency)
class AgencyAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'country']
	list_display_links = ['id']
	list_filter = ['name', 'country']

@admin.register(Measurements)
class MeasuresAdmin(admin.ModelAdmin):
	list_display = ['model', 'chest', 'waist', 'hips']
	list_display_links = ['model']
	list_filter = ['model', 'chest', 'waist', 'hips']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
	list_display = ['model']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ['id', 'model_name', 'image']
	list_display_links = ['id']

	@admin.display
	def model_name(self, obj):
		return f'{obj.portfolio.model.first_name} {obj.portfolio.model.last_name}'