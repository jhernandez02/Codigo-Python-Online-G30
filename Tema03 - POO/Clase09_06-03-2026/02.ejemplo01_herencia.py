class Mascota:
    def comer(self):
        print(f"{self.nombre} está comiendo")
    def dormir(self):
        print(f"{self.nombre} está durmiendo")
    def info(self):
        print("---- Datos Mascota ----")
        print('Especie:',self.especie)
        print('Raza:',self.raza)
        print('Nombre:',self.nombre)

class Perro(Mascota):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.especie = "perro"
        self.raza = raza
    def ladrar(self):
        print('wof wof wof')

class Gato(Mascota):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.especie = "gato"
        self.raza = raza
    def maullar(self):
        print('miau miau miau')

dog = Perro('Chiquitin','Doberman')
dog.info()
dog.comer()
dog.dormir()

cat = Gato('Bigotes','Angora')
cat.info()
cat.comer()
cat.dormir()
