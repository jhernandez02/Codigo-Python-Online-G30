'''
Los métodos públicos son los que definen la interfaz que el usuario pueden usar.
Los métodos privados se usan para ocultar la lógica interna 
que no debería ser llamada directamente por el usuario.
'''

class CuentaBancaria:
    def __init__(self, titular, saldoInicial):
        self.titular = titular
        self.__saldo = saldoInicial
    
    def depositar(self, monto):
        if monto>0:
            self.__saldo += monto 
            self.__registrarMovimiento('Depósito', monto)
    
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto 
            self.__registrarMovimiento('Retiro', monto)
        else:
            print("Fondos insuficientes")

    def mostrarSaldo(self):
        print(f"Saldo actual: {self.__saldo}")

    def __registrarMovimiento(self, movimiento, monto):
        print(f"Transacción: {movimiento} de {monto}")

cuenta = CuentaBancaria('Karen Mendoza', 5000)
cuenta.mostrarSaldo()
cuenta.depositar(1300)
cuenta.mostrarSaldo()
cuenta.retirar(700)
cuenta.mostrarSaldo()
# cuenta.__registrarMovimiento('consulta')
