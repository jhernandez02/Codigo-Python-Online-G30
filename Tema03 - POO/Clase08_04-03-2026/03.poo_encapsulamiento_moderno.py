# Ejemplo con encapsulamiento moderno
class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre # atributo privado
        self.__edad = edad # atributo privado
    
    # Con property, se pueda obtener el valor de objeto.propiedad, como si fuera un atributo
    # pero internamente sigue encapsulado y protegido
    @property
    def age(self):
        return self.__edad
    
    # Método setter, se pueda asignar objeto.propiedad = valor, como si fuera un atributo
    @age.setter
    def age(self, nueva_edad):
        if nueva_edad>0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser positiva")

# Instanciamos el objeto
per1 = Persona("Ana", 25)
# Accedemos y modificamos mediante los métodos getter y setter
print('Edad:',per1.age)
per1.age = -5
print('Edad:',per1.age)
per1.age = 35
print('Edad:',per1.age)