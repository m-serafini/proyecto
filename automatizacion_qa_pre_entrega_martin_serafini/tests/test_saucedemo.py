import pytest
from utils.funciones import (
    iniciar_sesion, obtener_titulo, traer_datos_producto,
    agregar_al_carrito, obtener_contador_carrito, ir_al_carrito, 
    verificar_producto_en_carrito, obtener_mensaje_error
)

# --- CASOS PRE-ENTREGA---
def test_login_y_verificacion_catalogo(navegador, usuario, password):
    # Valida el proceso de login, la redirección y elementos del catálogo
    # Acceso    
    navegador.get("https://www.saucedemo.com")
    print("\n[1] Accediendo a la URL de SauceDemo.")
    # Autenticación
    iniciar_sesion(navegador, usuario, password)
    print(f"[2] Intento de login con usuario: {usuario}")
    # Validación de la redirección
    assert "/inventory.html" in navegador.current_url
    print(f"[3] Redirección confirmada a: {navegador.current_url}")
    # Validación de UI
    assert obtener_titulo(navegador) == "Products"
    assert "Swag Labs" in navegador.page_source
    print("[4] Título 'Products' y logo 'Swag Labs' verificados correctamente.")
    # Verificación de carga de productos
    items = navegador.find_elements("class name", "inventory_item")
    assert len(items) > 0
    print(f"[5] Validación de catálogo: Se encontraron {len(items)} productos visibles.")
    # Verificación de que estan los Filtros
    assert navegador.find_element("class name", "product_sort_container").is_displayed()
    print("[6] Filtros detectado y visible.")
    # Extracción de datos del primer producto
    nombre, precio = traer_datos_producto(navegador)
    print(f"[7] Verificación de catálogo - Producto: {nombre} | Precio: {precio}")

def test_interaccion_carrito_compras(navegador, usuario, password):
    # Caso de Prueba de Carrito: Añadir, incrementar contador y verificar en carrito.
    # Acceso
    navegador.get("https://www.saucedemo.com")
    print("\n[1] Navegando a la página de inicio de sesión.")
    # Autenticación
    iniciar_sesion(navegador, usuario, password)
    print(f"[2] Sesión iniciada con el usuario: {usuario}")
    # Acción de compra
    agregar_al_carrito(navegador)
    print("[3] Producto seleccionado y añadido al carrito.")
    # Validación
    contador = obtener_contador_carrito(navegador)
    assert contador == "1"
    print(f"[4] Validación exitosa: El contador del carrito muestra {contador} unidad(es).")
    # 5 Navegación al checkout
    ir_al_carrito(navegador)
    assert "/cart.html" in navegador.current_url
    print("[5] Navegación al carrito de compras confirmada.")
    # 6: Verificación de persistencia
    assert verificar_producto_en_carrito(navegador) is True
    print("[6] Producto verificado correctamente dentro del carrito. Test finalizado con éxito.")

# CASOS ADICIONALES: LOGUEO INCORRECTO 
@pytest.mark.parametrize("user, pw, mensaje_esperado", [
    ("", "", "Epic sadface: Username is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"), 
    ("", "wrong_password", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),         
    ("wrong_user", "", "Epic sadface: Password is required"),            
    ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
    ("wrong_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service") 
])
def test_login_incorrecto(navegador, user, pw, mensaje_esperado):
    # Objetivo: Validar que el sistema bloquee el acceso con credenciales inválidas.
    # Datos: Usuario '{user}', Password '{pw}'.
    # Resultado esperado: Mensaje '{mensaje_esperado}'.
    navegador.get("https://www.saucedemo.com")
    iniciar_sesion(navegador, user, pw)
    assert obtener_mensaje_error(navegador) == mensaje_esperado

# CASOS ADICIONALES: USUARIOS VÁLIDOS
@pytest.mark.parametrize("user", [
    "standard_user", 
    "locked_out_user", 
    "problem_user", 
    "performance_glitch_user", 
    "error_user", 
    "visual_user"
])
def test_otros_usuarios_validos(navegador, user, password):
    # Pruebo cada usuario de la lista
    # user (str): Nombre de usuario obtenido mediante parametrización.
    # password_valido (str): Contraseña común 'secret_sauce'.
    navegador.get("https://www.saucedemo.com")
    iniciar_sesion(navegador, user, password)
    
    if user == "locked_out_user":
        assert "locked out" in obtener_mensaje_error(navegador)
    else:
        # Uso un mensaje de error personalizado para saber quién falló en el reporte
        assert "/inventory.html" in navegador.current_url, f"El usuario {user} no pudo ingresar"