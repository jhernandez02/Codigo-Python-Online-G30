# Funcion de devuelve otra función

def crearMultiplicar(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

multiplicaPorDos = crearMultiplicar(2)
print(multiplicaPorDos(9))
multiplicaPorCinco = crearMultiplicar(5)
print(multiplicaPorCinco(9))