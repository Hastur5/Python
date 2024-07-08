lista = [64, 34, 25, 12, 22, 11, 90]

n = len(lista)

# Bucle externo que recorre todos los elementos
for i in range(n):
    # Bandera para optimizar y salir del bucle si no se hicieron intercambios
    intercambio = False
    # Bucle interno para comparar los elementos adyacentes
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]  # Intercambio usando asignación múltiple en Python
            intercambio = True

    # Si no se hizo ningún intercambio en el bucle interno, significa que la lista ya está ordenada
    if not intercambio:
        break

print(lista)





