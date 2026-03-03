class Celular:
    # Implementamos el constructor
    def __init__(self, marca, modelo, numero):
        self.marca = marca
        self.modelo = modelo
        self.numero = numero
        if modelo=='Redmi':
            self.precio = 1600
        else:
            self.precio = 1800

    def info(self):
        print('---- Info Celular ----')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Precio:', self.precio)
        print('Número: ', self.numero)

celular1 = Celular('Xiaomi','Redmi','98797001')
celular1.info()

celular2 = Celular('Honor','Magic','98797002')
celular2.info()
