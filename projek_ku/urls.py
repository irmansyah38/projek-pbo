from django.contrib import admin
from django.urls import path
from website.views import halaman1, login , gbk , sign_up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('halaman1/', halaman1),
    path('login/', login),
    path('gbk/', gbk),
    path('sign_up/', sign_up),
]
