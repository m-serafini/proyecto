import pytest
from calculadora.operaciones import sumar, restar, multiplicar, dividir

@pytest.mark.suma
def test_sumar_fixture(datos_suma):
    a, b, esperado = datos_suma
    assert sumar(a, b) == esperado

def test_restar_fixture(datos_resta):
    a, b, esperado = datos_resta
    assert restar(a, b) == esperado

def test_multiplicar(datos_multiplicacion):
    a, b, esperado = datos_multiplicacion
    assert multiplicar(a, b) == esperado

def test_dividir(datos_division):
    a, b, esperado = datos_division
    assert dividir(a, b) == esperado

def test_division_por_cero(datos_division_error):
    a, b = datos_division_error # Desempaqueto los datos
    # Verifico que se lance la excepción y valido el mensaje
    with pytest.raises(ZeroDivisionError) as excinfo:
        dividir(a, b)
    
    # Valido que el mensaje de error sea el correcto
    assert str(excinfo.value) == "No es posible dividir por cero"

# Pruebas parametrizadas para sumar 

@pytest.mark.suma

@pytest.mark.parametrize("a, b, esperado", [
    (10, 5, 15),   # Suma de números enteros
    (-1, 1, 0),    # Suma de números con signo
    (0, 0, 0)      # Suma de ceros
])
# Uso los mismos nombres del decorador, no desempaqueto
def test_sumar_parametrize(a, b, esperado): 
    assert sumar(a, b) == esperado

# Pruebas parametrizadas para restar    
@pytest.mark.parametrize("a, b, esperado", [
    (10, 5, 5),    # Resta de números enteros
    (-1, 1, -2),   # Resta de números con signo
    (0, 0, 0)      # Resta de ceros
])
# Uso los mismos nombres del decorador, no desempaqueto
def test_restar_parametrize(a, b, esperado): 
    assert restar(a, b) == esperado

