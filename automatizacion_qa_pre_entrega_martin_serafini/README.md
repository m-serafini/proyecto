# Pre-Entrega Proyecto de Automatización QA - SauceDemo
**Autor:** Martin Nicolas Serafini
---

## Propósito del Proyecto
Este proyecto tiene como objetivo demostrar la capacidad de automatizar flujos básicos de navegación web utilizando **Selenium WebDriver** y **Python**. Se enfoca en la validación de procesos críticos en la plataforma [saucedemo.com](https://www.saucedemo.com), tales como el inicio de sesión seguro, la navegación por el catálogo de productos y la interacción funcional con el carrito de compras.

## Tecnologías Utilizadas
Para el desarrollo de esta solución se emplearon las siguientes herramientas:
- **Lenguaje:** Python 3.13.5
- **Framework de Pruebas:** Pytest
- **Automatización del Navegador:** Selenium WebDriver
- **Reportes:** Pytest-HTML
- **Control de Versiones:** Git y GitHub

## Estructura del Proyecto
El código se organiza de manera modular para garantizar la legibilidad y la independencia de las pruebas:
- `tests/`: Contiene los scripts de prueba (`test_saucedemo.py`).
- `utils/`: Contiene las funciones auxiliares y lógica de interacción (`funciones.py`).
- `reports/`: Carpeta donde se almacenan los reportes de ejecución generados automáticamente.

## Instalación de Dependencias
Para configurar el entorno local y poder ejecutar las pruebas, sigue estos pasos:

1. Asegúrate de tener instalado **Python** en tu sistema.
2. Instala las librerías necesarias ejecutando el siguiente comando en la terminal:
   ```bash
   pip install selenium pytest pytest-html