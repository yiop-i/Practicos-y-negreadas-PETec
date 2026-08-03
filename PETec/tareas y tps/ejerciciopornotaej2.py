productos = []

while True:
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    productos.append(nombre)

cantidad = len(productos)
print(f"Se ingresaron {cantidad} productos.")

if cantidad == 0:
    print("La lista quedó vacía.")
else:
    print("Lista de productos:")
    for producto in productos:
        print(producto)
