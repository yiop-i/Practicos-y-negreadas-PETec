"""
"Caso : Un club de basquet está buscando personas que cumplan con condiciones de edad y altura para su equipo, se requiere desarrollar
un módulo de un sistema que permita validar la búsqueda" 

1 ) Crea un repositorio en github llamado examen_funciones

2 ) Crea dos archivos : sistema.py y funciones.py

El archivo funciones.py debe contener una funcion llamada validador que reciba un parametro (lista) que contenga apellido (texto), año 
de nacimiento (número) y altura (en cm), la funcion debe determinar si es nacido desde el año 2010 inclusive o mas y si mide 180 cm o 
mas. La funcion debe devolver una lista que en el primer indice contenga verdadero o falso si es nacido desde el 2010 y el segundo indice 
contiene verdadero o falso si mide 180 cm o mas.

El archivo sistema.py debe llamar a la funcion validador y recibir el resultado para mostrar por pantalla si nacio en 2010 o mas debe mostrar 
por consola "Nacido en 2010 o mas" y si mide 180 cm o mas debe mostrar por consola "Cumple con la altura"
"""
def validador(jugador):
    resultado = []
    if jugador[1] >= 2010:
        resultado.append(True)
    else:
        resultado.append(False)
    
    if jugador[2] >= 180:
        resultado.append(True)
    else:
        resultado.append(False)
    
    return resultado