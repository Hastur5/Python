# def dividir(a, b):
#     if b == 0:
#         return None
#     return a / b

# print(dividir(34,0))
# print(dividir(7,2))


# def dividir_2(a,b):
#     try:
#         resultado = a/b
#     except Exception as error:
#         print("La operación no se pudo completar porque: ", error)
#         resultado = None
#     return resultado

# print(dividir_2(34,0))
# print(dividir_2(7,2))


# def dividir_2(a,b):
#     try:

#         resultado = c

#         return a/b
#     except ZeroDivisionError as error:
#         print("La operación no se pudo completar porque: ", error)
#     except TypeError:
#         print("Hubo un error en los tipos de dato")
#     except NameError:
#         print("Variable inexistente")
#     except Exception as e:
#         print("La operación no se pudo completar porque: ", e)

# print(dividir_2(34,(5,0)))
# print(dividir_2(7,2))


# def anio_bisiesto():
#     try:
#         anio = int(input("Introduce el año: "))
#     except: 
#         print("No se ingresó un dato válido.")
#         return None

#     if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
#         print(f"el año {anio} es bisiesto")
#     else:
#         print(f"El año {anio} no es bisiesto")

# anio_bisiesto()


# def anio_bisiesto():
#     try:
#         anio = int(input("Ingrese el año: "))
#     except:
#         print("No se ingresó el dato válido")
#         return None
#     else:
#         print("El dato es válido")
#     finally:
#         print("Esta línea se debería ejecutar siempre")

#     if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
#         print(f"el año {anio} es bisiesto")
#     else:
#         print(f"El año {anio} no es bisiesto")

# anio_bisiesto()
