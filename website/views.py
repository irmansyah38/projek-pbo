from django.shortcuts import render


# Create your views here.

def halaman1(request):
    return render(request,'halaman1.html')

def gbk(request):
    return render(request,'gbk.html')

def login(request):
    context = {

    }
    if request.method == 'POST':
        context['user_name'] = str(request.POST['user_name'])
        context['password'] = str(request.POST['password'])

    return render(request,'login.html',context)

def sign_up(request):
    return render(request,'sign_up.html')