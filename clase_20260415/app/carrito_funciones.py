
#funcion para agregar al carrito un producto y su precio, el carrito es una lista de diccionarios con nombre y precio del producto  
def agregar_producto(carrito, producto):
    carrito.append(producto)
    #print(f"Producto '{producto}' agregado al carrito.")
    return carrito

def eliminar_producto(carrito, producto):
    if producto in carrito:
        carrito.remove(producto)
        #print(f"Producto '{producto}' eliminado del carrito.")
    else:
        print(f"Producto '{producto}' no encontrado en el carrito.")
    return carrito      

def mostrar_carrito(carrito):    
    if carrito:
        print("Productos en el carrito:")     
        for producto in carrito:            
            print(f"- {producto}")
    else:
        print("El carrito está vacío.")
        
def calcular_total(carrito, precios):
    total = 0
    for producto in carrito:
        if producto in precios:
            total += precios[producto]
        else:
            print(f"Precio no encontrado para el producto '{producto}'.")
    return total

