# stellar_objects/models.py

from django.db import models
from milkyway.models import TimeStampedModel

# Create your models here.
class StellarObject(TimeStampedModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    constellation = models.ForeignKey('constellations.Constellation', null=True,
                                      blank=True, default=None)
    stellar_object_type = models.CharField(max_length=50, null=False, blank=False,
                                           default='Quasar')
    distance = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Stellar Object'
        verbose_name_plural = 'Stellar Objects'
        ordering = ['id']

    def __str__(self):
        return self.name
