# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='usuarios_index'),  # Una vista básica para la app usuarios
]
