from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login$', views.login, name="login"),
    url(r'^pinfo$', views.pinfo, name="personal_info"),
    url(r'^index$', views.index, name="index"),
    url(r'^$', views.index, name="index")
]
