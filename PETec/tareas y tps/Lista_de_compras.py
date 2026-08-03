import subprocess
subprocess.run("cls", shell=True)
productos = []
productoname=str(input("Ingrese el nombre del producto (o 'fin' para terminar): "))
while productoname!="fin":
    productos.append(productoname)
    productoname=str(input("Ingrese el nombre del producto (o 'fin' para terminar): "))

cantidad = len(productos)
print(f"Se ingresaron {cantidad} productos.")
for producto in productos:
    print(producto)

if cantidad == 0:
    print("La lista quedó vacía.")   