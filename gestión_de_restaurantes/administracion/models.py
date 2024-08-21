from django.db import models

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='menu_images/', null=True, blank=True, default='menu_images/default.jpg')
    disponible = models.BooleanField(default=True)

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
    reservada = models.BooleanField(default=False) 
    
    def __str__(self):
        return f'Mesa {self.numero} (Capacidad: {self.capacidad})'

    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
        ordering = ['numero']

class Empleado(models.Model):
    PUESTO_CHOICES = [
        ('camarero', 'Camarero'),
        ('cocinero', 'Cocinero'),
        ('limpieza', 'Limpieza'),
        ('mantenimiento', 'Mantenimiento'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100, choices=PUESTO_CHOICES)  # Actualización aquí
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']

class Venta(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADA', 'Completada'),
    ]

    fecha = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    mesa = models.ForeignKey('Mesa', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    pagado = models.BooleanField(default=False)  # Nuevo campo para marcar si se ha pagado

    def __str__(self):
        return f'Venta de {self.cantidad} {self.item.nombre} el {self.fecha}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['fecha']