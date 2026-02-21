# Desarrollar un programa para una discoteca
# que pregunte por la edad del cliente
# Verificar si es mayor de edad
# Validar si el cliente tiene suficiente dinero
# para pagar la entrada
# El programa debe indicas si puedes ingresar o no 

entrada = 70
edad = int(input('Edad: '))
dinero = int(input('Dinero: '))

'''
if edad < 18:
    print('Eres menor de edad')
elif dinero < entrada:
    print('No tienes dinero suficiente')
else:
    print('Puedes ingresar')
'''

if edad>=18 and dinero>entrada:
    print('Puedes ingresar')
else:
    print('No puedes ingresar')
