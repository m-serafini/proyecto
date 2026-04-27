from calculadora.calculadora.utils import solicitar_numero, pedir_opcion
from calculadora.operaciones import sumar, restar , multiplicar, dividir

# solicito los numeros al usuario y la operacion a realizar
def main():
    opcion = pedir_opcion()
    num1 = solicitar_numero("primer")
    num2 = solicitar_numero("segundo")

    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
    elif opcion == "4":
        resultado = dividir(num1, num2)

    print(f"El resultado es: {resultado}")  
    
if __name__ == "__main__":
    main()