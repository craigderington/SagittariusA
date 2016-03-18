# stellar_objects/admin.py

from django.contrib import admin
from .models import StellarObject

# Register your models here.

class StellarObjectAdmin(admin.ModelAdmin):
    fields = ('name', 'constellation', 'stellar_object_type', 'distance')
    list_display = ('name', 'stellar_object_type', 'constellation', 'distance')
    list_filter = ('name', 'stellar_object_type')
    search_fields = ['name', 'constellation',]


#register model in django admin
admin.site.register(StellarObject, StellarObjectAdmin)
