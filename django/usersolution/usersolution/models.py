from django.db import models
from django.utils import timezone

class User(models.Model):
    Name=models.CharField(max_length=10)
    Email=models.EmailField(max_length=50,unique=True)
    Father_name=models.CharField(max_length=30)
    Mobile_No=models.IntegerField()
    City=models.CharField(max_length=20)
    status= models.IntegerField(default=0)
    date= models.DateTimeField('date published', default=timezone.now)
    role= models.CharField(default="user",max_length=5)


def __str__(self):
    return"{0},{1},{2},{3},{4}".format(self.Name,self.Email,self.Father_namem,self.Mobile_No,
self.City,self.status,self.date,self.role)
