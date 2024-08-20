# usuarios/urls.py

from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='usuarios_index'), 
    path('agregar_al_carrito/<int:menu_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('procesar_compra/', views.procesar_compra, name='procesar_compra'),
    path('mesas/', views.mesas_disponibles_view, name='mesas_disponibles'),
    path('menu/', views.menu_disponible_view, name='menu_disponible'),
    path('eliminar_del_carrito/<int:menu_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('seleccionar_mesa/', views.seleccionar_mesa, name='seleccionar_mesa'),
]
