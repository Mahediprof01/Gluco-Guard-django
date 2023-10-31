from django.contrib import admin
from django.urls import path, include
from appone import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('result/',views.result)
]

