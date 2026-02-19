# Indicar el nombre de la fruta a eliminar
# Validar que la fruta exista
# Devolver el contenido de la cesta

cesta = ['uva','kiwi','coco','fresa','melón']
fruta = input('Fruta: ')

# Aqui agregas la lógica
existe = fruta in cesta

if existe:
    print('Eliminando fruta')
    indice = cesta.index(fruta) # Obtengo el indice de la fruta
    del(cesta[indice]) # Elimino el elemento de la lista
else:
    print('La fruta no se encuentra en la cesta')    

# Mostramos la cesta sin la fruta a eliminar
print(cesta)
