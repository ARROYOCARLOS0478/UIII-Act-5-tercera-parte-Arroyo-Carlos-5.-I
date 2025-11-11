# app_Proveedor/models.py

from django.db import models

# --- 1. Modelo Proveedor (7 campos) ---
class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Empresa") 
    contacto_principal = models.CharField(max_length=100, verbose_name="Contacto Principal") 
    telefono = models.CharField(max_length=15, blank=True, null=True) 
    email = models.EmailField(unique=True) 
    direccion = models.CharField(max_length=200, verbose_name="Dirección") 
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro") 
    activo = models.BooleanField(default=True) 

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre_empresa']

    def __str__(self):
        return self.nombre_empresa

# --- 2. Modelo Distribuidor (7 campos) ---
class Distribuidor(models.Model):
    nombre_distribuidor = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Distribuidor") 
    tipo_servicio = models.CharField(max_length=50, choices=[('LOCAL', 'Local'), ('NACIONAL', 'Nacional'), ('INTERNACIONAL', 'Internacional')]) 
    ciudad = models.CharField(max_length=50) 
    pais = models.CharField(max_length=50) 
    tiempo_entrega_dias = models.IntegerField(verbose_name="Tiempo de Entrega (días)") 
    comision = models.DecimalField(max_digits=5, decimal_places=2, help_text="Comisión en porcentaje") 
    ultima_revision = models.DateField(auto_now=True, verbose_name="Última Revisión") 

    class Meta:
        verbose_name = "Distribuidor"
        verbose_name_plural = "Distribuidores"
        ordering = ['nombre_distribuidor']

    def __str__(self):
        return self.nombre_distribuidor

# --- 3. Modelo Producto (7 campos, incluyendo las relaciones) ---
class Producto(models.Model):
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name='productos_suministrados',
        verbose_name="ID Proveedor" 
    )

    distribuidores = models.ManyToManyField(
        Distribuidor,
        related_name='productos_distribuidos',
        verbose_name="Distribuidores"
    )

    nombre = models.CharField(max_length=150, unique=True, verbose_name="Nombre del Producto") 
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU/Código") 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    stock_actual = models.IntegerField(verbose_name="Stock Actual") 
    descripcion = models.TextField(blank=True, verbose_name="Descripción") 

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre