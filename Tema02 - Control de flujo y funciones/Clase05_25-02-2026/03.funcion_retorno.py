'''
Una función con retorno, es aquella que después de ejecutar sus intrucciones,
devuelve un valor
'''

# Variables globales
billetera = 10
comision = 0.5

# Función que solo retorna un resultado
def cajeroAutomaticoBCHP():
    print('Ingrese su tarjeta BCHP')
    monto = int(input('Ingresa el monto: '))
    return monto-comision

def cajeroAutomaticoBBCTO():
    # Variable local
    comision = 1.5
    print('Ingrese su tarjeta BBCTO')
    monto = int(input('Ingresa el monto: '))
    return monto-comision

def guardarDinero(dinero):
    # La palabra "global", indica que la variable
    # pertenece al ámbito global (fuera de la función)
    global billetera
    billetera += dinero
    print(f"Billetera: S/ {billetera}")
# 
dinero = cajeroAutomaticoBCHP()
# print(dinero)
guardarDinero(dinero)
dinero2 = cajeroAutomaticoBBCTO()
guardarDinero(dinero2)

