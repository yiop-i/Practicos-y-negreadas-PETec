import subprocess
subprocess.run("cls", shell=True)
reprobados=0
aprobados=0
notas=[]
try:
    alumnos=int(input("Ingrese la cantidad de alumnos en la comision: "))
    for i in range(alumnos):
        nota=float(input(f"Ingrese la nota del alumno {i+1}: "))
        notas.append(nota)
    for nota in notas:
        if nota>=6:
            aprobados=aprobados+1
        else:
            reprobados=reprobados+1

    print(f"Cantidad total de alumnos: {alumnos}")
    print(f"Cantidad de aprobados: {aprobados}")    
    print(f"Cantidad de desaprobados: {reprobados}")
except ValueError:
    print("Tenes que ingresar un tipo de dato valido")