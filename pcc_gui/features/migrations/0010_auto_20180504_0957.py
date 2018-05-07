# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0009_auto_20180502_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dependent',
            name='feature',
        ),
        migrations.AlterField(
            model_name='feature',
            name='processed',
            field=models.NullBooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Dependent',
        ),
    ]