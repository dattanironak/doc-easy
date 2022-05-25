from django.urls import path
from . import views

urlpatterns = [
    path('imgToPdf', views.ImgtoPDF), 
    path('wordToPdf',views.WORDtoPDF),
    path('excelToPdf',views.ExcelToPDF),
    path('pptToPdf',views.PPTtoPDF),
    path('txtToPdf',views.TexttoPDF),
 ]