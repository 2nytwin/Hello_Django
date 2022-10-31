from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.project_index, name="blog_index"),
    path("<int:pk>/",views.project_detail, name="blog_detail"),
]