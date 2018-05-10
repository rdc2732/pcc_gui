# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader

from .models import Group, Function, Feature, Dependency

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the feature2 index.")

def loadfmm(request):
    fmm = open('FMM.txt', 'r')
    line_count = 0
    Group.objects.all().delete() # Scrub the database before processing FMM.txt

    for line in fmm:
        line_data = line.rstrip().split(',')

        group_name = line_data[0]
        function_name = line_data[1]
        feature_name = line_data[2]
        selection_name = line_data[3]
        dependencies = line_data[4].split(";")
        choice_type = line_data[5]
        option_min = line_data[6]
        option_max = line_data[7]

        groups = Group.objects.filter(name=group_name)  # Add Group if it does not exist
        if groups.count() == 0:
            group = Group(name=group_name)
            group.save()
        group = Group.objects.get(name=group_name)

        functions = Function.objects.filter(name=function_name)  # Add Function if it does not exist
        if functions.count() == 0:
            function = group.function_set.create(name=function_name)
            function.save()
        function = Function.objects.get(name=function_name)

        features = Feature.objects.filter(name=feature_name)  # Add Feature if it does not exist
        if features.count() == 0:
            feature = function.feature_set.create(name=feature_name)
            feature.selection_name=selection_name
            feature.choice_type=choice_type
            feature.option_min=option_min
            feature.option_max=option_max
            feature.save()
        feature = Feature.objects.get(name=feature_name)

        for dependency in dependencies:
            if dependency != "n/a":
                feature.dependency_set.create(name=dependency)
        feature.save()

        line_count += 1

    response_text = "FMM.txt load complete. " + str(line_count) + " records Processed. "
    return HttpResponse(response_text)


def group_view2(request):
    group_list = Group.objects.select_related()

    template = loader.get_template('feature2/group_list.html')
    context = {
        'group_list': group_list,
    }
    return HttpResponse(template.render(context, request))
