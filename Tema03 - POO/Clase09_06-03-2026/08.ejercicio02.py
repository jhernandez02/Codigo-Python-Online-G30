'''
Crear una aplicación para calcular el sueldo a pagar a los empleados de una empresa.
A todos los empledos se le descuent el 10% de su sueldo por concepto de AFP.
Del empleado fijo, se registra su nombre y su sueldo para el calculo del pago.
Del empleado por horas, se registra su nombre, las horas de trabajo y el costo por hora.
Del empleado por comisión, se registar su nombre, el monto total de ventas y el porcentaje de comsión
'''
class Empleado:
    descuentos = 0
    sueldoNeto = 0
    def calcularDescuentos(self):
        self.descuentos = self.sueldoBruto * 0.1
    def calcularSueldo(self):
        self.calcularDescuentos()
        self.sueldoNeto = self.sueldoBruto - self.descuentos
    def info(self):
        print('---- Info Pago Empleado ----')
        print('Empleado:',self.nombre)
        print('Sueldo bruto:',self.sueldoBruto)
        print('Descuentos:',self.descuentos)
        print('Sueldo neto:',self.sueldoNeto)

class EmpleadoFijo(Empleado):
    def __init__(self, nombre , sueldo):
        self.nombre = nombre
        self.sueldoBruto = sueldo

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifaHora):
        self.nombre = nombre
        self.horas = horas
        self.tarifaHora = tarifaHora
    
    def calcularSueldo(self):
        self.sueldoBruto = self.horas * self.tarifaHora
        self.calcularDescuentos()
        self.sueldoNeto = self.sueldoBruto - self.descuentos

class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, ventas, porcentajeComision):
        self.nombre = nombre
        self.ventas = ventas
        self.porcentajeComision = porcentajeComision
    
    def calcularSueldo(self):
        self.sueldoBruto = self.ventas * self.porcentajeComision
        self.calcularDescuentos()
        self.sueldoNeto = self.sueldoBruto - self.descuentos

empleado1 = EmpleadoFijo('Eduardo Salva', 4500)
empleado1.calcularSueldo()
empleado1.info()

empleado2 = EmpleadoPorHoras('Silvio Linares', 80, 20)
empleado2.calcularSueldo()
empleado2.info()

empleado3 = EmpleadoPorComision('Karen Mendoza', 16000, 0.20)
empleado3.calcularSueldo()
empleado3.info()