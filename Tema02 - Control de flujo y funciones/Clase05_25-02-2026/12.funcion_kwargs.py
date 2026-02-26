'''
kwargs es una forma de pasar una cantidad variable de parámetros 
de tipo clave-valor a una función
'''

def mostrarDatosMascota(**kwargs):
    print(kwargs, type(kwargs))
    for key,value in kwargs.items():
        print(f"{key}: {value}")

mostrarDatosMascota(nombre='Firulais',tipo='conejo')
mostrarDatosMascota(nombre='Chuletas',tipo='cerdo',color='pinky')