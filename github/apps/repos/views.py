# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello_world")

def hello_world(request):
    return render(request, "repos/index.html")