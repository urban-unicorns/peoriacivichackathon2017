# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoria', '0006_auto_20170812_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='filename',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('PV', 'Pavement'), ('BK', 'Bike'), ('TC', 'Trashcans'), ('RA', 'Ramps'), ('SW', 'Sidewalks')], max_length=100),
        ),
    ]