from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('users.urls')),
    path('', views.home),
    path('api/',include('api.urls')),
    path('pdfop/',include('pdfoperations.urls')),
    path('toPdf/',include('convertions.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)