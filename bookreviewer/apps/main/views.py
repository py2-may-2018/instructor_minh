# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    if "active_id" in request.session:
        return HttpResponse("already logged in!")
    return render(request, "main/index.html")

def register(request):
    User.objects.validate(request)
    return redirect("/")

def login(request):
    users = User.objects.filter(email=request.POST["email"])
    if len(users) > 0:
        user = users[0]
        if user.password == request.POST["password"]:
            request.session["active_id"] = user.id 
            return HttpResponse("logged in!")
            #dashboard
    messages.error(request, "Invalid login information")
    return redirect("/")