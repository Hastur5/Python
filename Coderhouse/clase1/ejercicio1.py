"""
1. Números y cadenas de caracteres:
Declara dos variables numéricas y súmalas. Declara una variable de texto y concaténala con otro string.

2. Listas y tuplas:
Crea una lista con al menos 5 elementos, añade un nuevo elemento y luego elimina el segundo. Crea una tupla y muestra su primer valor.

3.Conjuntos y diccionarios:
Crea un conjunto con valores repetidos y muestra el conjunto único. Crea un diccionario con al menos 3 pares clave-valor y accede a uno de ellos.

4.Operadores y sentencias de control:
Escribe un programa que compare dos números y te diga cuál es mayor usando operadores relacionales.

5.Ciclos:
Haz un bucle for que recorra una lista de 5 elementos y los imprima. Luego, haz un bucle while que sume números del 1 al 10.

6.Funciones:
Define una función que reciba dos parámetros y retorne su suma. Luego, llámala con dos números y muestra el resultado.

fili = 8
skip = 12

tomris = "Vivo en Turquía,"
yo = " hermano."

print(fili + skip)
print(tomris + yo)

#***************

perros = ["Chapo", "Skip", "Fili", "Volcán", "Chronito"]

perros.append("Estrellita")
perros.pop(1)
perros.append("Skippie")

bills = ("Josh Allen", 4, "James Cook", 85)

print(perros)

print(bills[0])

#********

areWeStillFriends = {"i", "got", "to", "knoooow", "oooo", "oooo"}

print(areWeStillFriends)

yop = {
    "nombre" : "mau", 
    "edad" : "31", 
    "género" : "masculino"
    }

print(yop["nombre"])

"""

#**********

"""

import random

def comparacion_de_numeros():

    while True:
        valor = random.randint(1,5)
        numero = int(input("Introduce el valor entre 1 y 5 a comparar: "))

        if numero >=  valor:
            print(f"Tu número es igual o más grande, hermane : {numero}")
            break 
        else:
            print(f"Intenta de nuevo, hermano")
            print(f"El número es: {valor}")

comparacion_de_numeros()

"""

#**********
"""
for perro in perros:
    print(perro)

cantidad = 5

Crea un programa que calcule la nota final de un estudiante basado en tres notas, cada una con un peso diferente:
nota_1 vale el 20%, nota_2 vale el 30%, y nota_3 el 50%.
calificacion_1 = float(input("Primera calificación: "))* 0.2
calificacion_2 = float(input("Segunda calificación: "))* 0.3
calificacion_3 = float(input("Tercera calificación: "))* 0.5

final = calificacion_1 + calificacion_2 + calificacion_3

print(f"Tu calificación es de: {final}")



1. Cálculos básicos:
    Declara dos variables numéricas e imprime la suma, resta, multiplicación y división entre ellas. Luego, pide estos valores al usuario utilizando input().


valor_1 = float(input("¿Qué valor buscas operar? "))
valor_2 = float(input("¿Qué valor buscas operar? "))

print(valor_1 + valor_2)
print(valor_1 - valor_2)
print(valor_1 / valor_2)
print(valor_1 * valor_2)


2. Manipulación de cadenas:

    Escribe un programa que solicite una cadena de texto al usuario. Muestra los primeros 3 caracteres, los últimos 3, y concaténalos. Convierte la cadena a mayúsculas y minúsculas y muestra su longitud.


frase = input("Ingresa la frase que deseas fusionar ")

print(frase[:3] + frase [-3:])

"""

