# Elaborar un algoritmo que solicite X números
# e imprima la suma
# Inicialmente solicitar la cantidad de números a ingresar

suma = 0
repeticiones = int(input('Cantidad Nros: '))
for i in range(repeticiones):
    numero = int(input('Número: '))
    suma += numero

print('Suma total:', suma)