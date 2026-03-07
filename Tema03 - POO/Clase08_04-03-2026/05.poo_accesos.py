'''
Los atributos y métodos públicos, se puede acceder desde la clase y objeto
Los atributos y métodos privados, no pueden ser accedidos desde el objeto
Los atributos y métodos privados, puede ser accedidos desde la clase
'''

class Mascota:
    def __init__(self, especie, nombre, edad):
        self.especie = especie  # Atributo público
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado
    
    def __getNombre(self):  # Método privado
        print('Nombre:', self.__nombre)

    def __getEdad(self):    # Método privado
        print('Edad:', self.__edad)

    def info(self): # Método público
        print ('--- Datos de la mascota ---')
        self.__getNombre()
        self.__getEdad()

mascota1 = Mascota('Perro','Firulais',2)
print('Especie:', mascota1.especie)
# print('Nombre:', mascota1.__nombre) # No se puede acceder a un atributo privado
# mascota1.__getEdad() # No se puede acceder a un método privado
mascota1.info()