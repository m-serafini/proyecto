import pytest
from selenium import webdriver

# Fixture para el navegador
@pytest.fixture 
def navegador():
    # Preparo el navegador antes de cada test y lo cierra al terminar
    driver = webdriver.Chrome()
    # Maximizo la ventana para asegurar que todos los elementos sean visibles
    driver.maximize_window()
    # Uso yield para que el código después de esta línea se ejecute después de que el test haya terminado
    yield driver
    # Cierro el navegador después de cada test
    driver.quit()

import pytest
from selenium import webdriver

@pytest.fixture 
def navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Fixtures individuales para los tests de la pre-entrega
@pytest.fixture
def usuario():
    return "standard_user"

# fixture para la contraseña
@pytest.fixture
def password():
    return "secret_sauce"
