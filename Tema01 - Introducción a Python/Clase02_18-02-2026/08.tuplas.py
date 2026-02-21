# Una tupla es una estructura de datos
# que puede almacenar una colección de elementos.
# Es inmutable, no se puede modificar.
# Los elementos tienen un orden definido, y no cambia
# Permite duplicados

# Días laborables
tupla = ('lun','mar','mie','jue','vie')

# Mostrar el contenido de la tupla
print(tupla)

# Obtener el total de elementos de la tupla
total = len(tupla)
print(total)

# Acceder a un elemento
#print(tupla[10]) # -> IndexError
print(tupla[3])  # -> jue

# No se puede modificar, agregar o quitar elementos
# tupla[1] = 'sab' # -> TypeError
# tupla.append("sab") # -> AttributeError
# del(tupla[3]) # -> TypeError