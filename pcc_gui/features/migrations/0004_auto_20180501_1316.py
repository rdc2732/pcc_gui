# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20180430_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependency',
            name='dependency_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='dependent',
            name='dependent_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]