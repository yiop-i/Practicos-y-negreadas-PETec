notas = []

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos en la comisión: "))

for i in range(cantidad_alumnos): # type: ignore
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    notas.append(nota)

aprobados = 0
reprobados = 0

for nota in notas:
    if nota >= 6:
        aprobados += 1
    else:
        reprobados += 1

print(f"Cantidad total de alumnos: {cantidad_alumnos}") # type: ignore
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de desaprobados: {reprobados}")
