# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
    context = {
        "users":User.objects.all()#list of users
    }
    return render(request, "users/index.html", context)

def create(request):
    if request.method == "POST":
        User.objects.create(email=request.POST["email"], password=request.POST["password"])
    return redirect("/")