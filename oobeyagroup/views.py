import os
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "oobeyagroup/index.html")

def agileandscrum(request):
    return render(request, "oobeyagroup/agileandscrum.html")    

def technologyleadership(request):
    return render(request, "oobeyagroup/technologyleadership.html")    

def productmanagement(request):
    return render(request, "oobeyagroup/productmanagement.html")    

def softwaredevelopment(request):
    return render(request, "oobeyagroup/softwaredevelopment.html")    

