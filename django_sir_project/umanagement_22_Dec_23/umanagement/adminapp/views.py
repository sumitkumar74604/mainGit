from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to AdminApp!!</h1>")

def adminhome(request):
    return HttpResponse("<h1>Welcome to Admin Home Page</h1>")