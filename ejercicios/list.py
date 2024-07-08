# Mutables: son objetos que pueden cambiar su valor.
# Crear Lista = array

countries = ['México', 'United States', 'India', 'Brazil']

print(countries[0])

print(countries[-4])

# Slicing / rebanada : nombre de la lista [start:stop]

print(countries[1:]) # = print(countries[1:4])

print(countries[:2])

# Operaciones y Métodos

countries.append('Canadá') # agregar un elemento

print(countries)

countries.insert(0, 'Yugoslavia') # agrega un elemento al inicio de la lista.

print(countries)

countries_2 = ['Perú', 'El Fili', 'Islas Skip']

print(countries + countries_2) # Concatenar dos listas

fili_lista = [countries, countries_2] # crear una lista de dos listas.

print(fili_lista)

countries.remove('Canadá')

print(countries)

countries.pop(0)

print(countries)

del countries [1]

print(countries)

numbers = [2, 3, 9.9, 9.1, 6, 49492, 47473]

print(numbers)

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

numbers[0] = 0

print(numbers)

lista_del_pili = countries.copy()

print(lista_del_pili)

lista_skip = countries[0:2] # copia segmentos (slice)

print(lista_skip)