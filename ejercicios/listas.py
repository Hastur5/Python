lista_1 = ["Fili", "Skip", 12]
lista_2 = ["Eón", 0, 5]

lista_1.append(456789)
lista_1.append("hola mundo")

lista_2.append("hola y adiós")
lista_2.append(5555)

print(lista_1)
print(lista_2)

lista_3 = lista_1[:-1]
lista_4 = lista_2[1:-1]

print(lista_3)
print(lista_4)