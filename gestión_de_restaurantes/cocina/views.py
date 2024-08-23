from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta

def pedidos_por_mesa(request):
    # Filtramos las ventas para obtener solo aquellas que están en proceso o preparadas
    ventas = Venta.objects.filter(estado__in=['EN_PROCESO', 'PENDIENTE']).order_by('fecha').select_related('item')
    return render(request, 'administracion/cocina.html', {'ventas': ventas})

def cambiar_estado_venta(request, pk, nuevo_estado):
    venta = get_object_or_404(Venta, pk=pk)
    venta.estado = nuevo_estado
    venta.save()
    return redirect('pedidos_por_mesa')
