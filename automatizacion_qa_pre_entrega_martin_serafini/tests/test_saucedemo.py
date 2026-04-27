import pytest
from utils.funciones import (
    iniciar_sesion, obtener_titulo, traer_datos_producto,
    agregar_al_carrito, obtener_contador_carrito, ir_al_carrito, verificar_producto_en_carrito
)

def test_login_y_verificacion_catalogo(navegador, usuario, password):
    """
    Valida el proceso de login, la redirección y elementos del catálogo. [cite: 22, 30]
    """
    navegador.get("https://www.saucedemo.com")
    
    # 1. Automatización de Login con espera explícita (dentro de la función) 
    iniciar_sesion(navegador, usuario, password)
    
    # 2. Validar redirección a inventario 
    assert "/inventory.html" in navegador.current_url
    
    # 3. Validar título de la página 
    assert obtener_titulo(navegador) == "Products"
    
    # 4. Validar presencia de texto "Swag Labs" 
    assert "Swag Labs" in navegador.page_source
    
    # 5. Validar que existan productos visibles 
    items = navegador.find_elements("class name", "inventory_item")
    assert len(items) > 0
    
    # 6. Validar presencia de elementos de interfaz (Filtros) 
    assert navegador.find_element("class name", "product_sort_container").is_displayed()
    
    # 7. Listar nombre/precio del primero [cite: 38]
    nombre, precio = traer_datos_producto(navegador)
    print(f"\nVerificación de catálogo - Producto: {nombre} | Precio: {precio}")

def test_interaccion_carrito_compras(navegador, usuario, password):
    """
    Caso de Prueba de Carrito: Añadir, incrementar contador y verificar en carrito.
    """
    navegador.get("https://www.saucedemo.com")
    iniciar_sesion(navegador, usuario, password)
    
    # 1. Añadir un producto al carrito (ESTO FALTABA)
    agregar_al_carrito(navegador)
    
    # 2. Verificar que el contador del carrito se incremente
    # Ahora sí debería encontrar el elemento ".shopping_cart_badge"
    assert obtener_contador_carrito(navegador) == "1"
    
    # 3. Navegar al carrito de compras
    ir_al_carrito(navegador)
    assert "/cart.html" in navegador.current_url
    
    # 4. Comprobar que el producto aparezca correctamente en el carrito
    assert verificar_producto_en_carrito(navegador) is True
    