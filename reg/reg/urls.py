from django.contrib import admin
from django.urls import path
from appone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('home/result',views.result),
    path('logout/',views.LogoutPage,name='logout'),
]
