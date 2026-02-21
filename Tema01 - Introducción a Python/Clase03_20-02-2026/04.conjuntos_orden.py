colorSet = {'rojo','azul','verde','azul','amarillo','azul','rojo'}

# Ordenamos lista/conjunto
listaOrdenada = sorted(colorSet)
print(listaOrdenada)
print('tipo',type(listaOrdenada))

# Invertimos el orden de los elementos
colorList = list(colorSet) # Convertimos el conjunto a una lista
print('colorList:', colorList)
listaInvertida = list(reversed(colorList))
print('listaInvertida:', listaInvertida)