
from django.shortcuts import render

# Create your views here.

def halaman1(request):
    return render(request,'depan.html')

def login(request):
    return render(request,'login.html')

# def login(request):
   
   