from django.contrib import admin
from django.urls import path
from website.views import halaman1 , gbk ,login_view ,sign_up, logout_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', halaman1,name='halaman1'),
    path('gbk/', gbk,name='gbk'),
    path('login/', login_view,name='login'),
    path('logout/', logout_view,name='logout'),
    path('sign_up/', sign_up,name='sign_up'),
]
