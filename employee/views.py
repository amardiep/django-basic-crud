from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp_data,Testimonial
from .forms import FeedbackForm, EmpForm
# Create your views here.
def employee_home(request):
    emps=Emp_data.objects.all()
    return render(request, "employee/home.html",{
        'emps':emps
    })


def add_employee(request):
    if request.method =="POST":
        print("Data Post Ho raha hai bhaisahab... Congradulations")

        #fetch data
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        contact = request.POST.get("contact")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        working = request.POST.get("working")
        department = request.POST.get("department")

        #create model oject and set the data
        data = Emp_data()
        data.fname = fname
        data.lname = lname
        data.email = email
        data.gender = gender
        data.contact = contact
        data.dob = dob
        data.address = address
        data.working = working
        if working is None:
            data.working= False
        else:
            data.working = True
        data.department = department

        #save the data
        data.save()

        #prepare message



        
        return redirect(to="/employee/home/")
    form = EmpForm
    return render(request,"employee/add-employee.html",{'form':form})


def delete_employee(request,employee_id):
    emp=Emp_data.objects.get(pk=employee_id)
    emp.delete()
    return redirect("/employee/home")


def update_employee(request,employee_id):
    emp= Emp_data.objects.get(pk=employee_id)
    return render(request,"employee/update-employee.html",{
        'emp':emp
    })
def do_update(request,employee_id):
    if request.method=="POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        contact = request.POST.get("contact")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        working = request.POST.get("working")
        department = request.POST.get("department")

        data= Emp_data.objects.get(pk=employee_id)

        data = Emp_data()
        data.fname = fname
        data.lname = lname
        data.email = email
        data.gender = gender
        data.contact = contact
        data.dob = dob
        data.address = address
        data.working = working
        if working is None:
            data.working= False
        else:
            data.working = True
        data.department = department


        data.save()
    return redirect("/employee/home/")

def testimonials(request):
    test= Testimonial.objects.all()
    return render(request,"employee/testimonials.html",{
        'test':test
    })

def feedback(request):
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("The feedback is submitted")
        else:
            return render (request, "employee/feedback.html",{
                'form':form
            })
    else:
        form = FeedbackForm()

    return render(request,"employee/feedback.html",{
        'form':form
    })

if __name__ == "__main__":
    add_employee.run(debug=True)