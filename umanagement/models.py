from django.db import models
from django.utils import timezone

class User(models.Model):
    userid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField(max_length=10)
    date = models.DateTimeField('date published', default=timezone.now)
    status = models.IntegerField(default=0)
    role = models.CharField(default="user",max_length=10)

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7},{8},{9},{10}".format(self.userid,self.name, self.email, self.password, self.mobile, self.address,self.gender,self.dob,self.date,self.status,self.role)

class AddCategory(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)     
    catid = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=100)
    caticon = models.CharField(max_length=100)

    def __str__(self):
        return "{0}, {1}, {2}, {3}, ".format(self.userid,self.catid,self.catname,self.caticon)
    
