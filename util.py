def mostrar_menu(menu):
    print("Opciones:")
    for i, opcion in enumerate(menu):
        print(f"{i+1}: {opcion}")
        
    eleccion = input("Seleccione una opción: ")
    print(f"Opcion elegida: {eleccion}")