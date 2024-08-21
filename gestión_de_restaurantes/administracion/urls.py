from django.urls import path
from . import views
from views.pedidos_cocina import cocina_view


urlpatterns = [
    path('', views.index, name='index'),
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/nuevo/', views.menu_create, name='menu_create'),
    path('menus/editar/<int:pk>/', views.menu_edit, name='menu_edit'),
    path('menus/eliminar/<int:pk>/', views.MenuDelete.as_view(), name='menu_confirm_delete'),
    path('menus/cambiar-disponibilidad/<int:pk>/', views.cambiar_disponibilidad, name='cambiar_disponibilidad'),


    path('mesas/', views.mesa_list, name='mesa_list'),
    path('mesas/nueva/', views.mesa_create, name='mesa_create'),
    path('mesas/editar/<int:pk>/', views.mesa_edit, name='mesa_edit'),
    path('mesas/eliminar/<int:pk>/', views.MesaDelete.as_view(), name='mesa_delete'),

    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/nuevo/', views.empleado_create, name='empleado_create'),
    path('empleados/editar/<int:pk>/', views.empleado_edit, name='empleado_edit'),
    path('empleados/eliminar/<int:pk>/', views.EmpleadoDelete.as_view(), name='empleado_delete'),
    
    path('ventas/', views.venta_list, name='venta_list'),
    
    path('cocina/', views.cocina_view, name='cocina_view'),
]