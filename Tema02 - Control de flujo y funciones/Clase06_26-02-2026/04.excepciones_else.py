'''
El código del bloque "else", 
se ejecutará si no ha ocurrido un ningún error
'''

try:
    monto = int(input('Ingrese monto a transferir: '))
    print("Monto transferido")
except Exception as error:
    print('Ha ocurrido un error')
    # guardo el error en error.log
else:
    print('Operación existosa')
    # guardo el operación en events.log
