from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .forms import UserLogin
from .models import User
curl = settings.CURRENT_URL

def index(request):
    '''
    render(arg1,arg2,arg3)
    arg1=request,
    arg2=html file,
    arg3={"name":"Rahul Sharma"}
    '''
    context = {"name":"Rahul Sharma","age":23,"address":"Indore M.P","curl":curl}
    return render(request,"MasterIndex.html",context)

def about(request):
    return render(request,"About.html",{"curl":curl})

def contact(request):
    return render(request,"Contact.html",{"curl":curl})

def register(request):
    return render(request,"Register.html",{"curl":curl})


# def login(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]
#         print(email)
#         print(password)
#         context = {"email":email,"password":password}
#         return render(request,"Login.html",{"curl":curl,"details":context})
#     elif request.method == "GET":
#         return render(request,"Login.html",{"curl":curl})

def login(request):
    fm = UserLogin()
    if request.method == "POST":
        fm = UserLogin(request.POST)  
        if fm.is_valid():
           print("Form Validated")
           print("Email:",fm.cleaned_data['email'])
           print("Password:",fm.cleaned_data['password'])
        return render(request,'Login.html',{'form':fm})  
    elif request.method == "GET":
        return render(request,'Login.html',{'form':fm})  
        
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
    
