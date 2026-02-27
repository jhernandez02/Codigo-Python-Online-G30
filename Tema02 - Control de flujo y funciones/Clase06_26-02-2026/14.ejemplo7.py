class EdadInvalidaError(Exception):
    pass

def verificarEdad(edad):
    if edad<0:
        raise EdadInvalidaError('La edad no puede ser negativa')
    print('Edad válida')

try:
    verificarEdad(-5)
except EdadInvalidaError as e:
    print('Error:', e)