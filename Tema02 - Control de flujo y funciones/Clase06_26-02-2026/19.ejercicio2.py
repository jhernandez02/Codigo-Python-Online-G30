'''
Crear una aplicación para retirar saldo de un cajero
Se debe lanzar excepciones personalizadas cuando:
- La cantidad es negativa
- No hay saldo suficiente
Usar try-except-else-finally
Simpre imprimir "Operacion Finalizada"
'''

class CajeroError(Exception):
    pass

saldo = 100

def retirarSaldo(cantidad):
    global saldo
    try:
        if  cantidad < 0:
            raise CajeroError('No puedes retirar cantidades negativas')
        if cantidad > saldo:
            raise CajeroError('Saldo insuficiente')
    except CajeroError as e:
        print('Error:', e)
    else:
        saldo -= cantidad
        print(f'Nuevo saldo: {saldo}')
    finally:
        print('Operación finalizada')

def menu():
    while(True):
        print('---- Menú ----')
        print('1. Mostrar saldo')
        print('2. Retirar saldo')
        print('3. Salir')
        opcion = input('Opción: ')
        if opcion=='1':
            print('Saldo:',saldo)
        elif opcion=='2':
            monto = int(input('Monto: '))
            retirarSaldo(monto)
        elif opcion=='3':
            break
        else:
            print('Opción inválida')

menu()