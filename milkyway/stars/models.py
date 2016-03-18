from __future__ import unicode_literals
from django.db import models
from milkyway.models import TimeStampedModel
from constellations.models import Constellation

# Create your models here.

class Star(TimeStampedModel):
    magnitude = models.DecimalField(max_digits=8, decimal_places=3)
    bayer_designation = models.CharField(max_length=50, null=False, blank=False)
    proper_name = models.CharField(max_length=50, null=False, blank=False)
    distance = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=False)
    spectral_class = models.CharField(max_length=50, null=False, blank=False)
    constellation_name = models.ForeignKey('constellations.Constellation', null=True, blank=True)
    evolution_stage = models.CharField(max_length=50, null=True, blank=True)
    star_mass = models.CharField(max_length=50, default=None, null=True, blank=True)
    star_age = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    surface_temperature = models.CharField(max_length=50, null=True, blank=True)
    visual_brightness = models.IntegerField(default=None, null=True, blank=True)
    star_volume = models.CharField(max_length=50, default=None, null=True, blank=True)


    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'
        ordering = ['id']

    def __str__(self):
        return self.proper_name
