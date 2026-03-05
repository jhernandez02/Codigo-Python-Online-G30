class Mascota:
    def __init__(self, especie, nombre, edad):
        self.__especie = especie    # Atributo privado
        self.__nombre = nombre      # Atributo privado
        self.__edad = edad          # Atributo privado

    # Métodos getters
    @property
    def species(self):
        return self.__especie
    
    @property
    def name(self):
        return self.__nombre
    
    @property
    def age(self):
        return self.__edad

    # Métodos setters
    @name.setter
    def name(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

# Instanciamos un objeto de la clase Mascota
mascota1 = Mascota('Gato','Bigotes',4)
print('Especie:', mascota1.species)
print('Nombre:', mascota1.name)
print('Edad:', mascota1.age)
print('-------------------------')
mascota2 = Mascota('Perro','Mustafa',2)
mascota2.name = 'Leono'
print('Especie:', mascota2.species)
print('Nombre:', mascota2.name)
print('Edad:', mascota2.age)
