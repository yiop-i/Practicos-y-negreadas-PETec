import subprocess
subprocess.run("cls", shell=True)
notastotales=0
notaalta=0  
notabaja=0
aprobado=0
desaprobado=0
alumnos=int(input("Ingrese la cantidad de alumnos: "))
for i in range(alumnos):
    nombre=str(input(f"Ingrese el nombre del alumno {i+1}: "))
    nota=float(input(f"Ingrese la nota del alumno {i+1}: "))
    
    notastotales=notastotales+nota

    if nota>=7:
        aprobado=aprobado+1
    else:
        desaprobado=desaprobado+1
        
        
    if nota>notaalta:
        notaalta=nota
    else:
        notabaja=nota
        
print(f"El promedio de notas es: {notastotales/alumnos}")
print(f"La nota más alta es: {notaalta}")
print(f"La nota más baja es: {notabaja}")
print(f"La cantidad de alumnos aprobados es: {aprobado}")
print(f"La cantidad de alumnos desaprobados es: {desaprobado}")