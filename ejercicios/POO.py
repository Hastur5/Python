class Perro:
    #Atributos de clase
    especie = "Mamifero"

    #El constructor
    def __init__(self, nombre, raza):
        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    
    #Método sin argumentos
    def ladrar(self):
        print("Este perro acaba de ladrar.")
    
    def caminar(self, pasos):
        print(f"este perro acaba de caminar {pasos}.")

perro1 = Perro("Skip", "Beagle")

# print(perro1.nombre)
# print(perro1.raza)

perro1.ladrar()
perro1.caminar(25)