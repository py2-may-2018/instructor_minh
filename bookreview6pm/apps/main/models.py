# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

class UserManager(models.Manager): #all, get, filter, exclude, create
    def validate(self, request):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    valid = False
                    messages.error(request, "{} need to be filled in".format(key))
            if request.POST["confirm password"] != request.POST["password"]:
                valid = False
                messages.error(request, "password must match confirmation password")
            if valid == True:
                #create/send to database
                User.objects.create(name=request.POST["name"], email=request.POST["email"], password=request.POST["password"])
                print User.objects.all()
                messages.success(request, "Created User")

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="has_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
