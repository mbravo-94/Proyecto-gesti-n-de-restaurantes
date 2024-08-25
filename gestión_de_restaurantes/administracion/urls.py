from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Rutas para el Menú
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/nuevo/', views.menu_create, name='menu_create'),
    path('menus/editar/<int:pk>/', views.menu_edit, name='menu_edit'),
    path('menus/eliminar/<int:pk>/', views.MenuDelete.as_view(), name='menu_confirm_delete'),
    path('menus/cambiar-disponibilidad/<int:pk>/', views.cambiar_disponibilidad, name='cambiar_disponibilidad'),

    # Rutas para Mesas
    path('mesas/', views.mesa_list, name='mesa_list'),
    path('mesas/nueva/', views.mesa_create, name='mesa_create'),
    path('mesas/editar/<int:pk>/', views.mesa_edit, name='mesa_edit'),
    path('mesas/eliminar/<int:pk>/', views.MesaDelete.as_view(), name='mesa_delete'),
    path('mesas/cambiar-disponibilidad/<int:pk>/', views.mesa_toggle_disponibilidad, name='mesa_toggle_disponibilidad'),

    # Rutas para Empleados
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/nuevo/', views.empleado_create, name='empleado_create'),
    path('empleados/editar/<int:pk>/', views.empleado_edit, name='empleado_edit'),
    path('empleados/eliminar/<int:pk>/', views.EmpleadoDelete.as_view(), name='empleado_delete'),

    # Rutas para Camarero y Ventas
    path('camarero/', views.vista_camarero, name='vista_camarero'),
    path('cambiar-estado-venta/<int:pk>/<str:nuevo_estado>/', views.cambiar_estado_venta, name='cambiar_estado_venta'),

    # Rutas para Ventas (incluyendo propinas)
    path('ventas/', views.venta_list, name='venta_list'),
    path('ventas/nueva/', views.venta_create, name='venta_create'),
    path('ventas/editar/<int:pk>/', views.venta_edit, name='venta_edit'),
    path('ventas/eliminar/<int:pk>/', views.VentaDelete.as_view(), name='venta_delete'),
    path('ventas/agregar-propina/<int:pk>/', views.agregar_propina, name='agregar_propina'),

    # Rutas para Login y Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
