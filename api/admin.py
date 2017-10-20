from django.contrib import admin
from api import models

#custom admin class
class PlanetAdmin(admin.ModelAdmin):
	list_display = ['name', 'population', 'surface_water','has_enough_water']
	list_filter = ['gravity']
	#specify what fields are editable
	fields = ['name', 'population']
	#'calculated field'
	def has_enough_water(self, obj):
		water = obj.surface_water
		if not water.isdigit():
		    return False
		return int(water) > 10
	has_enough_water.short_description = 'Habitable?'
	has_enough_water.boolean = True



# Register your models here.
#custom registaration
admin.site.register(models.Planet, PlanetAdmin)

admin.site.register(models.Vehicle)
admin.site.register(models.People)
admin.site.register(models.Species)
admin.site.register(models.Transport)
admin.site.register(models.Starship)
admin.site.register(models.Film)
