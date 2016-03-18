# constellations/models.py

from django.db import models
from milkyway.models import TimeStampedModel

# Create your models here.
class Constellation(TimeStampedModel):
    constellation_name = models.CharField(max_length=50, blank=False, null=False)
    iau_abbr = models.CharField(max_length=20, null=False, blank=False)
    other_abbr = models.CharField(max_length=20, null=False, blank=False)
    genitive = models.CharField(max_length=50, null=True, blank=True)
    family = models.CharField(max_length=50, null=True, blank=True)
    origin = models.CharField(max_length=50, null=True, blank=True)
    meaning = models.CharField(max_length=50, null=True, blank=True)
    brightest_star = models.ForeignKey('stars.Star', null=True, blank=True)
    right_ascension = models.CharField(default=None, null=True, blank=True,
                                       max_length=50)
    declination = models.CharField(default=None, null=True, blank=True,
                                   max_length=50)
    number_of_stars = models.PositiveIntegerField(default=0, null=True, blank=True)
    stars_with_planets = models.PositiveIntegerField(default=0, null=True, blank=True)


    class Meta:
        verbose_name = 'Constellation'
        verbose_name_plural = 'Constellations'
        ordering = ['id']

    def __str__(self):
        return self.constellation_name
