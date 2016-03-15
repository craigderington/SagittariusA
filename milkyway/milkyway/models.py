#config/models.py
from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class that provides self-updating
    'created' and 'modified' fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        app_label = 'stars'


class ModelFormFailureHistory(models.Model):
    form_data = models.TextField()
    model_data = models.TextField()

    class Meta:
        app_label = 'stars'
