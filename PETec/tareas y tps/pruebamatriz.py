from array import array

# Nombres para identificar las filas y las columnas
ciudades = ["Mendoza", "San Rafael", "Malargüe"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Matriz: cada array representa una fila
temperaturas = [
    array('f', [23.5, 25.2, 24.8, 27.1, 28.0]),
    array('f', [21.0, 23.4, 22.9, 25.0, 26.2]),
    array('f', [14.8, 16.5, 15.9, 18.2, 19.0])
]

# Mostrar todas las temperaturas
print("TEMPERATURAS REGISTRADAS")

for fila, datos_ciudad in enumerate(temperaturas):
    print(f"\n{ciudades[fila]}")

    for columna, temperatura in enumerate(datos_ciudad):
        print(f"{dias[columna]}: {temperatura:.1f} °C")

# Calcular el promedio de cada ciudad
print("\nPROMEDIOS")

for fila, datos_ciudad in enumerate(temperaturas):
    promedio = sum(datos_ciudad) / len(datos_ciudad)
    print(f"{ciudades[fila]}: {promedio:.1f} °C")

# Buscar la temperatura más alta
maxima = temperaturas[0][0]
fila_maxima = 0
columna_maxima = 0

for fila in range(len(temperaturas)):
    for columna in range(len(temperaturas[fila])):
        temperatura = temperaturas[fila][columna]

        if temperatura > maxima:
            maxima = temperatura
            fila_maxima = fila
            columna_maxima = columna

# Mostrar dónde se encontró la temperatura más alta
print("\nTEMPERATURA MÁS ALTA")
print(f"Valor: {maxima:.1f} °C")
print(f"Ciudad: {ciudades[fila_maxima]}")
print(f"Día: {dias[columna_maxima]}")