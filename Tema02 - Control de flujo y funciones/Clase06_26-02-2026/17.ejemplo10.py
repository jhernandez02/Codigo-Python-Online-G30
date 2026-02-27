# Desarrollar las excepciones personalizas para una biblioteca

class BibliotecaError(Exception):
    pass

class LibroNoEncontradoError(BibliotecaError):
    pass

libros = ['Caperucita roja','Los 3 cerditos','Blanca Nieves']

def buscarLibro():
    print(libros)
    index = int(input('Indice: '))
    if index>len(libros):
        raise LibroNoEncontradoError('No se encontró el libro en el sistema')
    print('Titulo:',libros[index])

try:
    buscarLibro()
except BibliotecaError as error:
    print('Ocurrio un error')
    print('Error:', error)