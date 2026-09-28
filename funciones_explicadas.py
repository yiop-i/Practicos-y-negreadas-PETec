def mostrarmenu():
    print ("1: ver productos")
    print ("2: Salir")
    
mostrarmenu()

def saludar(nombre):
    print ("hola", nombre)

nombre="juan"

nombre="jose"
saludar("Ana")
print (nombre)

def doble(numero):
    return numero*2

resultado=doble(5)

def calcular_precio(precio, cantidad):
    return precio*cantidad
