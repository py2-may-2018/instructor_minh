from django.conf.urls import url, include
from django.contrib import admin
import views
urlpatterns = [
    #/
    url(r'^$', views.index),
    #/users
    url(r'^users$', views.users),
    #/users/1
    url(r'^users/create$', views.create),
    url(r'^users/(?P<user_first_name>\w+)$', views.show),
]