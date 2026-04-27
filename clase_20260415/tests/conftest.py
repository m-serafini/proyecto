import pytest

@pytest.fixture
def producto_nuevo():
    return {"nombre": "Manzana", "precio": 2000}

@pytest.fixture
def carrito_vacio():
    return []

@pytest.fixture
def batch_productos():
    return [
        {"nombre": "Manzana", "precio": 2000},
        {"nombre": "Banana", "precio": 1500},
        {"nombre": "Naranja", "precio": 1800}
    ]