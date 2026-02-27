'''
raise es usado para lanzar una excepcion de forma manual
'''
try:
    raise ValueError('Este es un mensaje de error personalizado')
except Exception as error:
    print('Ocurrió un error')
    print('Nombre Error:', type(error).__name__)
    print('Descripcion Error:', error)