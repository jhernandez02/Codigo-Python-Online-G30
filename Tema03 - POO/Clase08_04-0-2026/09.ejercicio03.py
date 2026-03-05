'''
Desarrollar una calculadora con las operaciones básica: suma, resta, división y multiplicación
Solicitar 2 números.
Implementar un menú
'''

class Calculadora:
    __num1 = None
    __num2 = None

    def inicializar(self, num1,num2):
        self.__num1 = num1
        self.__num2 = num2

    def sumar(self):
        return self.__num1 + self.__num2
    
    def restar(self):
        return self.__num1 - self.__num2
    
    def dividir(self):
        return self.__num1 / self.__num2
    
    def multiplicar(self):
        return self.__num1 * self.__num2

menu = True
calculadora1 = Calculadora()

while menu:
    print('--- Menú Opciones ---')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Salir')
    opcion = input('Ingresa una opción: ')
    print('-------------------------')
    if opcion=='1' or opcion=='2' or opcion=='3' or opcion=='4':
        num1 = int(input('Ingresar el valor de num1: '))
        num2 = int(input('Ingresar el valor de num2: '))
    calculadora1.inicializar(num1, num2)
    if opcion=='1':
        print('Suma:', calculadora1.sumar())
    elif opcion=='2':
        print('Resta:', calculadora1.restar())
    elif opcion=='3':
        print('Multiplicación:', calculadora1.multiplicar())
    elif opcion=='4':
        print('División:', calculadora1.dividir())
    elif opcion=='5':
        menu = False
    else:
        print('Opción incorrecta')