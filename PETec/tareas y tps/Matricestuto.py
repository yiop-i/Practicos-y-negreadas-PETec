matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
#FORMAS DE IMPRIMIR UNA MATRIZ
#FORMA 1
for a in matriz:
    print(a)
    #Lo imprime como una lista, es decir, con corchetes y comas
#FORMA 2
for b in matriz:
    for element in b:
        print(element)
        #Lo imprime uno a bajo del otro, sin corchetes ni comas, pero tampoco parece matriz, solo es una columna
#FORMA 3
for c in matriz:
    for element in c:
        print(element, end=" ")
    print()
    #Lo imprime como una matriz, es decir, en filas y columnas, sin corchetes ni comas

#Matriz de forma manual
fila= int (input("Ingresa la cantidad de filas: "))
#Esta linea hace que el usuario ingrese la cantidad de filas que desea en la matriz
columna= int (input("Ingresa la cantidad de columnas: "))
#Esta linea hace que el usuario ingrese la cantidad de columnas que desea en la matriz
matrix = []
#Esta linea crea una lista vacía que se llenará con los elementos de la matriz
for fila_posicion in range(fila):
#Esta linea hace que el bucle se repita la cantidad de veces que el usuario ingresó en la variable fila
    fila = []
    #Esta linea crea una lista vacía que se llenará con los elementos de la fila
    for element in range(columna):
    #Esta linea hace que el bucle se repita la cantidad de veces que el usuario ingresó en la variable columna
        fila.append(int(input(f"Ingresa el elemento de la fila {fila_posicion + 1}, columna {element + 1}: ")))
        #Esta linea hace que el usuario ingrese el elemento de la fila y columna correspondiente y lo agregue a la lista fila
    matrix.append(fila)
    #Esta linea hace que la lista fila se agregue a la lista matrix, formando así la matriz completa
    
#Imprimir la matriz con los 3 métodos anteriores
print ("Metodo 1")
for a in matrix:
    print(a)
print ("Metodo 2")
for b in matrix:
    for element in b:
        print(element)
print ("Metodo 3")
for c in matrix:
    for element in c:
        print(element, end=" ")
    print()