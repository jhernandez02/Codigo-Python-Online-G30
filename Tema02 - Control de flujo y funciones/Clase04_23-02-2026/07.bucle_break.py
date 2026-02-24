'''
La instrucción break, se usa dentro de un bucle (while o for)
para sliar del bucle inmediatamente, sin esperar a que la condición 
del bucle se vuelva fals o que se complete el recorrido
'''

print('--- Break en bucle while ---')
while True:
    texto = input("Escribe 'salir' para terminar: ")
    if texto=='salir':
        break
    print('Escribiste: ', texto)

print('--- Break en bucle for ---')
colores = ('rojo','verde','azul','amarillo','negro')
buscar = input('Escribe el color: ')

for color in colores:
    print(color)
    if color==buscar:
        print('Encontrado')
        break