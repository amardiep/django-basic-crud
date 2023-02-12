from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
   path("home/",employee_home),
   path("add-employee/",add_employee),
   path("delete-employee/<int:employee_id>",delete_employee),
   path("update-employee/<int:employee_id>",update_employee),
   path("do-update/<int:employee_id>",do_update),
   path("testimonials/",testimonials),
   path("feedback/",feedback)

]