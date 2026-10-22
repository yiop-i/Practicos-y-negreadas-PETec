"""
"Caso : Un club de basquet está buscando personas que cumplan con condiciones de edad y altura para su equipo, se requiere 
desarrollar un módulo de un sistema que permita validar la búsqueda" 

1 ) Crea un repositorio en github llamado examen_funciones

2 ) Crea dos archivos : sistema.py y funciones.py

El archivo funciones.py debe contener una funcion llamada validador que reciba un parametro (lista) que contenga apellido (texto), año de 
nacimiento (número) y altura (en cm), la funcion debe determinar si es nacido desde el año 2010 inclusive o mas y si mide 180 cm o 
mas. La funcion debe devolver una lista que en el primer indice contenga verdadero o falso si es nacido desde el 2010 y el segundo indice 
contiene verdadero o falso si mide 180 cm o mas.

El archivo sistema.py debe llamar a la funcion validador y recibir el resultado para mostrar por pantalla si nacio en 2010 o mas debe 
mostrar por consola "Nacido en 2010 o mas" y si mide 180 cm o mas debe mostrar por consola "Cumple con la altura"
"""
import funciones
print("Bienvenido al sistema de validación del club de basquet")
print("Se requiere ingresar los siguientes datos para validar si cumple con las condiciones de edad y altura")
jugador=[]
apellido=input("Ingrese su apellido: ")
jugador.append(apellido)
nacimiento=int(input("Ingrese su año de nacimiento: "))
jugador.append(nacimiento)
altura=int(input("Ingrese su altura en cm: "))
jugador.append(altura)
resultado = funciones.validador(jugador)
if resultado[0]:
    print("Nacido en 2010 o mas")
else:
    print("No cumple con la edad requerida")
if resultado[1]:
    print("Cumple con la altura")
else:
    print("No cumple con la altura requerida")
