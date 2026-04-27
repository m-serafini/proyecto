# -------------------------------------------
# BLOQUE DE OPERACIONES MATEMÁTICAS:
# -------------------------------------------

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No es posible dividir por cero")
    return a / b
