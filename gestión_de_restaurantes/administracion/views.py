# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Mesa, Empleado, Venta
from .forms import MenuForm, MesaForm, EmpleadoForm, VentaForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Vistas para Menu
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

# Vistas para Empleado
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

# Vistas para Venta
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

# ################# Vista principal ################################
def index(request):
    return render(request, 'administracion/index.html')
