# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Mesa, Empleado, Venta
from .forms import MenuForm, MesaForm, EmpleadoForm, VentaForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView

########################## Vistas para Menu ###########################
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'administracion/menu_list.html', {'menus': menus})

def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'administracion/menu_form.html', {'form': form})

def menu_edit(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'administracion/menu_form.html', {'form': form})

class MenuDelete(DeleteView):
    model = Menu
    template_name = 'administracion/menu_confirm_delete.html'
    success_url = reverse_lazy('menu_list')

def cambiar_disponibilidad(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        disponible = request.POST.get('disponible') == 'True'
        menu.disponible = disponible
        menu.save()
        return redirect('menu_list')
    return render(request, 'administracion/cambiar_disponibilidad.html', {'menu': menu})


# #######################  Vistas para Mesa  #################################
def mesa_list(request):
    mesas = Mesa.objects.all()
    return render(request, 'administracion/mesa_list.html', {'mesas': mesas})

def mesa_create(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesa_list')
    else:
        form = MesaForm()
    return render(request, 'administracion/mesa_form.html', {'form': form})

def mesa_edit(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('mesa_list')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'administracion/mesa_form.html', {'form': form})

class MesaDelete(DeleteView):
    model = Mesa
    template_name = 'administracion/mesa_confirm_delete.html'
    success_url = reverse_lazy('mesa_list')

def mesa_toggle_disponibilidad(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == "POST":
        disponible = request.POST.get('disponible') == 'True'
        mesa.disponible = disponible
        mesa.save()
        return redirect('mesa_list')
    return render(request, 'administracion/mesa_toggle_disponibilidad.html', {'mesa': mesa})

################################ Vistas para Empleado #################################
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'administracion/empleado_list.html', {'empleados': empleados})

def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'administracion/empleado_form.html', {'form': form})

def empleado_edit(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'administracion/empleado_form.html', {'form': form})

class EmpleadoDelete(DeleteView):
    model = Empleado
    template_name = 'administracion/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')

################################ vistas para cocina #################################

def vista_cocina(request):
    ordenes_pendientes = Venta.objects.filter(estado='PENDIENTE').order_by('fecha')
    return render(request, 'administracion/vista_cocina.html', {'ordenes': ordenes_pendientes})

################################ vistas para camarero  ################################

def vista_camarero(request):
    # Recuperar todas las ventas que están pendientes o en proceso
    ordenes_pendientes = Venta.objects.filter(estado__in=['PENDIENTE', 'EN_PROCESO']).order_by('fecha')
    context = {
        'ordenes': ordenes_pendientes
    }
    return render(request, 'administracion/vista_camarero.html', context)


######################################## Vistas para Venta ####################################

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'administracion/venta_list.html', {'ventas': ventas})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'administracion/venta_form.html', {'form': form})

def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'administracion/venta_form.html', {'form': form})

class VentaDelete(DeleteView):
    model = Venta
    template_name = 'administracion/venta_confirm_delete.html'
    success_url = reverse_lazy('venta_list')

def cambiar_estado_venta(request, pk, nuevo_estado):
    venta = get_object_or_404(Venta, pk=pk)
    
    if nuevo_estado == 'COMPLETADA':
        venta.estado = nuevo_estado
        if 'marcar_pagado' in request.POST:
            venta.pagado = True
            # Cambiar la mesa a disponible si el pago está completo
            venta.mesa.reservada = False
            venta.mesa.disponible = True
            venta.mesa.save()
        venta.save()
        
    return redirect('vista_camarero')

def mesas_disponibles_view(request):
    # Mostrar mesas que están disponibles, no reservadas y no asociadas a ventas sin pagar
    mesas_disponibles = Mesa.objects.filter(disponible=True, reservada=False)
    
    return render(request, 'usuarios/mesas_disponibles.html', {'mesas': mesas_disponibles})


##################### Vista principal ################################
def index(request):
    return render(request, 'administracion/index.html')  # Llama a la pagina index.html 

def index(request):
    # Calcular los totales de pedidos
    total_pedidos = Venta.objects.count()
    pedidos_pendientes = Venta.objects.filter(estado='PENDIENTE').count()
    pedidos_en_proceso = Venta.objects.filter(estado='EN_PROCESO').count()
    pedidos_entregados = Venta.objects.filter(estado='COMPLETADA').count()

    # Obtener las mesas disponibles
    mesas_disponibles = Mesa.objects.filter(disponible=True, reservada=False)

    context = {
        'total_pedidos': total_pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_en_proceso': pedidos_en_proceso,
        'pedidos_entregados': pedidos_entregados,
        'mesas_disponibles': mesas_disponibles,
    }

    return render(request, 'administracion/index.html', context)



############Login Administrador ##############

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Vista de Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirigir a la página de administración después del login
        else:
            return render(request, 'administracion/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'administracion/login.html')

# Vista de Logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirigir a la página de login después de cerrar sesión

# Vista de la Página de Administración, protegida por login
@login_required(login_url='login')
def index(request):
    return render(request, 'administracion/index.html')


######################### Prueba_Index #########################

