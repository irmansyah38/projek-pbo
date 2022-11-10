
from django.shortcuts import render

# Create your views here.

def halaman1(request):
    return render(request,'depan.html')

def login(request):
    return render(request,'login.html')

def gbk(request):
    return render(request,'gbk.html')

def sign_up(request):
    return render(request,'sign_up.html')

# def login(request):
   
   