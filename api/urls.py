from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.Register), 
    path('users/login', views.Login),
    
 ]