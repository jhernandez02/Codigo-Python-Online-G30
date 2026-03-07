class Mascota:
    def __init__(self, raza, nombre):
        self.__raza = raza
        self.__nombre = nombre
    
    def info(self):
        print("---- Info Mascota ----")
        print("Nombre:", self.__nombre)
        print("Especie:", self.especie)
        print("Raza:", self.__raza)
    
    def generarSonido(self):
        print(f'{self.especie} haciendo sonido')

class Perro(Mascota):
    especie = 'Perro'
    def generarSonido(self):
        print('wof wof wof')

class Gato(Mascota):
    especie = 'Gato'
    def generarSonido(self):
        print('miau miau miau')

class Reptil(Mascota):
    especie = 'Reptil'

dog = Perro('Doberman','Julius')
dog.info()
dog.generarSonido()

cat = Gato('Persa','Leono')
cat.info()
cat.generarSonido()

reptil = Reptil('Lagarto','Juancho')
reptil.info()
reptil.generarSonido()