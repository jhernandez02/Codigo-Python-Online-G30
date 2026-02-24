'''
El bucle while es una estructura de control, que repite un bloque de codigo}
mientras se cumpla la condición.
No se puede determinar cuantas veces se va a repetir el código.
'''
condicion = True
cont = 0

while condicion:
    cont += 1
    numero = int(input('Ingresa un número: '))
    if numero<10:
        condicion = False

print('Repeticiones:', cont)