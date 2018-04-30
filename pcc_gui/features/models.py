# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feature(models.Model):
    group_name = models.CharField(max_length=100, blank=True)                # FMM page
    function_name = models.CharField(max_length=100, blank=True)             # FMM major function group
    feature_name = models.CharField(max_length=50, blank=True)               # FMM feature name
    selection_name = models.CharField(max_length=100, blank=True)            # FMM keyword selection
    choice_type = models.CharField(max_length=15, blank=True)                # FMM valid values are 'selection' or 'option'
    option_min = models.IntegerField(blank=True, null=True)                  # FMM range of options minimum
    option_max = models.IntegerField(blank=True, null=True)                  # FMM range of options maximum
    processed = models.NullBooleanField()                   # FMM.txt row was processed = True; else created from dependency

class Dependency(models.Model):
    feature = models.ForeignKey(Feature)                # list of features that the related feature depends upon

class Dependent(models.Model):
    feature = models.ForeignKey(Feature)                # list of features that are dependent upon the related

