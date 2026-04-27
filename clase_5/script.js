// Esperamos a que el DOM esté cargado para no tener errores de lectura
document.addEventListener('DOMContentLoaded', () => {
    const formulario = document.getElementById('calc-form');
    const displayResultado = document.getElementById('display-resultado');

    formulario.addEventListener('submit', (e) => {
        // Evitamos que la página se recargue (comportamiento por defecto del form)
        e.preventDefault();

        // 1. Obtener valores usando los IDs que Silvia y Matías pidieron
        const n1 = parseFloat(document.getElementById('num1').value);
        const n2 = parseFloat(document.getElementById('num2').value);
        
        // Buscamos cuál de los radios con name "operacion" está marcado
        const operacion = document.querySelector('input[name="operacion"]:checked').value;

        let resultado;

        // 2. Ejecutar la lógica (equivalente a tu operaciones.py)
        switch (operacion) {
            case 'sumar':
                resultado = n1 + n2;
                break;
            case 'restar':
                resultado = n1 - n2;
                break;
            case 'multiplicar':
                resultado = n1 * n2;
                break;
            case 'dividir':
                if (n2 === 0) {
                    resultado = "Error: Division por 0";
                } else {
                    resultado = n1 / n2;
                }
                break;
            default:
                resultado = "Opción inválida";
        }

        // 3. Mostrar el resultado en el contenedor de QA
        displayResultado.innerText = resultado;
    });
});