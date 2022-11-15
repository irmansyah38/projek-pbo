from django.contrib import admin
from django.urls import path
from website.views import halaman1 , gbk ,login ,sign_up

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', halaman1,name='halaman1'),
    path('gbk/', gbk,name='gbk'),
    path('login/', login,name='login'),
    path('sign_up/', sign_up,name='sign_up'),
]
