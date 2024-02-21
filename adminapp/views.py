from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from umanagement import settings
from umanagement import models
from django.db.models.expressions import RawSQL

#for file uploading
from django.core.files.storage import FileSystemStorage

#for logout
from django.contrib.auth import logout


#for display image
from django.conf import settings
media_url=settings.MEDIA_URL

# Create your views here.
curl = settings.CURRENT_URL
import time
import datetime

#django rest framework
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
#from.serializers import UserSerializer


def sessioncheckadmin_middleware(get_response):
    def middleware(request):
        print("============= request=====:",request.path)
        strpath = request.path
        list1 = strpath.split("/")
        if len(list1)>2:
           strnewpath = "/"+list1[1]+"/"+list1[2]+"/"
           if strnewpath=='/adminhome/' or strnewpath=='/adminapp/manageusers/' or strnewpath=='/adminapp/addcategory/'  or strnewpath=='/adminapp/viewcategory/' or strnewpath=='/adminapp/changepassword/':
              if 'emailid' not in request.session:            
            # if request.session["emailid"]==None or request.session["role"]!="admin":
            #    print("EmailId:",request.session["emailid"])
                  response=redirect('http://13.215.47.16:8002/login')
                  return response
              else:
                  response=get_response(request) 
                  return response
           else:
               response=get_response(request)
               return response
        else:
            print("else part =============")
            return get_response(request)
    return middleware 

def index(request):
    return HttpResponse("<h1>Welcome to AdminApp!!</h1>")

def adminhome(request):
    # return HttpResponse("<h1>Welcome to Admin Home Page</h1>")
    emailid=request.session.get("emailid")
    role=request.session.get("role") 
    data = models.User.objects.filter(email=emailid,role=role).values()
    print(data)
    return render(request,'Admin.html',{'curl':curl,'details':data})

def manageusers(request):
    dic = models.User.objects.values('userid','name','email','mobile','address','gender','dob','status')
    return render(request,'ManageUsers.html',{'curl':curl,'context':dic})

def manageuserstatus(request):
    if request.method=="GET":
        id=request.GET.get('userid')
        status=request.GET.get('status')
        print(id,status)
        if status == "block":
           models.User.objects.filter(userid=id).update(status=1)
        elif status == "verify":
           models.User.objects.filter(userid=id).update(status=0)
        return redirect(curl+"adminapp/manageusers/")     

def deleteuser(request):
    if request.method == "GET":
       gId = request.GET.get("userid") 
       print("get id:",gId)
       obj=models.User.objects.get(userid=gId)
       print(obj)
       obj.delete()
    return redirect(curl+"adminapp/manageusers/") 

def getsinglerecord(request):
    print("<===========getsinglerecord=========>")
    if request.method == "GET":
       gId = request.GET.get("userid") 
       print("get id:",gId)
       dic=models.User.objects.values('userid','name','email','mobile','address','gender','dob','status').get(userid=gId)   
       t = dic["dob"]
       r=t.strftime('%Y-%m-%d')
       print(dic,r)
    # return redirect(curl+"adminapp/manageusers/",{'curl':curl,'single':dic})   
    return render(request,'Modal.html',{'curl':curl,'context':dic,"dob":r})
   
def editprofile(request):
    print("<===========editprofile=========>")
    if request.method == "POST":
       print("=====POST Method")
       id=request.POST.get('userid') 
       name=request.POST.get('name') 
       mobile=request.POST.get('mobile') 
       gender=request.POST.get('gender') 
       address=request.POST.get('address') 
       dob=request.POST.get('dob') 
       print(id,name,mobile,gender,address,dob)
       #models.User.objects.get(userid=id).update()
       models.User.objects.filter(userid=id).update(name=name,mobile=mobile,gender=gender,address=address,dob=dob)
       
    return redirect(curl+"adminapp/manageusers/")

def changepassword(request):
    msg=""
    emailid=request.session.get("emailid")
    role=request.session.get("role") 
    if request.method == "POST":
        oldpass=request.POST.get('oldpass') 
        newpass=request.POST.get('newpass') 
        confirmpass=request.POST.get('confirmpass')
        list1 = models.User.objects.filter(role="admin",password=oldpass).values()
        # print(list1[0])
        if len(list1)>0:
            if newpass == confirmpass:
                models.User.objects.filter(role="admin").update(password=newpass)
                msg="Password Changed Successfully"
            else:
                msg="New Password and Confirm Password mismatch"    
        else:
            msg="Please enter correct old password" 
        return render(request,'ChangePassword.html',{'curl':curl,'msg':msg,'emailId':emailid,'role':role})     
    elif request.method == "GET":
        return render(request,'ChangePassword.html',{'curl':curl,'msg':msg,'emailId':emailid,'role':role})
        
def addcategory(request):
    msg=""
    dic = models.User.objects.values('userid','name','email')
    if request.method == "POST":
        catname=request.POST.get('catname') 
        #for file uploading .............................
        caticon=request.FILES['caticon']
        #print(catname,caticon)
        fs=FileSystemStorage()
        fs.save(caticon.name,caticon)  
        #....................................................
        userid=request.POST.get('userid') 
        print(catname,caticon,userid)
        obj = models.AddCategory(userid_id=userid,catname=catname,caticon=caticon)
        try:
            obj.save()
            msg="Category Added Successfully!!"
        except:
            msg="Category Not Added!!"

    return render(request,'AddCategory.html',{'curl':curl,'context':dic,'msg':msg})

def viewcategory(request):
    if request.method == "GET":
        s='''SELECT a.userid,a.name,b.userid_id,b.catid,b.catname,b.caticon FROM umanagement_user as a LEFT JOIN umanagement_addcategory as b on b.userid_id = a.userid'''
        obj=models.User.objects.raw(s)
        print(obj)  
        obj1=models.User.objects.all().values('userid','name')
    return render(request,'ViewCategory.html',{'curl':curl,'context':obj,'context2':obj1,'media_url':media_url})

def Logout(request):
    logout(request)
    return redirect('http://13.215.47.16:8002/login')

#django rest framework
'''
Full form of REST API is Representational State Transfer Application Programming Interface more commonly known as REST API web service. It means when a RESTful API is called, the server will transfer a representation of the requested resource's state to the client system.
'''
@csrf_exempt
def userlist(request):
    if request.method == 'GET':
        users = models.User.objects.all()
        serializer = UserSerializer(users,many=True)
        '''
The safe boolean parameter defaults to True . If it's set to False , any object can be passed for serialization (otherwise only dict instances are allowed).
        '''
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def createuser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = UserSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.errors,
        status=400)

@csrf_exempt
def user(request,userid):
    try:
        user = models.User.objects.get(userid=userid)
    except Exception:
       models.User.DoesNotExist
       return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data) 

@csrf_exempt
def updateuser(request,userid):
    try:
        user = models.User.objects.get(userid=userid)
    except Exception:
       models.User.DoesNotExist
       return HttpResponse(status=404)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def deleteuser(request,userid):
    try:
        user = models.User.objects.get(userid=userid)
    except Exception:
       models.User.DoesNotExist
       return HttpResponse(status=404)
    
    msg=""   
    if request.method == 'DELETE':
        try:
           user.delete()
           msg="User Delete Successfully!!"
        except:
           msg="User Not Deleted"
        return HttpResponse(msg)
 

def viewcategory(request):

    if request.method == "GET":
        userdata = models.User.objects.all().values('userid','name') 
        catdata = models.AddCategory.objects.all().values()
        print(userdata)
        print(catdata)
        print(media_url)
        user_list = []
        
        dic={}
        for index in range(len(userdata)):
            id = userdata[index]["userid"]
            name = userdata[index]["name"]
            # print("============",id,name,"============")
            cat_list = []
            for index in range(len(catdata)):
                userid=catdata[index]["userid_id"]
                if id==userid:
                   cat = catdata[index]
                   cat_list.append(cat)
                   dic=({id:cat_list})
            user_list.append(dic)            
        print("===============================") 
        print(user_list)
        
    return render(request,'ViewCategory.html',{'curl':curl,'context':user_list,'medial_url':media_url})

