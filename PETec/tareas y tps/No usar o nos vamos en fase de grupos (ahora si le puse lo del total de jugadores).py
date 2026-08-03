# Examen de fundamentos en Python.

# Lionel Scaloni te está pidiendo ayuda para manejar los datos de los jugadores en el mundial y así optimizar las jugadas.
# Para ello necesita un sistema que permita cargar los datos de los jugadores y mostrarlos.
# EL DESEMPEÑO DE LA SELECCIÓN ARGENTINA EN EL MUNDIAL DEPENDE DE QUÉ TAN BIEN SEA RESUELTO EL SIGUIENTE EXAMEN.

# El sistema debe mostrar un menú que permita:
#	1) Cargar jugador, goles marcados por el jugador y posición (en esta opción se cargan las tres cosas al mismo tiempo).
#	2) Mostrar todos los jugadores cargados con sus goles marcados y posición.
#	3) Mostrar la cantidad de jugadores total utilizando el comando len()
#	4) Salir

# Condiciones:
#	Si la posición del jugador es "arquero", al momento de mostrar todos los jugadores NO se mostrará la cantidad de goles marcada.
#	Esto significa que si el programa muestra "Goles marcados: 0", es incorrecto. La línea de goles marcados no deberá aparecer.
#	Si el nombre del jugador es "Lionel Messi", el programa debe imprimir "Elegiste al GOAT".
#	Conviene manejar tres listas distintas para manipular los datos en vez de meterlas todas a la misma lista.
#	El menú debe estar en un bulce while() 
#	El código debe comentar brevemente qué va a hacer cada parte, con las palabras del alumno.
#	Al cargar un jugador, si se ingresa un valor que provoque un error, debe ser manejado con try / except.


#limpiador de terminales
import subprocess
subprocess.run("cls", shell=True)
#listas vacias
jugadores = []
goles = []
posiciones = []     
cantidadjugadores=0
opcion=str(input("En el siguiente menu debera de cargar distintos datos de los jugadores, en caso de querer terminar ingrese la palabra 'terminar': "))
#mintras que no se ponga terminar te tira el menu de los jugadores y no se que 
while opcion!="terminar":
    try:
        nombre=str(input("Ingrese el nombre del jugador: "))
        if nombre=="Lionel Messi":
            print("Elegiste al GOAT")
        jugadores.append(nombre)
        gol=int(input("Ingrese la cantidad de goles marcados por el jugador: "))
        goles.append(gol)
        posicion=str(input("Ingrese la posición del jugador: "))
        posiciones.append(posicion)
        #puse lo del total de jugadores a ultimo momento porque me olvide, que tiene?
        cantidadjugadores=cantidadjugadores+1
    #si sos medio peculiar y no sabes ingesar datos te tira error y te termina el programa, por chistoso
    except ValueError:
        print("Error, ingrese un tipo de dato valido")
        exit()
    opcion=str(input("En caso de querer finalizar ingrese la palabra 'terminar'"))
#recorre las listas y te tira los datos en pantalla
for i in range(len(jugadores)):
    if posiciones[i].lower() == "arquero":
    #si es arquero no muestra los goles, si el pobre hizo gol de arco a arco no lo reconocen, que triste
        print(f"Jugador: {jugadores[i]} \nPosición: {posiciones[i]}")
    else:
        print(f"Jugador: {jugadores[i]} \nGoles: {goles[i]} \nPosición: {posiciones[i]}")
        
print(f"La cantidad total de jugadores es: {cantidadjugadores}")