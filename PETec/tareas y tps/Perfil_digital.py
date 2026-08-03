import subprocess
subprocess.run("cls", shell=True)
print("♡✿ Vamos a crear tu perfil digital ⁠✿⁠♡⁠⁠")
#Le pide los datos a quien corra el codigo
try:
    nombre = str(input("ingresa tu nombre:\n "))
    edad = int(input("ingresa tu edad: "))
    altura = float(input("ingresa tu altura exacta (en metros):\n "))
    estudiante = bool(input("¿Eres estudiante? (si/no):\n "))
    #Saca un aproximado del año de nacimiento
    nacimiento = 2026-edad
    #Si es mayor de 16 pide la red social favorita
    if edad>16:
        social =  str(input("Ingrese red social favorita: \n "))
    else:
        social = ""
    if social == "":
        #Muestra el perfil digital sin red social
        print(f"🪼 Tu perfil digital es:\n🦭 Nombre: {nombre}\n🦭 Edad: {edad}\n🦭 Altura: {altura} m\n🦭 Estudiante: {estudiante}\n🦭 Año de nacimiento aproximado: {nacimiento}")
    else:
        #Muestra el perfil digital con red social
        print(f"🪼 Tu perfil digital es:\n🦭 Nombre: {nombre}\n🦭 Edad: {edad}\n🦭 Altura: {altura} m\n🦭 Estudiante: {estudiante}\n🦭 Año de nacimiento aproximado: {nacimiento}\n🦭 Red social favorita: {social}")
  #muestra el tipo de dato de las variables
    print(type(nombre))
    print(type(edad))
    print(type(altura))
    print(type(estudiante))
except ValueError:
    print("❌ EL VALOR INGRESADO NO ES VÁLIDO ❌")
    exit()      
