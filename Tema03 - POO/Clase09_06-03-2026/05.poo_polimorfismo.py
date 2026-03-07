'''
El polimosfismo permite usar el mismo método en diferentes clases,
pero que cada clase hija, lo implemente de manera distinta
'''

class FiguraGeometrica:
    def __init__(self, nombre, base, altura):
        self.nombre = nombre
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

class Rectangulo(FiguraGeometrica):
    pass

class Cuadrado(FiguraGeometrica):
    pass

class Triangulo(FiguraGeometrica):
    # Aplicamos polimorfismo sobreescribiendo el método
    def area(self):
        # Accedemos al area de la clase FiguraGeometrica (padre)
        return super().area() / 2

figura1 = Rectangulo('Rectángulo', 20, 10)
print(f"Área del {figura1.nombre}: {figura1.area()}")

figura2 = Triangulo('Triangulo', 20, 10)
print(f"Área del {figura2.nombre}: {figura2.area()}")