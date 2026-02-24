'''
La instrucción continue, salta el resto del código dentro del bucle
y pasa directamete a la siguiente iteración del bucle
'''

print('--- Continue con for ---')
personas = (16,29,18,17,23,32,15,19,28)
for edad in personas:
    # Solo le vende a mayores de 18 años
    if edad < 18:
        continue
    print('Compra tu entrada:', edad)

print('--- Continue con while ---')
numero = 0
# Mostramos los números pares menores a 8
while numero<8:
    numero += 1
    if numero%2!=0:
        continue
    print(numero)