#constellations/admin.py

from django.contrib import admin
from .models import Constellation

# Register your models here.

class ConstellationAdmin(admin.ModelAdmin):
    fields = ('constellation_name', 'iau_abbr', 'other_abbr', 'genitive',
              'family', 'origin', 'meaning', 'brightest_star', 'right_ascension',
              'declination', 'number_of_stars', 'stars_with_planets',)
    list_display = ('constellation_name', 'family', 'iau_abbr', 'origin',
                    'brightest_star', 'number_of_stars')
    list_filter = ('constellation_name', 'origin',)
    search_fields = ['constellation_name', 'brightest_star',]


#register model in django admin
admin.site.register(Constellation, ConstellationAdmin)
