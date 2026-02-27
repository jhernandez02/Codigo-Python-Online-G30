'''
Las excepciones es una forma de controlar el comportamiento
de un programa cuando se produce un error.
'''
a,b = 4,0
# ZeroDivisionError: division by zero
# print(a/b)

c = input('Ingresa un número: ')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a+c)