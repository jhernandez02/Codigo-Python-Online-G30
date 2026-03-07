'''
Desarrollar una aplicacion en POO, que halle el perímetro y área de un rectángulo.
Mediante un menú:
- Se debe solicitar el valor de la altura y ancho del rectángulo.
- Se puede mostrar el valor del perímetro o el área del rectángulo
'''

class Rectangulo:
    __base = None
    __altura = None

    def inicializar(self, base, altura):
        self.__base = base
        self.__altura = altura

    def getArea(self):
        if self.__base:
            return self.__base*self.__altura
        else:
            return "Se debe asignar la base y altura"
    
    def getPerimetro(self):
        if self.__base:
            return (self.__base+self.__altura)*2
        else:
            return "Se debe asignar la base y altura"

menu = True
rectangulo1 = Rectangulo()

while menu:
    print('--- Menú Opciones ---')
    print('1. Ingresar datos del rectángulo')
    print('2. Mostrar perímetro')
    print('3. Mostrar área')
    print('4. Salir')
    opcion = input('Ingresa una opción: ')
    print('-------------------------')
    if opcion=='1':
        base = int(input('Ingresar el valor de la base: '))
        altura = int(input('Ingresar el valor de la altura: '))
        rectangulo1.inicializar(base, altura)
    elif opcion=='2':
        print('Perímetro:', rectangulo1.getPerimetro())
    elif opcion=='3':
        print('Área:', rectangulo1.getArea())
    elif opcion=='4':
        menu = False
    else:
        print('Opción incorrecta')