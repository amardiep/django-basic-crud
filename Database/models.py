from django.db import models

# Create your models here.
class addworker(models.Model):
    wid=models.IntegerField(6)
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=200,default='amardiep@xyz.com')
    phone= models.IntegerField(12)
    sex= models.CharField(max_length=2)
    city= models.CharField(max_length=30)
    department= models.CharField(max_length=30)