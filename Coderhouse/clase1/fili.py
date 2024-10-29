""" 
Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia.
cadena = "acitametaM ,5.8 ,otipeP ordeP"
1. Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing: cadena[::-1]
2. Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno 
3. Extraer la nota y almacenarla en una variable llamada nota.
4. Extraer la materia y almacenarla en una variable llamada materia.
5.  Mostrar por pantalla la siguiente estructura, usando la concantenación de cadenas:
NOMBRE APELLIDO ha sacado un NOTA en MATERIA
"""

cadena = "sacitámetaM ,5.8 ,otipeP ordeP"
cadena_volteada = cadena[::-1]

print(cadena_volteada)

nombre = cadena_volteada[:12:1]
print(nombre)

nota = cadena_volteada[14:17:1]
print(nota)

materia = cadena_volteada[19::1]
print(materia)

print(nombre, "ha sacado ", nota, "en ", materia)

cadena = "Ay MI Pili"
print(cadena.lower())

expresiones=[
    False == True,
    10 >= 2*4,
    33/3 == 11,
    True > False,
    True *5 == 2.5*2
]

print(expresiones)

cadena23 = cadena[1]

print(cadena23)

lista = [1, 2, 56, 4]
nueva_lista = [x * 2 for x in lista]  # Multiplicar cada elemento por 2

print(nueva_lista)