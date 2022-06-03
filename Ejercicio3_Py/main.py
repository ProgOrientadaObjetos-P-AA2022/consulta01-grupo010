
class Estudiante:
    def __init__(self, nombre, cedula, calificacion):
        self.nombre = nombre
        self.cedula = cedula
        self.calificacion = calificacion

    def establecerNombre(self, valor):
        self.nombre = valor
    def obtenerNombre(self):
        return self.nombre

    def establecerCalificacion(self, valor):
        self.calificacion = valor
    def obtenerCalificacion(self):
        return str(self.calificacion)

    def establecerIdentificacion(self, valor):
        self.cedula = valor
    def obtenerIdentificacion(self):
        return str(self.cedula)

    def __str__(self):
        return 'Estudiante: ' + self.nombre + "\nCalificacion: " + str(self.calificacion) + '\nIdentificacion: ' + \
               str(self.cedula)

e1 = Estudiante('Kevin Barrazueta', '1105589426', 8.56)
print(e1)

