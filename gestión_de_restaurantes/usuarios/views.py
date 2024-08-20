# usuarios/views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Carrito, CarritoItem

from administracion.models import Venta

from django.shortcuts import render
from administracion.models import Menu, Mesa

def index(request):
    return render(request, 'usuarios/index.html')


def menu_list_view(request):
    # Filtrar menús creados por el administrador
    menus = Menu.objects.all()  # O aplicar un filtro si necesitas
    context = {
        'menus': menus
    }
    return render(request, 'usuarios/menu_usuarios.html', context)


def menu_disponible_view(request):
    menus_disponibles = Menu.objects.filter(disponible=True)
    context = {
        'menus': menus_disponibles
    }
    return render(request, 'usuarios/menu_disponible.html', context)

def mesas_disponibles_view(request):
    mesas_disponibles = Mesa.objects.filter(disponible=True)
    context = {
        'mesas_disponibles': mesas_disponibles
    }
    return render(request, 'usuarios/mesas_disponibles.html', context)




############################## CARRITO #####################    
def agregar_al_carrito(request, menu_id):
    menu_item = get_object_or_404(Menu, id=menu_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, menu=menu_item)
    carrito_item.cantidad += 1
    carrito_item.save()
    return redirect('menu_disponible')


def procesar_compra(request):
    carrito = Carrito.objects.get(usuario=request.user)
    for item in carrito.items.all():
        Venta.objects.create(item=item.menu, cantidad=item.cantidad)
    carrito.delete()  # Vaciar el carrito después de la compra
    return render(request, 'usuarios/compra_exitosa.html')

def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    context = {
        'carrito': carrito
    }
    return render(request, 'usuarios/carrito.html', context)