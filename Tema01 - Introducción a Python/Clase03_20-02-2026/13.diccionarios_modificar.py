productoDict = {'marca':'Akita', 'nombre':'pilas', 'precio':4}
print(productoDict)

#Actualizar valores
productoDict['nombre'] = 'Pilas A3'
print(productoDict)
productoDict.update({'precio': 3.7})
print(productoDict)

# Añadir un nuevo elemento
productoDict['categoria'] = 'Herramientas'
productoDict.update({'peso':'40gr'})
print(productoDict)

# Eliminar un elemento
productoDict.pop('peso')
print(productoDict)