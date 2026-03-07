'''
Desarrollar un clase para instanaciar objetos microondas.
El objeto debe tener las funcionalidades básicar de un microondas.
Implementa un menú interactivo.
'''
class Microondas:
    # Atributos
    encendido = False

    # Constructor
    def __init__(self, marca, capacidad, color):
        self.marca = marca
        self.capacidad = capacidad
        self.color = color
    
    # Métodos
    def info(self):
        print('---- Datos Microondas ----')
        print('Marca:', self.marca)
        print('Capacidad:', self.capacidad)
        print('Color:', self.color)
    
    def encender(self):
        if self.encendido == False:
            self.encendido = True
            print(f"Microondas {self.marca} encendido.")
        else:
            print(f"Microondas {self.marca} ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"Microondas {self.marca} apagado.")
        else:
            print(f"Microondas {self.marca} ya está apagado.")

    def calentar(self):
        if self.encendido:
            segundos = int(input('Ingrese los segundos: ')) 
            print("Calentando la comida...")
            while segundos>0:
                print(f"Segundos: {segundos}")
                segundos -= 1
            print("¡Comida lista!")
        else:
            print("No se puede calentar: el microondas está apagado.")

micro1 = Microondas('LG', '20Kg', 'Negro')
menu = True

while menu:
    print('--- Panel de control ---')
    print('1. Encender')
    print('2. Calentar')
    print('3. Apagar')
    print('4. Salir')
    opcion = input('Ingresa una opción: ')
    print('-------------------------')
    if opcion=='1':
        micro1.encender()
    elif opcion=='2':
        micro1.calentar()
    elif opcion=='3':
        micro1.apagar()
    elif opcion=='4':
        menu = False
    else:
        print('Opción incorrecta')