import subprocess
subprocess.run("cls", shell=True)
saldo = 100000
print("Indique el NÚMERO de la accion que desea realizar:\n🦕 1)Consultar saldo\n🦕 2)Depositar\n🦕 3)Retirar\n🦕 4)Salir")
accion = input("Accion:")
try:
    while accion != "4":
        if accion == "1":
            print(f"🦖 El saldo actual es de: {saldo}")
        elif accion == "2":
            deposito = int(input("Ingrese la cantidad que desea depositar: "))
            saldo += deposito
            print(f"🦖 Depositaste {deposito}$")
            print(f"🦖 Tu saldo actual es de: {saldo}")
        elif accion == "3":
            retirar = int(input("Ingrese la cantidad que desea retirar: "))
            if retirar > saldo:
                print("🦖 No puedes sacar una cantidad mayor a tu saldo")
            else:
                saldo -= retirar
                print(f"🦖 Retiraste {retirar}$")
                print(f"🦖 Tu saldo actual es de: {saldo}")
        else:
            print("🦖 Acción no válida")

        print("Indique la accion que desea realizar:\n🦕 1)Consultar saldo\n🦕 2)Depositar\n🦕 3)Retirar\n🦕 4)Salir")
        accion = input("Accion:")
        subprocess.run("cls", shell=True)
except ValueError:
    print("EL TIPO DE DATO INGRESADO NO ES VALIDO")