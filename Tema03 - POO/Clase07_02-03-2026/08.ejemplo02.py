class Auto:
    encendido = False
    bateria = 50 # 0% -> 100 %
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def info(self):
        print('------ Datos del Auto ------')
        print('Marca:',self.marca)
        print('Modelo:', self.modelo)
    
    def encender(self):
        self.encendido = True
        print('Auto encendido')
    
    def apagar(self):
        self.encendido = False
        print('Auto apagado')

    def avanzar(self):
        if self.encendido and self.bateria>0:
            self.bateria -= 10
            print('Auto avanzando...')
        else:
            print('Auto apagado o sin combustible')

    def mostrarBateria(self):
        print('Bateria: ', self.bateria,'%')

    def cargarBateria(self, cantidad):
        for i in range(self.bateria, cantidad, 10):
            print('Cargando bateria al ',i,'%')
        self.bateria += cantidad
        print('Bateria cargada al ',self.bateria,'%')

auto1 = Auto('Toyota','Hilux','Negro')
auto1.info()
auto1.avanzar()
auto1.encender()
auto1.avanzar()
auto1.avanzar()
auto1.avanzar()
auto1.mostrarBateria()
auto1.avanzar()
auto1.avanzar()
auto1.avanzar()
auto1.cargarBateria(80)
auto1.avanzar()
auto1.avanzar()
auto1.apagar()
auto1.avanzar()