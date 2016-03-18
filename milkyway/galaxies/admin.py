#galaxies/admin.py

from django.contrib import admin
from .models import Galaxy

# Register your models here.

class GalaxyAdmin(admin.ModelAdmin):
    fields = ('galaxy_name', 'distance', 'notes', 'constellation',)
    list_display = ('galaxy_name', 'distance', 'constellation',)
    list_filter = ('galaxy_name', 'distance')
    search_fields = ['galaxy_name', 'constellation',]


#register model in django admin
admin.site.register(Galaxy, GalaxyAdmin)
