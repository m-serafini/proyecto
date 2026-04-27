def solicitar_numero(orden):
    while True:
        try:
            valor = float(input(f"Ingresa el {orden} número: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor escribe un número.")

def pedir_opcion():
    print("\n==========CALCULADORA===========")
    print("\nOpciones: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elija la opción ( 1-4 )\n")

    opcion_valida = {
        "1":"Sumar",
        "2":"Restar",
        "3":"Multiplicar",
        "4":"Dividir"
    }
    try:
        opcion_valida[opcion]
    except KeyError:
        print("Opcion invalida, elgí entre 1 y 4")
    
    return opcion


