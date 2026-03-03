class Pastel:
    # Atributos
    sabor = '' # Chocolate, Vainilla, Marmoleado
    ingredientes = ''
    receta = ''
    forma = '' # Circular, Rectangular, Cuadrado
    precio = 0

# Instanciamos un objeto de la clase Cake
pastel = Pastel()
print('---- Solicitud del Paste ----')
pastel.sabor = input('Sabor: ')
pastel.ingredientes = input('Ingredientes: ')
pastel.receta = input('Receta: ')
pastel.forma = input('Forma: ')
pastel.precio = input('Precio: ')

print('---- Datos del Pastel ----')
print('Sabor:', pastel.sabor)
print('Ingredientes:', pastel.ingredientes)
print('Receta:', pastel.receta)
print('Forma:', pastel.forma)
print('Precio:', pastel.precio)