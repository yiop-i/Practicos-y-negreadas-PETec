from util import mostrar_menu
nombre=(input("Ingrese el nombre de su menú:"))
print("Ingrese los valores de su lista de 4 opciones: ")
menu = []
for i in range(4):
    opcion = input(f"Ingrese la opción {i+1}: ")
    menu.append(opcion)

eleccion = input("Seleccione una opción: ")
mostrar_menu(menu, eleccion, nombre)