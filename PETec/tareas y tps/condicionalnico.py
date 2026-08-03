#condicional
# si.........
num=4
#operadores logicos
#
if num==4:
    print("4 es igual a 4")
elif num==5:
    print("segunda condicion correcta")
elif num==6:
    print("tercera condicion correcta")
elif num==7:
    print("cuarta condicion correcta")
else:
    print("ninguna condicion es correcta")
    
if num>1 and num<5:
    print("4 es igual a 4")
elif num==5:
    print("segunda condicion correcta")
elif num==6:
    print("tercera condicion correcta")
elif num==7:
    print("cuarta condicion correcta")
else:
    print("ninguna condicion es correcta")
    
#bucles iterativos
condicion = True
while condicion:
    print("BUCLES")
    opcion = (input("¿Deseas seguir? "))
    if opcion == "si":
        condicion = False