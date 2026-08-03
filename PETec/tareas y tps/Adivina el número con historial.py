import subprocess
subprocess.run("cls", shell=True)
import random
aleatorio=random.randint(1,100)
intentos=0
numerosquetiro=[]
while intentos!=10:
    try:
        numero=int(input("Adivina el numero entre 1 y 100: "))
        intentos=intentos+1
        numerosquetiro.append(numero)
        if numero!=aleatorio:
            print("Aun no lo adivinas")
        else:
            print(f"Felicitaciones, adivinaste el numero en {intentos} intentos")
            print(f"Los numeros que intentaste son: {numerosquetiro}")
        if intentos==10:
            print(f"Se te acabaron los intentos, el numero era {aleatorio}")
            break
    except ValueError:
        print("Error: tipo de dato no valido")