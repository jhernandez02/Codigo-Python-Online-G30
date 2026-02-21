# Ingresar el monto de ganancias por año.
# Si el monto no supera los 10000, se paga 5% de impuesto
# Si el monto va entre 10001 y 20000, se paga 15% de impuesto
# Si el monto va entre 20001 y 35000, se paga 20% de impuesto
# Si el monto supera los 35000, se paga el 30% de impuesto
# Indicar el porcentaje de impuesto a pagar

monto = int(input('Ingresa el monto de ganancia por año:'))

'''
if monto <= 10000:
    print('5%')
elif monto>=10001 and monto<=20000:
    print('15%')
elif monto>=20001 and monto<=35000:
    print('20%')
else:
    print('30%')
'''

if monto <= 10000:
    print('5%')
elif monto <= 20000:
    print('15%')
elif monto <= 35000:
    print('20%')
else:
    print('30%')
