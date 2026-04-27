from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Función para iniciar sesión en la aplicación
def iniciar_sesion(driver, usuario, contrasena):
    # Creamos la espera dentro de la función
    espera = WebDriverWait(driver, 10)
    # Localizadores de los elementos de la página de inicio de sesión
    campo_usuario = (By.ID, "user-name")
    campo_contrasena = (By.ID, "password")
    boton_login = (By.ID, "login-button")
    # Esperamos a que los elementos sean visibles y realizamos las acciones necesarias 
    espera.until(EC.visibility_of_element_located(campo_usuario)).send_keys(usuario)
    espera.until(EC.visibility_of_element_located(campo_contrasena)).send_keys(contrasena)
    espera.until(EC.element_to_be_clickable(boton_login)).click()

# Función para obtener el título de la página después de iniciar sesión
def obtener_titulo(driver):
    # Creamos la espera dentro de la función
    espera = WebDriverWait(driver, 10)
    # Localizador del elemento que contiene el título de la página
    elemento_titulo = (By.CLASS_NAME, "title")
    # Esperamos a que el elemento del título sea visible y retornamos su texto
    return espera.until(EC.visibility_of_element_located(elemento_titulo)).text

# Función para extraer datos del primer producto (Requisito de la entrega)
def traer_datos_producto(driver):
    # Buscamos el nombre y el precio del primer artículo que aparezca
    nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    return nombre, precio

def agregar_al_carrito(driver):
    # Buscamos el primer botón de "Add to cart" y hacemos clic
    boton = driver.find_element(By.CLASS_NAME, "btn_inventory")
    boton.click()

def obtener_contador_carrito(driver):
    """Devuelve el número que aparece en el ícono del carrito."""
    return driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

def ir_al_carrito(driver):
    """Navega a la página del carrito de compras."""
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

def verificar_producto_en_carrito(driver):
    """Comprueba que haya al menos un producto en la lista del carrito."""
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    return len(items) > 0