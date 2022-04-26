
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from noticias.views import Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Inicio.as_view(),name='index'),
]
