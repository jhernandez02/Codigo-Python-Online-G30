'''
args es una forma de pasar una cantidad variable de parámetros a una función
'''

def promediarNotas(*args):
    print(args, type(args))
    total = len(args)
    suma = sum(args)
    promedio = suma/total
    return promedio

def entregarPromedioCursoAlgoritmos():
    resultado = promediarNotas(15,18,12,10)
    print("Promedio Algoritmos:",resultado)

def entregarPromedioCursoBaseDatos():
    resultado = promediarNotas(10,15,13,18,12,16)
    print("Promedio Base de Datos:",resultado)

# Ejecutamos las funciones
entregarPromedioCursoAlgoritmos()
entregarPromedioCursoBaseDatos()