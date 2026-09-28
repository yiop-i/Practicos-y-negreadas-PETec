def mostrar_menu(menu,eleccion,nombre):
    print(nombre)
    print("Opciones:")
    for i, opcion in enumerate(menu):
        print(f"{i+1}: {opcion}")

    print(f"Opcion elegida: {eleccion}")