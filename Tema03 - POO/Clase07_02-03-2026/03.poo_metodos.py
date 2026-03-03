class Celular:
    marca = '' # Xiaomi | Honor
    modelo = '' # Redmi - 1600 | Magic - 1800
    precio = 0
    numero = ''

    def setModelo(self, modelo):
        self.modelo = modelo
        if modelo=='Redmi':
            self.marca = 'Xiaomi'
            self.precio = 1600
        else:
            self.marca = 'Honor'
            self.precio = 1800

    def info(self):
        print('---- Info Celular ----')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Precio:', self.precio)
        print('Número: ', self.numero)
        print('----------------')

    def llamar(self, numero):
        print(f"Llamando al número {numero}")
    
    def enviarSMS(self, numero, mensaje):
        print(f"Enviando sms: '{mensaje}' al número {numero}")

# Instanciamos un objeto de la clase Celular
celular1 = Celular()
modelo = input('Modelo1: ')
celular1.setModelo(modelo)
celular1.numero = '98765001'
celular1.info()
celular1.llamar('987987987')
celular1.enviarSMS('987987987', 'Hola que haces?')

print('---- Celular2 ----')
celular2 = Celular()
modelo = input('Modelo2: ')
celular2.setModelo(modelo)
celular2.numero = '98765002'
celular2.info()