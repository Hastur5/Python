n = int(input("number: "))
# Se tiene que especificar qué el input reciba un entero. Si no, lo toma como string.
if n > 0:  
    print("n is positive")
elif n < 0:
    print("n is negative")
else:   
    print("n is zero")

countries = ['Mexico', 'United States', 'India', 'Brazil']

m = input('Introduce tu país: ')

title_name = m.title()

if title_name in countries:
    print('Acertaste un país')
else:
    print("Lo siento")