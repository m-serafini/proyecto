# Tabla de Selectores Robustos - Portal de Perfiles
---

Esta tabla contiene los selectores optimizados para la automatización de pruebas, priorizando la independencia del layout y la estabilidad ante rediseños visuales.

| Elemento | Selector CSS | XPath Relativo | Razón de la elección |
| :--- | :--- | :--- | :--- |
| **Usuario** | `#user-name` | `//input[@id='user-name']` | Uso de ID único. Es el selector más rápido y menos propenso a cambios. |
| **Contraseña** | `#password` | `//input[@id='password']` | Uso de ID único. Garantiza que el campo se encuentre incluso si se mueve de sección. |
| **Botón Login** | `#login-button` | `//input[@type='submit']` | El ID asegura la puntería; el XPath por tipo de atributo protege contra cambios en el texto del botón. |

---


