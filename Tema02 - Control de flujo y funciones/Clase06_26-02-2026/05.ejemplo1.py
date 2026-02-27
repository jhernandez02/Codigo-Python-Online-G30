'''
Implementamos un programa que solicite el nombre del archivo
para poder mostrar su contenido.
'''

try:
    nombreArchivo = input('Nombre del archivo: ')
    archivo = open(nombreArchivo+'.txt','r')
except FileNotFoundError:
    print('El archivo no existe')
else:
    contenido = archivo.read()
    print('Archivo leído correctamente')
    print(contenido)
    archivo.close()