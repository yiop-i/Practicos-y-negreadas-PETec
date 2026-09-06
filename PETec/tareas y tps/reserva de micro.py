
colectivo= []
ocupado = "X"
disponible = "☻"
for fila in range(12):
   nueva_fila = []
   for columna in range(5):
       if columna == 2:
           nueva_fila.append("")
       else:
           nueva_fila.append(disponible)
   colectivo.append(nueva_fila)

def mostrar_colectivo():
    print("Columnas:  1    2         4    5")
    print ("--------------------------------")
    for i in range(len(colectivo)):
        if i <=8:
            print(f"Fila {i+1} : {colectivo[i]}")
        else:
            print(f"Fila {i+1}: {colectivo[i]}")
    print ("--------------------------------")
    
    
print("Sistema de reserva de asientos")
mostrar_colectivo()
print('ocupado = X\ndisponible = ☻')
eleccion=(input('Presione ENTER para reservar o escriba "S" para salir:'))
fila=int(input("Ingrese el número de fila, del 1 al 12: "))
filal=fila-1
columna=int(input("Ingrese el número de columna 1, 2, 4 o 5: "))
columnal=columna-1
if eleccion != "S":
    if columna == 3:
     print("La columna 3 es el pasillo. No se puede reservar.")
    elif colectivo[filal][columnal]== "X":
        print("La butaca ya está ocupada. Por favor, elija otra.")
    elif colectivo[filal][columnal]== "☻":
        colectivo[filal][columnal
                         ] = "X"
        print("Butaca reservada")
        mostrar_colectivo()
        

