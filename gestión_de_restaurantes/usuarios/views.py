# usuarios/views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Carrito, CarritoItem

from django.shortcuts import render

from administracion.models import Menu, Mesa, Venta

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
    carrito = request.session.get('carrito', {})
    mesa_id = request.session.get('mesa_id')
    mesa = Mesa.objects.get(id=mesa_id) if mesa_id else None

    # Calcular el total del carrito
    total = sum(float(item['precio']) * item['cantidad'] for item in carrito.values())
    
    context = {
        'menus': menus_disponibles,
        'carrito': carrito,
        'total': total,
        'mesa': mesa,
    }
    return render(request, 'usuarios/menu_disponible.html', context)

def mesas_disponibles_view(request):
    # Mostrar mesas que están disponibles y no están reservadas
    mesas_disponibles = Mesa.objects.filter(disponible=True, reservada=False)
    
    if request.method == 'POST':
        mesa_id = request.POST.get('mesa_id')
        mesa = get_object_or_404(Mesa, id=mesa_id)
        mesa.reservada = True
        mesa.save()

        # Guardar la mesa seleccionada en la sesión para uso futuro (p.ej., en la compra)
        request.session['mesa_id'] = mesa.id
        
        return redirect('menu_disponible')  # Redirigir al menú para comenzar a hacer pedidos

    return render(request, 'usuarios/mesas_disponibles.html', {'mesas': mesas_disponibles})

def seleccionar_mesa(request):
    if request.method == 'POST':
        numero_mesa = request.POST.get('numero_mesa')
        mesa = Mesa.objects.filter(numero=numero_mesa, disponible=True).first()
        if mesa:
            request.session['mesa_id'] = mesa.id
            return redirect('menu_disponible')  # Redirige al menú después de seleccionar la mesa
        else:
            return render(request, 'usuarios/seleccionar_mesa.html', {'error': 'Mesa no disponible o no existe'})
    return render(request, 'usuarios/seleccionar_mesa.html')



############################## CARRITO #####################    
def agregar_al_carrito(request, menu_id):
    if 'mesa_id' not in request.session:
        return redirect('seleccionar_mesa')

    menu_item = get_object_or_404(Menu, id=menu_id)
    
    # Obtener o crear un carrito basado en la sesión
    carrito = request.session.get('carrito', {})

    # Si el ítem ya está en el carrito, aumentar la cantidad
    if str(menu_id) in carrito:
        carrito[str(menu_id)]['cantidad'] += 1
    else:
        carrito[str(menu_id)] = {
            'nombre': menu_item.nombre,
            'precio': str(menu_item.precio),
            'cantidad': 1
        }
    
    # Guardar el carrito en la sesión
    request.session['carrito'] = carrito

    return redirect('menu_disponible')  # Redirigir de vuelta al menú disponible

def procesar_compra(request):
    carrito = request.session.get('carrito', {})
    mesa_id = request.session.get('mesa_id')
    
    if not mesa_id:
        return redirect('mesas_disponibles')  # Asegurarse de que una mesa esté seleccionada

    mesa = get_object_or_404(Mesa, id=mesa_id)

    # Procesar cada ítem del carrito
    for menu_id, item in carrito.items():
        menu_item = get_object_or_404(Menu, id=menu_id)
        Venta.objects.create(item=menu_item, cantidad=item['cantidad'], mesa=mesa, estado='PENDIENTE')

    # Vaciar el carrito y eliminar la mesa seleccionada
    request.session['carrito'] = {}
    del request.session['mesa_id']

    return render(request, 'usuarios/compra_exitosa.html')

def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    context = {
        'carrito': carrito
    }
    return render(request, 'usuarios/carrito.html', context)


def eliminar_del_carrito(request, menu_id):
    carrito = request.session.get('carrito', {})

    # Eliminar el ítem del carrito si existe
    if str(menu_id) in carrito:
        del carrito[str(menu_id)]

    # Actualizar el carrito en la sesión
    request.session['carrito'] = carrito

    return redirect('menu_disponible')  # Redirigir de vuelta al menú disponible o a la página que desees