from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import addworker

# # Create your views here.
def worker():
    print("bhava mi ith alav")  
    return render("worker/home.html",{})

def addworker(request):
        print(request)
        print("ith hav")  
        if request.method =="POST" :

            #fetch data
            worker_wid = request.POST.get("worker_wid")
            worker_name = request.POST.get("worker_name")
            worker_email = request.POST.get("worker_email")
            worker_phone = request.POST.get("worker_phone")
            worker_sex = request.POST.get("worker_sex")
            worker_city = request.POST.get("worker_address")
            worker_department = request.POST.get("worker_department")

            #create model oject and set the data
            d = addworker()
            d.wid= worker_wid,
            d.name= worker_name,
            d.email = worker_email,
            d.phone = worker_phone,
            d.sex = worker_sex,
            d.city = worker_city,
            d.department = worker_department

            #save the data
            d.save()

            # #prepare message
        

            return redirect("worker/home")
        return render(request, "worker/add_worker.html",{})