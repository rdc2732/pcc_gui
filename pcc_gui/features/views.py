# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader

from .models import Feature, Dependency

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the features index.")

def loadfmm(request):
    fmm = open('FMM.txt', 'r')
    line_count = 0
    Feature.objects.all().delete() # Scrub the database before processing FMM.txt

    for line in fmm:
        line_data = line.rstrip().split(',')

        f_name = line_data[3]   # Get fm_select name from line
        f = Feature.objects.filter(selection_name=f_name) # Add fm_select as Feature if it does not exist
        if f.count() == 0:
            f = Feature(
                selection_name=f_name, \
                group_name=line_data[0], \
                function_name=line_data[1], \
                feature_name=line_data[2], \
                choice_type=line_data[5], \
                option_min=line_data[6], \
                option_max=line_data[7], \
                )
            f.save()

        for parent in line_data[4].split(";"):  # Process feature model dependencies.
            if parent != "n/a":
                p = f.dependency_set.create(name=parent)
                p.save()

        line_count += 1

    response_text = "FMM.txt load complete. " + str(line_count) + " records Processed. "
    return HttpResponse(response_text)

class FeatureListView(generic.ListView):
    model = Feature


def group_view(request):
    group_list = []
    for g in Feature.objects.values('group_name').distinct():
        group_list.append(g.values()[0])
    print group_list
    template = loader.get_template('features/group_list.html')
    context = {
        'group_list': group_list,
    }
    return HttpResponse(template.render(context, request))

