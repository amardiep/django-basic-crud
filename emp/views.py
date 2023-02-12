from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    if request.method == "POST":
        check= request.POST['check']
        print(check)

    name='AmarDiep Mankoskar'
    time= datetime.datetime.now()
    isActive=True
    li = ['WAP to check even or odd',
            'WAP to check prime number',
            'WAP to print all prime number from 1 to 100',
            'WAP to print pascals tringals']
    
    student= {"st_name":"Rahul Pagar",
              "st_address":"Nashik",
              "st_phone_number":"+918888888888"}
    
    data = { 
        "isActive":isActive,
        "time":time,
        "name":name,
        "li":li,
        "student_data":student}
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse('Welcome to our website and Please free to contact with us on following email')
    return render(request,"about.html",{})


def services(request):
    #return HttpResponse('Welcome to our services')
    return render(request,"services.html",{})