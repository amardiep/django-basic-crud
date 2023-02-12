from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    age = models.IntegerField()
    isActive = models.BooleanField(default=False)
    address= models.CharField(max_length=300)
    company=models.CharField(max_length=100)