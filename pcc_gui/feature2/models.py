# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, blank=True)     # FMM page

    def __str__(self):
        return self.name


class Function(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)          # FMM major function group

    def __str__(self):
        return self.name


class Feature(models.Model):
    CHOICE = 'CHO'
    SELECTION = 'SEL'

    RULE_TYPES = (
        (CHOICE, 'choice'),
        (SELECTION, 'selection'),
    )

    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)                              # FMM feature name
    selection_name = models.CharField(max_length=100, blank=True)                   # FMM keyword selection
    rule_type = models.CharField(max_length=15, blank=True, choices=RULE_TYPES)     # FMM rule for selection
    option_min = models.IntegerField(blank=True, null=True)                         # FMM range of options minimum
    option_max = models.IntegerField(blank=True, null=True)                         # FMM range of options maximum
    enabled = models.NullBooleanField(default=False)                                # Feature enabled state
    selected = models.NullBooleanField(default=False)                               # Feature selected state

    def __str__(self):
        return self.name


class Dependency(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)          # FMM required dependency

    def __str__(self):
        return self.name
