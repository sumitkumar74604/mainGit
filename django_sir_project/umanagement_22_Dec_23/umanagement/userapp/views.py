from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to User App</h1>")

def userhome(request):
    return HttpResponse("<h1>Welcome to User Home Page</h1>")

