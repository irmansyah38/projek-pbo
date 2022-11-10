from django.contrib import admin
from django.urls import path
from website.views import halaman1, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('halaman1/', halaman1),
    path('login/', login),
]
