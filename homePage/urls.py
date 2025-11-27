from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage_index, name='homePage_index'),
    path('register', views.register, name='register'),
    path('login', views.logIn, name='logIn'),
    path('logout', views.logOut, name='logOut'),
    path('booking', views.booking_form, name='booking_form'),
    path('setting', views.setting, name='setting'),


]