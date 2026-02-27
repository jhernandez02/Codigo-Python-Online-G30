try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print('División:', a/b)
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except Exception as error:
    print('Ha ocurrido un error')
    print('Nombre Error:', type(error).__name__)
    print('Descripcion Error:', error)