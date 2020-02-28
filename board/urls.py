from django.contrib import admin
from django.urls import path, include, re_path
from board import views

urlpatterns = [
    re_path(r'^(?P<pk>\w+)/$', views.details),
    path('create', views.create_msg),
]
