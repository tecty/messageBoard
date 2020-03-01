from django.contrib import admin
from django.urls import path, include, re_path
from board import views

urlpatterns = [
    path("", views.msg_index, name="index"),
    path('<int:pk>/', views.details, name='details'),
    path('page/<int:page>/', views.list_view, name='list'),
]
