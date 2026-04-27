import pytest
from app.carrito_funciones import agregar_producto, mostrar_carrito

'''
def test_validar__producto_agregado(carrito_vacio, producto_nuevo):
    carrito = agregar_producto(carrito_vacio, producto_nuevo)
    # assert se usa para buscar un resultado esperado, si el resultado no es el esperado, se lanza una excepción y el test falla
    assert len(carrito) == 1
    
def test_nombre_producto(carrito_vacio, producto_nuevo):
    carrito = agregar_producto(carrito_vacio, producto_nuevo)
    # assert se usa para buscar un resultado esperado, si el resultado no es el esperado, se lanza una excepción y el test falla
    assert carrito[0]["nombre"] == "Manzana"

def test_precio_producto(carrito_vacio, producto_nuevo):
    carrito = agregar_producto(carrito_vacio, producto_nuevo)
    # assert se usa para buscar un resultado esperado, si el resultado no es el esperado, se lanza una excepción y el test falla
    assert carrito[0]["precio"] == 2000
'''
    
# Unifico los 3 test anteriores en uno solo, para validar el producto agregado al carrito, su nombre y su precio
def test_validar_producto_agregado(carrito_vacio, producto_nuevo):
    carrito = agregar_producto(carrito_vacio, producto_nuevo)
    assert len(carrito) == 1
    assert carrito[0]["nombre"] == "Manzana"
    assert carrito[0]["precio"] == 2000

#prueba con batch de productos, para validar que se agregan correctamente al carrito
def test_agregar_batch_productos(carrito_vacio, batch_productos):       
    for producto in batch_productos:
        carrito_vacio = agregar_producto(carrito_vacio, producto)
    assert len(carrito_vacio) == 3
    assert carrito_vacio[0]["nombre"] == "Manzana"
    assert carrito_vacio[1]["nombre"] == "Banana"
    assert carrito_vacio[2]["nombre"] == "Naranja"  

# mostrar en pantalla el carrito con los 3 productos agregados, para validar que se muestran correctamente
def test_mostrar_carrito(batch_productos):
    carrito = []
    for producto in batch_productos:
        carrito = agregar_producto(carrito, producto)
    mostrar_carrito(carrito)
    
# mostrar en pantalla el carrito para el caso que este vacio y chequear el mensaje que se muestra, para validar que se muestra el mensaje correcto
def test_mostrar_carrito_vacio(carrito_vacio, capsys):
    mostrar_carrito(carrito_vacio)
    # capsys captura lo que se le manda a imprimir en pantalla, y lo guarda en un objeto con dos atributos: out (lo que se imprimió) y err (lo que se imprimió por error)
    captura = capsys.readouterr()
    assert "El carrito está vacío." in captura.out
    