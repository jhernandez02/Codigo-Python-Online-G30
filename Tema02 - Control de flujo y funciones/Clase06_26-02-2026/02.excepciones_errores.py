'''
Manejamos los errores que puedan ocurrir
dentro del bloque try
'''

try:
    a = int(input('Número: '))
    print(a**2)
except ValueError:
    print('Tipo de dato inválido')

print('----------------------------------')

try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print('División:', a/b)
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except ValueError:
    print('Valores inválidos')

print('----------------------------------')

lista = ['uva','pera','fresa']
try:
    print(lista)
    index = int(input('Indique el índice: '))
    print(lista[index])
# IndexError: list index out of range
except IndexError:
    print('Índice inválido')
