'''
class: Una clase es una plantilla, donde se define las características y funcionalidades de un objeto
objeto: Tiene atributos (características) y métodos (funcionalidades)
instanciar: Es la creación de un objeto basado en una clase 
'''

class MascotaBot:
    # Atributos
    nombre = ''
    especie = ''
    raza = 'Sin datos'
    color = ''
    tamanio = '' # Pequeño, Mediano, Grande
    fechaNac = 'Sin datos'
    # Métodos
    def emitirSonido(self):
        print('emitiendo sonido')
    def saltar(self):
        print('saltando')
    def comer(self):
        print('comiendo')

# Instanciamos un objeto de la clase MascotaBot
mascota1 = MascotaBot()

# Accedemos a los atributos de un objeto
print('Nombre:', mascota1.nombre)
print('Raza:', mascota1.raza)

# Asignar valores a los atributos de un objeto
mascota1.nombre = 'Firulais'
mascota1.especie = 'Perro'
mascota1.color = 'Caramelo'
mascota1.tamanio = 'Grande'

# Accedemos a los atributos de un objeto
print('---- Datos de la Mascota1 ----')
print('Nombre:', mascota1.nombre)
print('Especie:', mascota1.especie)
print('Color:', mascota1.color)
print('Tamaño:', mascota1.tamanio)

# Accedemos a los métodos de un objeto
mascota1.emitirSonido()
mascota1.saltar()
mascota1.comer()

# Instanciando otro objeto
print('---- Mascota2 ----')
mascota2 = MascotaBot()
mascota2.emitirSonido()
mascota2.saltar()
mascota2.comer()