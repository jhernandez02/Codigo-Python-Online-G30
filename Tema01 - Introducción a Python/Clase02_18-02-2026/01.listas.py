# una lista es una estrucutra de datos
# que puede almacenar una colección de elementos

cesta = ['uva','piña','kiwi','coco']

# Mostrar el contenido de la lista
print(cesta)

# Obtener el total de elementos de la lista
total = len(cesta)
print(total)

# Acceder a un elemento
# print(cesta[10]) # -> IndexError
print(cesta[3])  # -> kiwi

# Modificar elemento
cesta[1] = "melón"
print(cesta)

# Agregar un nuevo elemento
cesta.append("manzana")
cesta.append("sandía")
print(cesta)

# Eliminar un elmento
del(cesta[3])
print(cesta)