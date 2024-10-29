"""
Objetivo
Practicar el concepto de funciones. Preparar la parte lógica para el registro de usuarios.

Consigna

Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.
Formato

El proyecto debe compartirse utilizando Colab bajo el nombre “Primera pre-entrega+Apellido”.
Se debe entregar
Se debe entregar todo el programa.

Sugerencias
El formato de registro es: Nombre de usuario y Contraseña.
Utilizar una función para almacenar la información y otra función para mostrar la información.
Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

"""

registros = {"mau" : "fili"}

def registrar():
    while True:
        usuario = input("Elige tu nombre de usuario: ")
        contraseña = input("Crea tu contraseña para ingresar: ")
        if usuario in registros:
            print("El nombre de usuario que seleccionaste ya está registrado.")
        else:
            registros[usuario] = contraseña
            print(f"Se ha registrado tu usuario {usuario} y contraseña {contraseña} correctamente")
            break

def login ():
    usuarioL = input("Ingresa tu usuario: ")
    contraseñaL = input("Ingresa tu contraseña: ")
    if usuarioL in registros and registros[usuarioL] == contraseñaL:
        print(f"Bienvenido {usuarioL} :)")
    else:
        print("Usuario o contraseña no registrados.")

def mostrar ():
        print(registros)

menu = True

while menu:
    try:
        eleccion = int(input("Elige la opción que deseas realizar: 1. Registarte 2. Login 3. Mostrar datos guardados o 0. Para salir: "))

        if eleccion == 1:
            registrar()
        elif eleccion == 2:
            login()
        elif eleccion == 3:
            mostrar()
        elif eleccion == 0:
            print("Adiós :)")
            break
        else:
            print("Elige por favor uno de los números correspondientes.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

        respuesta = input("¿Deseas hacer algo más? Presione 's' para sí, cualquier otra tecla para salir: ").lower()
        if respuesta == "s":
            print("Continuemos")
        else:
            menu = False