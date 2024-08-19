from django.db import models

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    disponible = models.BooleanField(default=True)  # Nuevo campo

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Menú'
        verbose_name_plural = 'Menús'
        ordering = ['nombre']

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'Mesa {self.numero} (Capacidad: {self.capacidad})'

    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
        ordering = ['numero']

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Venta de {self.cantidad} {self.item.nombre} el {self.fecha}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['fecha']
