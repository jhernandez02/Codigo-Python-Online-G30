# Elaborar una funcion que tenga como primer argumento una lista N números.
# y como segundo argumento una función.
# El parámetro como función puede sumar todos los números
# o puede multiplicar todos los números de la lista.

# Ej: funcion([1,2,3,4], sumar)         => 10
#     funcion([1,2,3,4], multipilicar)  => 24

def sumarNumeros(lista):
    return sum(lista)

def multiplicarNumeros(lista):
    total = 1
    for num in lista:
        total *= num
    return total

def ejecutarFuncion(lista, funcion):
    resultado = funcion(lista)
    return resultado

lista = [1,2,3,4]
print('Sumatoria:', ejecutarFuncion(lista, sumarNumeros))
print('Multiplicación:', ejecutarFuncion(lista, multiplicarNumeros))