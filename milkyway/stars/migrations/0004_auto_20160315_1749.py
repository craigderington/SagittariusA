# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0003_auto_20160315_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='distance',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]
