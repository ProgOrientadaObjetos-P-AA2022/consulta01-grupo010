
class Multiplicacion:

    def __init__(self,  v1, v2):
        self.valor1 = v1
        self.valor2 = v2
    def valor1(self, valor):
        self.valor1 = valor

    def valor1(self):
        return self.valor1

    def valor2(self, valor):
        self.valor2 = valor

    def valor2(self):
        return self.valor2
    def calculo(self):
        return self.valor1 * self.valor2
m1 = Multiplicacion(7, 111)
print(m1.calculo())
m2 = Multiplicacion(12, 7)
print(m2.calculo())
m3 = Multiplicacion(9, 18)
print(m3.calculo())