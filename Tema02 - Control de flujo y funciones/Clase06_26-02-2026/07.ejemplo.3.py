try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    resultado = a/b
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except ValueError:
    print('Valores inválidos')
else:
    print('Resultado:',resultado)
