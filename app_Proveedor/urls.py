# app_Proveedor/urls.py (Versión Corregida y Completa)

from django.urls import path
from . import views

urlpatterns = [
    # ... (Rutas de Proveedor existentes)
    path('', views.inicio_proveedor, name='ver_proveedores'), 
    path('inicio/', views.inicio_sistema, name='inicio'), 
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/guardar_actualizacion/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),

    # ----------------- CRUD Distribuidor -----------------
    path('distribuidor/', views.inicio_distribuidor, name='ver_distribuidores'), 
    path('distribuidor/agregar/', views.agregar_distribuidor, name='agregar_distribuidor'),
    path('distribuidor/actualizar/<int:pk>/', views.actualizar_distribuidor, name='actualizar_distribuidor'),
    path('distribuidor/guardar_actualizacion/<int:pk>/', views.actualizar_distribuidor, name='realizar_actualizacion_distribuidor'),
    path('distribuidor/borrar/<int:pk>/', views.borrar_distribuidor, name='borrar_distribuidor'),

    # 💥💥 RUTAS FALTANTES: CRUD PRODUCTO 💥💥
    path('producto/', views.inicio_producto, name='ver_productos'), 
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/guardar_actualizacion/<int:pk>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:pk>/', views.borrar_producto, name='borrar_producto'),
]