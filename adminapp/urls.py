from django.urls import path
from . import views
#for file uploading .......................
from django.conf.urls.static import static
from django.conf import settings
#.....................................
urlpatterns = [
path('', views.index),
path('adminhome/',views.adminhome),
path('manageusers/',views.manageusers),
path('manageuserstatus/',views.manageuserstatus),
path('deleteuser/',views.deleteuser),
path('editprofile/',views.editprofile),
path('record/',views.getsinglerecord),
path('changepassword/',views.changepassword),
path('addcategory/',views.addcategory),
path('viewcategory/',views.viewcategory),
path('logout/',views.Logout),
# django-rest-framework
# path('user_api/users/',views.userlist),
# path('user_api/user/<int:userid>/',views.user),
# path('user_api/deleteuser/<int:userid>/',views.deleteuser),
# path('user_api/createuser/',views.createuser),
# path('user_api/updateuser/<int:userid>/',views.updateuser)
]