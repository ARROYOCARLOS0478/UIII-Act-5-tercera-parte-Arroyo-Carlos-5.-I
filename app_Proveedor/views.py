# app_Proveedor/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Distribuidor, Producto # Solo trabajaremos con Proveedor por ahora
from django.db import IntegrityError # Para manejar errores de unique

# ----------------- Funciones para PROVEEDOR ------------------------------------------------------------
# [0] INICIO DEL SISTEMA (Muestra el inicio.html)
def inicio_sistema(request):
    """Muestra la página de inicio/bienvenida del sistema."""
    return render(request, 'inicio.html')

# [1] INICIO PROVEEDOR (Muestra la tabla de proveedores)
def inicio_proveedor(request):
    """Muestra la lista de proveedores."""
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})


# [2] AGREGAR PROVEEDOR (GET y POST)
def agregar_proveedor(request):
    if request.method == 'POST':
        # Captura de datos del formulario POST (sin forms.py)
        try:
            Proveedor.objects.create(
                nombre_empresa=request.POST.get('nombre_empresa'),
                contacto_principal=request.POST.get('contacto_principal'),
                telefono=request.POST.get('telefono'),
                email=request.POST.get('email'),
                direccion=request.POST.get('direccion'),
                activo=request.POST.get('activo') == 'on' # Checkbox activo
            )
            # Redirigir a la lista de proveedores después de agregar
            return redirect('ver_proveedores')
        except IntegrityError:
            # Manejo básico de datos duplicados (e.g., email o nombre_empresa)
            contexto = {'error': 'Error: El Nombre de la Empresa o Email ya existe.', 'es_post': True}
            return render(request, 'proveedor/agregar_proveedor.html', contexto)
        except Exception as e:
             contexto = {'error': f'Error al guardar: {e}', 'es_post': True}
             return render(request, 'proveedor/agregar_proveedor.html', contexto)
    
    # Si es GET, simplemente renderiza el formulario
    return render(request, 'proveedor/agregar_proveedor.html')


# [3] ACTUALIZAR PROVEEDOR (GET - Muestra el formulario con datos actuales)
def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


# [4] REALIZAR ACTUALIZACION PROVEEDOR (POST - Guarda los cambios)
def realizar_actualizacion_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    
    if request.method == 'POST':
        try:
            proveedor.nombre_empresa = request.POST.get('nombre_empresa')
            proveedor.contacto_principal = request.POST.get('contacto_principal')
            proveedor.telefono = request.POST.get('telefono')
            proveedor.email = request.POST.get('email')
            proveedor.direccion = request.POST.get('direccion')
            proveedor.activo = request.POST.get('activo') == 'on' # Checkbox activo
            
            # Guardar en la BD
            proveedor.save()
            return redirect('ver_proveedores')
        except IntegrityError:
            contexto = {'error': 'Error: El Nombre de la Empresa o Email ya existe.', 'proveedor': proveedor}
            return render(request, 'proveedor/actualizar_proveedor.html', contexto)
        except Exception as e:
            contexto = {'error': f'Error al actualizar: {e}', 'proveedor': proveedor}
            return render(request, 'proveedor/actualizar_proveedor.html', contexto)
    
    return redirect('ver_proveedores') # Si no es POST, regresa a la lista


# [5] BORRAR PROVEEDOR (GET - Muestra confirmación/se utiliza como acción directa)
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
        
    # Si es GET, muestra la página de confirmación
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# [6] INICIO/VER DISTRIBUIDOR-----------------------------------------------------------------------------------------------
def inicio_distribuidor(request):
    """Muestra la lista de distribuidores."""
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor')
    # Usamos un nuevo template para mostrar la tabla
    return render(request, 'distribuidor/ver_distribuidores.html', {'distribuidores': distribuidores})

# [7] AGREGAR DISTRIBUIDOR (GET y POST)
def agregar_distribuidor(request):
    if request.method == 'POST':
        try:
            # Captura de datos del formulario POST (sin forms.py)
            Distribuidor.objects.create(
                nombre_distribuidor=request.POST.get('nombre_distribuidor'),
                tipo_servicio=request.POST.get('tipo_servicio'),
                ciudad=request.POST.get('ciudad'),
                pais=request.POST.get('pais'),
                tiempo_entrega_dias=request.POST.get('tiempo_entrega_dias'),
                comision=request.POST.get('comision')
            )
            return redirect('ver_distribuidores')
        except IntegrityError:
            contexto = {'error': 'Error: El Nombre del Distribuidor ya existe.', 'es_post': True}
            return render(request, 'distribuidor/agregar_distribuidor.html', contexto)
    
    # Si es GET, simplemente renderiza el formulario
    return render(request, 'distribuidor/agregar_distribuidor.html')


# [8] ACTUALIZAR DISTRIBUIDOR (GET - Muestra el formulario con datos actuales)
def actualizar_distribuidor(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    return render(request, 'distribuidor/actualizar_distribuidor.html', {'distribuidor': distribuidor})


# [9] REALIZAR ACTUALIZACION DISTRIBUIDOR (POST - Guarda los cambios)
def realizar_actualizacion_distribuidor(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    
    if request.method == 'POST':
        try:
            distribuidor.nombre_distribuidor = request.POST.get('nombre_distribuidor')
            distribuidor.tipo_servicio = request.POST.get('tipo_servicio')
            distribuidor.ciudad = request.POST.get('ciudad')
            distribuidor.pais = request.POST.get('pais')
            distribuidor.tiempo_entrega_dias = request.POST.get('tiempo_entrega_dias')
            distribuidor.comision = request.POST.get('comision')
            
            distribuidor.save()
            return redirect('ver_distribuidores')
        except IntegrityError:
            contexto = {'error': 'Error: El Nombre del Distribuidor ya existe.', 'distribuidor': distribuidor}
            return render(request, 'distribuidor/actualizar_distribuidor.html', contexto)
    
    return redirect('ver_distribuidores') 


# [10] BORRAR DISTRIBUIDOR (GET/POST - Muestra confirmación/se utiliza como acción directa)
def borrar_distribuidor(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    
    if request.method == 'POST':
        distribuidor.delete()
        return redirect('ver_distribuidores')
        
    # Si es GET, muestra la página de confirmación
    return render(request, 'distribuidor/borrar_distribuidor.html', {'distribuidor': distribuidor})

# app_Proveedor/views.py (Fragmento, AÑADIR estas funciones)

# ... (Funciones CRUD para Distribuidor existentes)
# ...

# ----------------- Funciones para PRODUCTO -----------------

# [11] INICIO/VER PRODUCTO
def inicio_producto(request):
    """Muestra la lista de productos."""
    productos = Producto.objects.select_related('proveedor').all().order_by('nombre')
    return render(request, 'producto/ver_productos.html', {'productos': productos})

# [12] AGREGAR PRODUCTO (GET y POST)
def agregar_producto(request):
    proveedores = Proveedor.objects.all().order_by('nombre_empresa') 
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor') # Obtener lista de distribuidores

    contexto_base = {
        'proveedores': proveedores,
        'distribuidores': distribuidores 
    }
    
    if request.method == 'POST':
        # 1. Capturar todos los datos del formulario (incluyendo SKU)
        datos_formulario = {
            'nombre_producto': request.POST.get('nombre_producto'),
            'descripcion': request.POST.get('descripcion'),
            'precio': request.POST.get('precio'),
            'stock': request.POST.get('stock'),
            'proveedor_id': request.POST.get('proveedor_id'),
            'sku': request.POST.get('sku') 
        }
        proveedor_id = datos_formulario['proveedor_id'] 
        
        try:
            # 2. Obtener la instancia del proveedor y los IDs de distribuidores
            proveedor_instancia = Proveedor.objects.get(pk=proveedor_id)
            # request.POST.getlist se usa para campos 'multiple' de select
            distribuidores_ids = request.POST.getlist('distribuidores') 
            
            # 3. CREAR EL PRODUCTO y ASIGNARLO a 'nuevo_producto' (¡CORRECCIÓN CLAVE!)
            nuevo_producto = Producto.objects.create(
                nombre=datos_formulario['nombre_producto'],
                descripcion=datos_formulario['descripcion'],
                precio=datos_formulario['precio'],
                stock_actual=datos_formulario['stock'],
                sku=datos_formulario['sku'], 
                proveedor=proveedor_instancia 
            )
            
            # 4. Guardar la relación Muchos a Muchos (M2M)
            # Solo se puede llamar a .set() en el campo M2M después de que el objeto ha sido creado
            nuevo_producto.distribuidores.set(distribuidores_ids)
            
            return redirect('ver_productos')
        
        except IntegrityError:
            error_msg = 'Error: El Nombre del Producto o el SKU/Código ya existe.'
            contexto = {
                'error': error_msg, 
                'proveedores': proveedores,
                'distribuidores': distribuidores, # Persistencia de distribuidores
                'form_data': datos_formulario # Persistencia de campos llenados
            }
            return render(request, 'producto/agregar_producto.html', contexto)

        except Proveedor.DoesNotExist:
             error_msg = 'Error: El proveedor seleccionado no es válido.'
             contexto = {
                'error': error_msg, 
                'proveedores': proveedores,
                'distribuidores': distribuidores, 
                'form_data': datos_formulario 
            }
             return render(request, 'producto/agregar_producto.html', contexto)
    
    # Si es GET, simplemente renderiza el formulario
    return render(request, 'producto/agregar_producto.html', contexto_base)
        


# app_Proveedor/views.py (FUNCIÓN realizar_actualizacion_producto CORREGIDA)

# [13] ACTUALIZAR PRODUCTO (GET - Muestra el formulario con datos actuales)
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    # Necesitas los proveedores y distribuidores para rellenar los select
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor')
    
    contexto = {
        'producto': producto, 
        'proveedores': proveedores,
        'distribuidores': distribuidores
    }
    return render(request, 'producto/actualizar_producto.html', contexto)

# [14] REALIZAR ACTUALIZACION PRODUCTO (POST - Guarda los cambios)
def realizar_actualizacion_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    # Obtener todas las listas necesarias para el contexto de error (GET)
    proveedores = Proveedor.objects.all().order_by('nombre_empresa') 
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor')
    
    if request.method == 'POST':
        
        # 1. Captura de datos para persistencia en caso de error
        datos_formulario = {
            'nombre_producto': request.POST.get('nombre_producto'),
            'descripcion': request.POST.get('descripcion'),
            'precio': request.POST.get('precio'),
            'stock': request.POST.get('stock'),
            'proveedor_id': request.POST.get('proveedor_id'),
            'sku': request.POST.get('sku'), # Capturar SKU
            'distribuidores': request.POST.getlist('distribuidores') # Capturar IDs de distribuidores M2M
        }
        
        proveedor_id = datos_formulario['proveedor_id']
        distribuidores_ids = datos_formulario['distribuidores'] # Lista de IDs seleccionados

        try:
            # 2. Obtener la instancia del Proveedor (objeto) usando el ID
            proveedor_instancia = Proveedor.objects.get(pk=proveedor_id)
            
            # 3. Actualizar campos (incluyendo SKU)
            producto.nombre = datos_formulario['nombre_producto']
            producto.descripcion = datos_formulario['descripcion']
            producto.precio = datos_formulario['precio']
            producto.stock_actual = datos_formulario['stock']
            producto.sku = datos_formulario['sku'] # 💥 ACTUALIZAR SKU
            producto.proveedor = proveedor_instancia 
            
            # Guardar en la BD el objeto principal
            producto.save()
            
            # 4. 💥 GUARDAR LA RELACIÓN MUCHOS A MUCHOS (M2M) 💥
            # .set() reemplaza las relaciones antiguas con las nuevas IDs
            producto.distribuidores.set(distribuidores_ids) 
            
            return redirect('ver_productos')
        
        except Proveedor.DoesNotExist:
            error_msg = 'Error: Proveedor no válido.'
            contexto = {'error': error_msg, 'producto': producto, 'proveedores': proveedores, 'distribuidores': distribuidores, 'form_data': datos_formulario}
            return render(request, 'producto/actualizar_producto.html', contexto)
            
        except IntegrityError:
            error_msg = 'Error: El Nombre o el SKU ya existe.'
            contexto = {'error': error_msg, 'producto': producto, 'proveedores': proveedores, 'distribuidores': distribuidores, 'form_data': datos_formulario}
            return render(request, 'producto/actualizar_producto.html', contexto)
    
    # Si no es POST o si el objeto no se encuentra, usamos el contexto simple
    contexto_get = {
        'producto': producto, 
        'proveedores': proveedores,
        'distribuidores': distribuidores
    }
    return render(request, 'producto/actualizar_producto.html', contexto_get)


# [15] BORRAR PRODUCTO (GET/POST)
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
        
    # Si es GET, muestra la página de confirmación
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

