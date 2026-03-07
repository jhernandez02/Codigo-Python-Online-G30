class FiguraGeometrica:
    def __init__(self, nombre, lados):
        self.nombre = nombre # Atributo publico
        self.__lados = lados # Atributo privado
    def info(self):
        print('---- Info Figura ----')
        print(f'El {self.nombre} tiene {self.__lados} lados')
        if self.nombre=='Cuadrado':
            print('Lado:',self.lado)
        if self.nombre=='Triángulo':
            print('Base:',self.base)
            print('Altura:',self.altura)

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
        super().__init__('Cuadrado', 4)
    def area(self):
        area = self.lado**2
        print(f'Área del {self.nombre}: {area}')

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        super().__init__('Triángulo', 3)
    def area(self):
        area = (self.base * self.altura)/2
        print(f'Área del {self.nombre}: {area}')

figura1 = Cuadrado(7)
figura1.info()
figura1.area()

figura2 = Triangulo(5,4)
figura2.info()
figura2.area()