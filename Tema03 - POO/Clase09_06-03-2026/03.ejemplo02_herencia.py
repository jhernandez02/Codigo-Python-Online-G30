class Vehiculo:
    encendido = False
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
    def encender(self):
        self.encendido = True
        print(f"{self.tipo} encendido")
    def apagar(self):
        self.encendido = False
        print(f"{self.tipo} apagado")
    def info(self):
        print('---- Info Vehículo ----')
        print('Marca:',self.marca)
        print('Tipo:',self.tipo)

# La clase Auto hereda de la clase Vehiculos
class Auto(Vehiculo):
    def __init__(self, marca, placa):
        self.placa = placa
        # Pasamos los datos al constructor de la clase Vehiculos (padre)
        super().__init__(marca, "Auto")
    def avanzar(self):
        if self.encendido:
            print("Avanzando por la carretera")

# La clase Auto hereda de la clase Vehiculos
class Barco(Vehiculo):
    def __init__(self, marca, camino):
        self.camino = camino
        # Pasamos los datos al constructor de la clase Vehiculos (padre)
        super().__init__(marca, "Barco")
    def avanzar(self):
        if self.encendido:
            print(f"Navegando por el {self.camino}")

auto = Auto('Toyota','ABC123')
auto.info()
auto.encender()
auto.avanzar()

barco = Barco('Beneteau','río')
barco.info()
barco.encender()
barco.avanzar()
