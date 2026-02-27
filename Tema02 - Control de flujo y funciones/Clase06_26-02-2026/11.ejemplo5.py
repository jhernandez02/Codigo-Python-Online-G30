def saludar(nombre=None):
    try:
        if nombre is None:
            raise ValueError('Error! No se permite un valor nulo')            
    except Exception as error:
        print('Ocurrió un error')
        print('Nombre Error:', type(error).__name__)
        print('Descripcion Error:', error)
    else:
        print(f"Hola {nombre}")

saludar('Jhon')
print('-----------------------')
saludar()