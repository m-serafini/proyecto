import pytest
from utils.funciones import (
    iniciar_sesion, obtener_titulo, traer_datos_producto,
    agregar_al_carrito, obtener_contador_carrito, ir_al_carrito, verificar_producto_en_carrito
)

# Caso de prueba: Valida el proceso de login, la redirección y elementos del catálogo.
def test_login_y_verificacion_catalogo(navegador, usuario, password):

    # 1. Ingreso a la página de login
    navegador.get("https://www.saucedemo.com")

    iniciar_sesion(navegador, usuario, password)
    
    # 2. Valido la redirección a inventario 
    assert "/inventory.html" in navegador.current_url
    
    # 3. Valido título de la página 
    assert obtener_titulo(navegador) == "Products"
    
    # 4. Valido presencia de texto "Swag Labs" 
    assert "Swag Labs" in navegador.page_source
    
    # 5. Valido que existan productos visibles 
    items = navegador.find_elements("class name", "inventory_item")
    assert len(items) > 0
    
    # 6. Valido presencia de elementos de interfaz (Filtros) 
    assert navegador.find_element("class name", "product_sort_container").is_displayed()
    
    # 7. Listo nombre/precio del primero [cite: 38]
    nombre, precio = traer_datos_producto(navegador)
    print(f"\nVerificación de catálogo - Producto: {nombre} | Precio: {precio}")

# Caso de Prueba de Carrito: Añadir, incrementar contador y verificar en carrito.
def test_interaccion_carrito_compras(navegador, usuario, password):
    
    # 1. Ingreso a la página de login
    navegador.get("https://www.saucedemo.com")
    
    iniciar_sesion(navegador, usuario, password)
    
    # 2. Añado un producto al carrito (ESTO FALTABA)
    agregar_al_carrito(navegador)
    
    # 3. Verifico que el contador del carrito se incremente
    assert obtener_contador_carrito(navegador) == "1"
    
    # 4. Navego al carrito de compras
    ir_al_carrito(navegador)
    assert "/cart.html" in navegador.current_url
    
    # 5. Compruebo que el producto aparezca correctamente en el carrito
    assert verificar_producto_en_carrito(navegador) is True
    