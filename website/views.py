from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

# Create your views here.

@login_required
def halaman1(request):
    return render(request,'halaman1.html')

@login_required
def gbk(request):
    return render(request,'gbk.html')

def login_view(request):

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'login.html', {"form": form})

def sign_up(request):
    return render(request,'sign_up.html')

def logout_view(request):
    logout(request)
    return redirect('/login')