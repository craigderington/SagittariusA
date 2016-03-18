from django.contrib import admin
from .models import Star

# Register your models here.


class StarAdmin(admin.ModelAdmin):
    fields = ('proper_name', 'distance', 'spectral_class', 'magnitude',
              'bayer_designation', 'evolution_stage', 'constellation_name',)
    list_display = ('proper_name', 'constellation_name', 'magnitude', 'distance',
                    'spectral_class', 'evolution_stage')
    list_filter = ('proper_name', 'constellation_name', 'magnitude')
    search_fields = ['proper_name', 'spectral_class']



#register model in django admin
admin.site.register(Star, StarAdmin)
