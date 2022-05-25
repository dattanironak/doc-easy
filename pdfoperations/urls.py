from django.urls import path
from . import views

urlpatterns = [
    path('mergepdf', views.mergePDF),
    path('CompressPdf',views.CompressPDF),  
    path('unlockPdf',views.UnlockPDF),
    path('lockPdf',views.ProtectPDF),
    path('extract',views.extract),
    path('splitpdf',views.Split)
 ]