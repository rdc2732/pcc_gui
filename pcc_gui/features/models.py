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
    enabled = models.NullBooleanField(default=False)                         # FMM.txt row was processed = True; else created from dependency
    selected = models.NullBooleanField(default=False)                        # FMM.txt row was processed = True; else created from dependency


    def __str__(self):
        return self.selection_name

class Dependency(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)                # list of features that the related feature depends upon
    name = models.CharField(max_length=51, blank=True)

    def __str__(self):
        return self.name


