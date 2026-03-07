'''
Desarrollar una aplicacion en POO, que halle el perímetro y área de un cuadrado.
Mediante un menú:
- Se debe solicitar el valor del lado del cuadrado.
- Se puede mostrar el valor del perímetro o el área del cuadrado
'''

class Cuadrado:
    __lado = None

    def setLado(self, lado):
        self.__lado = lado

    def getArea(self):
        if self.__lado:
            return self.__lado**2
        else:
            return "Se debe asignar un valor para lado"
    
    def getPerimetro(self):
        if self.__lado:
            return self.__lado*4
        else:
            return "Se debe asignar un valor para lado"

menu = True
cuadrado1 = Cuadrado()

while menu:
    print('--- Menú Opciones ---')
    print('1. Ingresar datos del cuadrado')
    print('2. Mostrar perímetro')
    print('3. Mostrar área')
    print('4. Salir')
    opcion = input('Ingresa una opción: ')
    print('-------------------------')
    if opcion=='1':
        lado = int(input('Ingresar el valor del lado: '))
        cuadrado1.setLado(lado)
    elif opcion=='2':
        print('Perímetro:', cuadrado1.getPerimetro())
    elif opcion=='3':
        print('Área:', cuadrado1.getArea())
    elif opcion=='4':
        menu = False
    else:
        print('Opción incorrecta')