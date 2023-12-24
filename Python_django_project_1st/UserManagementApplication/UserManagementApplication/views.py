from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .forms import UserLogin
from .models import User
curl = settings.CURRENT_URL

def index(request):
    return render(request,"MasterIndex.html",{})

def about(request):
    return render(request,"About.html",{"curl":curl})

def contact(request):
    return render(request,"Contact.html",{"curl":curl})

def forgetpassword(request):
     return render(request,"ForgetPassword.html",{"curl":curl})

def newpassword(request):
     return render(request,"NewPassword.html",{"curl":curl})

def login(request):
    if request.method == "POST":
        fm = UserLogin(request.POST)  
        if fm.is_valid():
           print("Form Validated")
           print("Email:",fm.cleaned_data['email'])
           print("Password:",fm.cleaned_data['password'])
           email=fm.cleaned_data['email']
           password=fm.cleaned_data['password']
        else:
           fm = UserLogin()
           print("Form Not Validated")
        return render(request,'Login.html',{'form':fm})  
    elif request.method == "GET":
        return render(request,'Login.html',{"curl":curl})  

#def login(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]
#         print(email)
#         print(password)
#         context = {"email":email,"password":password}
#         return render(request,"Login.html",{"curl":curl,"details":context})
#     elif request.method == "GET":
#         return render(request,"Login.html",{"curl":curl})

        
def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        mobile = request.POST["mobile"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        dob = request.POST["dob"]
        print(name,email,password,mobile,gender,address,dob)
        userObj = User(name=name,email=email,password=password,mobile=mobile,gender=gender,address=address,dob=dob)
        msg=""
        try:
            userObj.save()
            msg="User Register Successfully"
        except:
            msg="User Not Register"    
        return render(request,"Register.html",{"curl":curl,"msg":msg})
    else:
        return render(request,"Register.html",{"curl":curl})
    
