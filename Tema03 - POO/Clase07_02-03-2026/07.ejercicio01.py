'''
Desarrolla un programa que solicite el lado de un cuadrado.
El programa debe devoler el perímetro y área segun el valor del lado del cuadrado
'''

class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def getPerimetro(self):
        perimetro = self.lado * 4
        print('Perimetro: ', perimetro)
    
    def getArea(self):
        area = self.lado ** 2
        print('Área: ', area)

lado = int(input('Lado del cuadrado: '))
cuadrado = Cuadrado(lado)
cuadrado.getArea()
cuadrado.getPerimetro()