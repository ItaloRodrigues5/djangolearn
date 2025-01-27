class Forma():

    def area(self):
        pass

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self, pi):
        return pi * self.raio ** 2

#Instâncias
quadrado = Quadrado(2)
print('Área do Quadrado: {}'.format(quadrado.area()))

quadrado2 = Quadrado(5)
print('Área do Quadrado: {}'.format(quadrado2.area()))

circulo = Circulo(4)
print('Área da Circunferência: {}'.format(circulo.area(3.14)))

# circulo2 = Circulo(6)
# print('Área da Circunferência: {}'.format(circulo2.area()))