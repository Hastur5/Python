registrados = {"Mau" : "Fili"}

def registrar ():
    usuario = input("Elige tu nombre de usuario: ")
    contraseña = input("Crea tu contraseña para ingresar: ")
    if usuario in registrados:
         print("El nombre de usuario que seleccionaste ya está registrado.")
    else:
        registrados[usuario] = contraseña
        print(f"Se ha registrado tu usuario {usuario} y contraseña {contraseña} correctamente")

def login ():
    usuarioL = input("Ingresa tu usuario: ")
    contraseñaL = input("Ingresa tu contraseña: ")
    if usuarioL in registrados and registrados[usuarioL] == contraseñaL:
        print(f"Bienvenido {usuarioL} :)")
    else:
        print("Usuario o contraseña no registrados.")

def mostrar ():
     print(registrados)

contador = True

while contador:
        eleccion = int(input("Elige la opción que deseas realizar: 1. Registarte 2. Login 3. Mostrar datos guardados: "))

        if eleccion == 1:
            registrar()
        elif eleccion == 2:
            login()
        elif eleccion == 3:
            mostrar()
        else:
             print("Elige por favor uno de los números correspondientes.")

        respuesta = input("¿Deseas hacer algo más? Presione 's' para sí, cualquier otra tecla para salir: ").lower()
        if respuesta == "s":
            print("Continuemos")
        else:
            contador = False
