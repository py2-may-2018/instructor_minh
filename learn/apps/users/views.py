# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
    return render(request, "users/index.html")

def users(request):
    if "users" not in request.session:
        request.session["users"] = []
    print request.session["users"]
    context = {
        "users": User.objects.all()
    }
    return render(request, "users/users.html", context)


def show(request, user_first_name):
    for user in request.session["users"]:
        if user["first_name"] == user_first_name:
            current_user = user
    context = {
        "name":current_user["first_name"],
         "users":request.session["users"]
    }
    return render(request, "users/users.html", context)

def create(request):
    if "users" not in request.session:
        request.session["users"] = []
    if request.method == "POST":
        User.objects.create(
            first_name=request.POST["first_name"], 
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            password=request.POST["password"]
        )
    return redirect("/users")