from django.shortcuts import render
from .models import Venta

def cocina_view(request):
    # Obtener todas las ventas (pedidos)
    ventas = Venta.objects.all()
    
    # Pasar los pedidos a la plantilla
    return render(request, 'administracion/cocina.html', {'ventas': ventas})
