# Los diccionarios sirven para guardar elementos. Viene siendo equivalente a objetos en JS.
mi_fili = { 'nombre' : 'Filip', 'edad' : 6 }

print(mi_fili)

print(mi_fili['nombre'])

print(mi_fili.keys())

print(mi_fili.values())

print(mi_fili.items())

mi_fili['apodo'] = 'El pili'

print(mi_fili)

dopple_fili = mi_fili.copy()

print(dopple_fili)

mi_fili.update({'apodo' : 'El Fili', 'color' : ['negro', 'blanco']})

print(mi_fili)

mi_fili.pop('color')

print(mi_fili)

del mi_fili ['apodo']

print(mi_fili)

mi_fili.clear()

print(mi_fili)
