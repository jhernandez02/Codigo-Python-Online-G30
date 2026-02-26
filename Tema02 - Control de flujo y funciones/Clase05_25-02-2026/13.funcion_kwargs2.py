# Implementar una función que muestre el nombre y especie de una mascota obligatoriamente
# También se puede mostrar otros datos adicionales.

def mostrarDatosMascota(nombre, especie, **kwargs):
    print('Nombre:',nombre)
    print('Especie:',especie)
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print('-----------------')

mostrarDatosMascota('Firulais','conejo',Edad=4)
mostrarDatosMascota('Chuletas','cerdo',Color='pinky',Raza='Pig')