from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpRequest("Hello this is a view inside my_app")