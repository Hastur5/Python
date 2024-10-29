class Cliente:
    def __init__(self, nombre, email, edad, intereses):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.intereses = intereses

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Edad: {self.edad}, Intereses: {', '.join(self.intereses)}"
