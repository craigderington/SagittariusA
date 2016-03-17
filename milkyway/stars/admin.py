from django.contrib import admin
from .models import Galaxy, Constellation, Star, StellarObject

# Register your models here.

class GalaxyAdmin(admin.ModelAdmin):
    fields = ('galaxy_name', 'constellation', 'distance', 'notes')
    list_display = ('galaxy_name', 'constellation', 'distance')
    list_filter = ('galaxy_name', 'constellation', 'distance')
    search_fields = ['galaxy_name', 'constellation']


class ConstellationAdmin(admin.ModelAdmin):
    fields = ('constellation_name', 'iau_abbr', 'other_abbr', 'genitive', 'family',
              'origin', 'meaning', 'brightest_star')
    list_display = ('constellation_name', 'family', 'iau_abbr', 'origin', 'brightest_star')
    list_filter = ('constellation_name', 'origin', 'brightest_star')
    search_fields = ['constellation_name', 'brightest_star']


class StarAdmin(admin.ModelAdmin):
    fields = ('proper_name', 'distance', 'spectral_class', 'magnitude', 'bayer_designation', 'constellation_name', 'evolution_stage')
    list_display = ('proper_name', 'magnitude', 'distance', 'spectral_class', 'evolution_stage')
    list_filter = ('proper_name', 'magnitude')
    search_fields = ['proper_name', 'spectral_class']


class StellarObjectAdmin(admin.ModelAdmin):
    fields = ('name', 'constellation', 'stellar_object_type', 'distance')
    list_display = ('name', 'stellar_object_type', 'constellation', 'distance')
    list_filter = ('name', 'constellation', 'stellar_object_type')
    search_fields = ['name']

admin.site.register(Galaxy, GalaxyAdmin)
admin.site.register(Constellation, ConstellationAdmin)
admin.site.register(Star, StarAdmin)
admin.site.register(StellarObject, StellarObjectAdmin)
