from __future__ import unicode_literals
from django.db import models
from milkyway.models import TimeStampedModel

# Create your models here.


class Galaxy(TimeStampedModel):
    galaxy_name = models.CharField(max_length=50, null=False, blank=False)
    constellation = models.ForeignKey('Constellation')
    notes = models.TextField(default=None)
    distance = models.DecimalField(max_digits=6, decimal_places=3, null=False, blank=False)

    class Meta:
        verbose_name = 'Galaxy'
        verbose_name_plural = 'Galaxies'
        ordering = ['id']

    def __str__(self):
        return self.galaxy_name


class Constellation(TimeStampedModel):
    constellation_name = models.CharField(max_length=50, blank=False, null=False)
    iau_abbr = models.CharField(max_length=20, null=False, blank=False)
    other_abbr = models.CharField(max_length=20, null=False, blank=False)
    genitive = models.CharField(max_length=50, null=True, blank=True)
    family = models.CharField(max_length=50, null=True, blank=True)
    origin = models.CharField(max_length=50, null=True, blank=True)
    meaning = models.CharField(max_length=50, null=True, blank=True)
    brightest_star = models.ForeignKey('Star', null=True, blank=True)

    class Meta:
        verbose_name = 'Constellation'
        verbose_name_plural = 'Constellations'
        ordering = ['id']

    def __str__(self):
        return self.constellation_name


class Star(TimeStampedModel):
    magnitude = models.DecimalField(max_digits=8, decimal_places=3)
    bayer_designation = models.CharField(max_length=50, null=False, blank=False)
    proper_name = models.CharField(max_length=50, null=False, blank=False)
    distance = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=False)
    spectral_class = models.CharField(max_length=50, null=False, blank=False)
    constellation_name = models.ForeignKey('Constellation', null=True, blank=True)
    evolution_stage = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'
        ordering = ['id']

    def __str__(self):
        return self.proper_name


class StellarObject(TimeStampedModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    constellation = models.ForeignKey('Constellation')
    stellar_object_type = models.CharField(max_length=50, null=False, blank=False,
                                           default='Quasar')
    distance = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Stellar Object'
        verbose_name_plural = 'Stellar Objects'
        ordering = ['id']

    def __str__(self):
        return self.name
