from django.contrib import admin
from .models import Emp_data, Testimonial
# Register your models here.

class Emp_dataAdmin(admin.ModelAdmin):
    list_display=('fname','lname','working','gender','contact')
    search_fields=('fname','contact',)


admin.site.register(Emp_data,Emp_dataAdmin)
admin.site.register(Testimonial)