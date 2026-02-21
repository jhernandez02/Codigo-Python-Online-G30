colorSet = {'rojo','azul','verde','azul','amarillo','azul','rojo'}
print(colorSet)

# Añadir un elemento a un conjunto
colorSet.add('blanco')
colorSet.add('amarillo')
print(colorSet)

# No se puede modificar el valor de un elemento
# colorSet[2] = 'negro' # TypeError

# Eliminar un elemento
colorSet.remove('rojo')
# colorSet.remove('celeste')  # KeyError:
print(colorSet)

# Discard elimina un elemento si encuentra el elemento
# de lo contrario no hace nada, ni da error
colorSet.discard('verde')
colorSet.discard('morado')
print(colorSet)

# Eliminar todos los elementos de un conjunto
colorSet.clear()
print(colorSet)