# galaxies/models.py

from django.db import models
from milkyway.models import TimeStampedModel

# Create your models here.
class Galaxy(TimeStampedModel):
    galaxy_name = models.CharField(max_length=50, null=False, blank=False)
    galaxy_type = models.CharField(max_length=50, null=True, blank=True)
    constellation = models.ForeignKey('constellations.Constellation', null=True, blank=True)
    notes = models.TextField(default=None)
    distance = models.DecimalField(max_digits=6, decimal_places=3, null=False, blank=False)
    diameter = models.PositiveIntegerField(default=0, null=True, blank=True)
    number_of_stars = models.PositiveIntegerField(default=0, null=True, blank=True)
    galaxy_mass = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        verbose_name = 'Galaxy'
        verbose_name_plural = 'Galaxies'
        ordering = ['id']

    def __str__(self):
        return self.galaxy_name
