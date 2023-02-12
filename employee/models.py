from django.db import models

# Create your models here.
class Emp_data(models.Model):
    fname= models.CharField(max_length=30)
    lname= models.CharField(max_length=30)
    email= models.CharField(max_length=40)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact= models.IntegerField()
    dob = models.DateField(verbose_name='Date of Birth')
    address =models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.fname
    def __str__(self):
        return self.contact
    

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to="testimonial")
    rating=models.IntegerField(max_length=1)

    def __str__(self):
        return self.testimonial
