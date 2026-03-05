'''
Crear una aplicación que registre: nombre, salario, horas extras.
Se debe calcular el salario total, donde cada hora extra vale el 20% más que la hora normal
'''

class Empleado:
    def __init__(self, nombre, salario, horas_extras):
        self.__nombre = nombre
        self.__salario = salario
        self.__horasExtras = horas_extras

    def getNombre(self):
        return self.__nombre
    
    def getSalario(self):
        return self.__salario
    
    def getHorasExtras(self):
        return self.__horasExtras

    def __calcularValorHora(self):
        return self.__salario/160 # asumismo 160 hrs al mes

    def __calcularSalarioExtra(self, valor_hora_extra):
        return self.__horasExtras * valor_hora_extra

    def __getSalarioTotal(self):
        valor_hora = self.__calcularValorHora()
        valor_hora_extra = valor_hora * 1.2
        salario_extra = self.__calcularSalarioExtra(valor_hora_extra)
        return self.__salario + salario_extra
    
    def info(self):
        print('Nombre:', self.getNombre())
        print('Salario:', self.getSalario())
        print('Horas extras:', self.getHorasExtras())
        print('Salario Total:', self.__getSalarioTotal())

empleado1 = Empleado('Kevin', 1600, 10)
empleado1.info()