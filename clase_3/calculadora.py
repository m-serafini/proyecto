
# BLOQUE DE OPERACIONES MATEMÁTICAS:


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # Devuelvo un mensaje de error específico que puedo validar en mis pruebas
        return "Error: División por cero"


# BLOQUE DE INTERFAZ Y VALIDACIÓN:

def solicitar_numero(orden):
    while True:
        try:
            valor = float(input(f"Ingresa el {orden} número: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor escribe un número.")

def ejecutar_calculadora():
    print("--- Calculadora para Testing Automatizado ---")
    
    # Valido mis entradas individualmente
    n1 = solicitar_numero("primer")
    n2 = solicitar_numero("segundo")

    # Bucle para asegurar que la opción sea válida
    while True:
        print("\nOperaciones: 1. Sumar | 2. Restar | 3. Multiplicar | 4. Dividir")
        opcion = input("Selecciona una opción (1-4): ")
        if opcion in ['1', '2', '3', '4']:
            break
        else:
            print("Error. Elegir un número del 1 al 4.")

    # Ejecuto la lógica basada en mi elección
    if opcion == '1':
        resultado = sumar(n1, n2)
        simbolo = "+"
    elif opcion == '2':
        resultado = restar(n1, n2)
        simbolo = "-"
    elif opcion == '3':
        resultado = multiplicar(n1, n2)
        simbolo = "*"
    elif opcion == '4':
        resultado = dividir(n1, n2)
        simbolo = "/"

    # Imprimo el resultado final
    print(f"\nResultado final: {n1} {simbolo} {n2} = {resultado}")


#EJECUCIÓN:
if __name__ == "__main__":
    ejecutar_calculadora()