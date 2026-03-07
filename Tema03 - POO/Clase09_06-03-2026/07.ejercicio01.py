'''
Crear una aplicación para el registro de una cuenta bancaria.
Para crear una cuenta (clase padre), se necesita solicitar un monto inicial.
Una cuenta permite depositar y retirar un monto indicado.
Para la creación de la cuenta, se debe crear primero un cliente (clase hijo).
El cliente puede mostrar el saldo de su cuenta.
'''

class CuentaBancaria:
    def __init__(self, monto):
        self.saldo = monto
    def depositar(self, monto):
        self.saldo += monto
        print(f'Monto depositado:',monto)
    def retirar(self, monto):
        if monto > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= monto
            print(f'Monto retirado:',monto)

class Cliente(CuentaBancaria):
    def mostrarSaldo(self):
        print(f"Saldo: {self.saldo}")

cliente = Cliente(1000)
cliente.mostrarSaldo()
cliente.retirar(350)
cliente.mostrarSaldo()
cliente.depositar(500)
cliente.mostrarSaldo()