from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('simple_view', views.simple_view),
]
