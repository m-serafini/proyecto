# Pre-Entrega Proyecto de Automatización QA - SauceDemo
**Curso:** Automatizacion QA
**Autor:** Martin Nicolas Serafini
---

## Propósito del Proyecto
Este proyecto tiene como objetivo demostrar la capacidad de automatizar flujos básicos de navegación web utilizando **Selenium WebDriver** y **Python**. Se enfoca en la validación de procesos críticos en la plataforma [saucedemo.com](https://www.saucedemo.com), tales como el inicio de sesión seguro, la navegación por el catálogo de productos y la interacción funcional con el carrito de compras.

## Tecnologías Utilizadas
Para el desarrollo de esta solución se emplearon las siguientes herramientas:
- Lenguaje: Python 3.13.5
- Framework de Pruebas: Pytest
- Automatización del Navegador: Selenium WebDriver
- Reportes: Pytest-HTML
- Control de Versiones: Git y GitHub

### Casos Base (Pre-Entrega) 
Estos casos tienen prints detallados de cada paso realizado, esto sirve solo a los fines de muestra en estas pruebas individuales ya que si se escala la cantidad de casos puede generar confusión.
1. Login y Validación de Catálogo: Inicio de sesión exitoso y comprobación de elementos visuales, títulos y carga de productos.
2. Interacción con Carrito: Flujo completo de añadir producto, verificar incremento en el contador y validación de presencia en la página del carrito.

### Casos Extra: Login Incorrecto (Negativos)
El objetivo fue confirmar que el sitio impide el acceso y muestra el feedback correcto al usuario. Se utilizó Parametrización para cubrir las siguientes combinaciones de error:
* Usuario y contraseña vacíos.
* Usuario vacío con contraseña (correcta/incorrecta).
* Usuario válido con contraseña vacía.
* Usuario inválido con contraseña vacía.
* Usuario y contraseña no coincidentes (inválidos).
* Validación: En todos los casos se verifica el mensaje de error específico en el DOM: `h3[data-test="error"]`.

### Casos Extra: Login de Usuarios Aceptados
Validación de acceso para toda la suite de usuarios oficiales de SauceDemo:
* `standard_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user`.
* Caso Especial: Validación del mensaje de bloqueo para `locked_out_user`.

## Estructura del Proyecto
```text
automatizacion_qa_pre_entrega_martin_serafini/
├── tests/
│   └── conftest.py                # Configuración de Fixtures (WebDriver, Credenciales)
│   └── test_saucedemo.py      # Suite de pruebas (A, B y C)
├── utils/
│   └── funciones.py           # Funciones de interacción con el navegador
├── reports/
│   └── reporte.html           # Reporte de ejecución (Evidencia)
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación
```

## Arquitectura Técnica
* **Modularización:** Separación de funciones de interacción (`utils/`) y lógica de pruebas (`tests/`).
* **Fixtures de Pytest:** Gestión centralizada de la vida útil del WebDriver y credenciales de prueba en `conftest.py`.
* **Reportes:** Generación automática de reportes HTML detallados para auditoría de resultados.

## Instalación de Dependencias
Para configurar el entorno local y poder ejecutar las pruebas, sigue estos pasos:

1. Asegurarse de tener instalado **Python** en tu sistema.
2. Instalar las librerías necesarias 