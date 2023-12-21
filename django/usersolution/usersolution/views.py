from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import User

curl = settings.CURRENT_URL

def index(request):
    return render(request,"index.html",{})

def About(request):
    return render(request,"about.html",{"curl":curl})

def Services(request):
    return render(request,"service.html",{"curl":curl})

def WhyUs(request):
    return render(request,"why.html",{"curl":curl})

def Team(request):
    return render(request,"team.html",{"curl":curl})

def Login(request):
    return render(request,"login.html",{"curl":curl})

def reg(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Email = request.POST["Email"]
        Father_name = request.POST["Father_name"]
        Mobile_No = request.POST["Mobile_No"]
        City =  request.POST["City"]
        print(Name,Email,Father_name,Mobile_No,City)
        userOBj = User(Name=Name,Email=Email,Father_name=Father_name,Mobile_No=Mobile_No,City=City)
    return render(request,"registration.html",{"curl":curl})
