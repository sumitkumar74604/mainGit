from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

curl = settings.CURRENT_URL


def index(request):
    return render(request,"MasterIndex.html",{})

def about(request):
    return render(request,"about.html",{"curl":curl})

def login(request):
     return render(request,"login.html",{"curl":curl})

def pricing(request):
     return render(request,"pricing.html",{"curl":curl})
def feature(request):
    return render(request,"Feature.html",{"curl":curl})

def signup(request):
    return render(request,"Signup.html",{"curl":curl})


def service(request):
    return render(request,"Service.html",{"curl":curl})

def ourteam(request):
    return render(request,"OurTeam.html",{"curl":curl})

def ourquoet(request):
    return render(request,"OurQuoet.html",{"curl":curl})