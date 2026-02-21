colorList = ['rojo','azul','verde','azul','amarillo','azul','rojo']

# Obtener los colores únicos de la lista
coloresUnicos = []
for color in colorList:
    print(color)
    if color not in coloresUnicos:
        coloresUnicos.append(color)

print('coloresUnicos:', coloresUnicos)

# Convierto la lista en un conjunto
colorSet = set(colorList)
print('colorSet:', colorSet)