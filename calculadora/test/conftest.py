import pytest

# Fixture para la suma
@pytest.fixture
def datos_suma():
    return 10, 10, 20

# Fixture para la resta
@pytest.fixture
def datos_resta():
    return 20, 8, 12

# Fixture para la multiplicación
@pytest.fixture
def datos_multiplicacion():
    return 6, 7, 42

# Fixture para la división exitosa
@pytest.fixture
def datos_division():
    return 100, 4, 25

# Fixture para el caso de error (División por cero)
@pytest.fixture
def datos_division_error():
    return 10, 0

# Fixtures para las pruebas de validación de entrada
@pytest.fixture
def inputs_validos_numero():
    return ["10.5"]

@pytest.fixture
def inputs_invalidos_numero():
    # Simulamos que primero escribe "letras" (falla) y luego "5" (éxito)
    return ["letras", "5"]

@pytest.fixture
def opcion_correcta():
    return ["1"]

@pytest.fixture
def opcion_incorrecta():
    return ["9"]