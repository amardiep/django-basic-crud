from django.contrib import admin
from django.urls import path, include
from Database.views import worker,addworker

urlpatterns = [
    path("home/",addworker),
    path("add_worker/",addworker)
]