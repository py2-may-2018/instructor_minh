from django.conf.urls import url
import views
urlpatterns = [
    #/
    url(r'^$', views.index),
    #/hello_world
    url(r'^hello_world$', views.hello_world),
]