from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('loginUser/', views.LoginPage, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser')

]
