from django import forms
from .models import Menu, Mesa, Empleado, Venta

# Define las categorías posibles en una lista
CATEGORIA_CHOICES = [
    ('Entrante', 'Entrante'),
    ('Plato Principal', 'Plato Principal'),
    ('Ensalada', 'Ensalada'),
    ('Postre', 'Postre'),
    ('Bebida', 'Bebida'),
    # Se puede añadir mnas categorias si fuera necesario
]

class MenuForm(forms.ModelForm):
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES)

    class Meta:
        model = Menu
        fields = ['nombre', 'precio', 'descripcion', 'categoria', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'imagen': forms.ClearableFileInput(attrs={'multiple': False}),
        }

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'capacidad']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'puesto', 'fecha_contratacion']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['item', 'cantidad']
        widgets = {
            'item': forms.Select(),
            'cantidad': forms.NumberInput(attrs={'min': 1}),
        }