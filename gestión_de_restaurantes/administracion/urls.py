from django.urls import path
from . import views


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
    path('mesas/cambiar-disponibilidad/<int:pk>/', views.mesa_toggle_disponibilidad, name='mesa_toggle_disponibilidad'),

    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/nuevo/', views.empleado_create, name='empleado_create'),
    path('empleados/editar/<int:pk>/', views.empleado_edit, name='empleado_edit'),
    path('empleados/eliminar/<int:pk>/', views.EmpleadoDelete.as_view(), name='empleado_delete'),
    

    path('camarero/', views.vista_camarero, name='vista_camarero'),
    path('cambiar-estado-venta/<int:pk>/<str:nuevo_estado>/', views.cambiar_estado_venta, name='cambiar_estado_venta'),
    ############################################################################################################################
    path('cocina/', views.vista_cocina, name='pedidos_por_mesa'),
    path('cambiar-estado-venta/<int:pk>/<str:nuevo_estado>/', views.cambiar_estado_venta, name='cambiar_estado_venta'),
    #############################################################################################################################
    path('ventas/', views.venta_list, name='venta_list'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    ]
