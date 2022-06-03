
class Persona():
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

    def nombre(self, valor):
        self.edad = valor

    def edad(self):
        return self.edad

    def nombre(self, valor):
        self.nombre = valor

    def edad(self):
        return self.nombre

    def __str__(self):
        return 'Nombre: ' + str(self.nombre) + ' Edad: ' + str(self.edad)
p1 = Persona(18, 'Kevin Barrazaueta')
p2 = Persona(17, 'Carolina de los Angeles')
print(p1)
print(p2)
