from django.core.checks import templates
from django.urls import path

from calories_counter import views

urlpatterns = [
    path('', views.all_people)
]
