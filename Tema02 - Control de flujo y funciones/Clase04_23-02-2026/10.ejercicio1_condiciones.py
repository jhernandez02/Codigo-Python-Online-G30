'''
Crear una aplicación en Python, para solicitar el valor de un ángulo al usuario.
Donde los ángulos se clasifican de las siguiente manera:
b=0         => Nulo
0<b<90      => Agudo
b=90        => Recto
90<b<180    => Obtuso
b=180       => Llano
180<b<360   => Cóncavo
b=360       => Completo
'''
b = int(input('Ingrese el valor del ángulo (0-360): '))

# Validamos según las indiciaciones previas:
if b==0:
    print('Nulo')
elif b<90:
    print('Agudo')
elif b==90:
    print('Recto')
elif b<180:
    print('Obtuso')
elif b==180:
    print('Llano')
elif b<360:
    print('Cóncavo')
elif b==360:
    print('Completo')
else:
    print('Ángulo inválido')
