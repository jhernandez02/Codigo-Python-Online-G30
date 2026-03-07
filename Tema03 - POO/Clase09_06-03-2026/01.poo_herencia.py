'''
La herencia permite que una clase (hija) reutilice y extienda
el comportamiento de otra clase (padre)
La clase hija solo puede heredar los atributos y métodos públicos.
'''

class Padre:
    __nombre = 'José'       # Atributo privado
    apellido = 'Gonzales'   # Atributo público
    __edad = 70             # Atributo privado
    def saludar(self):  # Método público
        print('¡Hola que tal!')
    def __cantar(self): # Método privado
        print('Padre cantando')

# La clase Hijo hereda de la clase Padre
class Hijo(Padre):
    def __init__(self, nombre):
        self.nombre = nombre
    def cantando(self):
        super().__cantar() # No se hereda

child = Hijo('Felipe')

# Accedemos a los atributos y métodos del hijo
print('Nombre:', child.nombre)
print('Apellido:', child.apellido)
#print('Edad:', child.__edad) # No puede heredar la edad del padre
child.saludar()
#child.cantando() # No puede heredar el método cantar del padre
