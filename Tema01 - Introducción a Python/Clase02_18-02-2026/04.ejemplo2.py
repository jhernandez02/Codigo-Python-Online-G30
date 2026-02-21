# Tenemos una lista de invitados para una fiesta
# Para ingresar cada invitado brindará su nombre
# y el programa deberá indicas si esta o no en la lista

invitados = ['Luis','Carlos','Sara','Alán']
nombre = input('Cual es su nombre? ')
existe = nombre in invitados
print('Permitir ingreso?', existe)