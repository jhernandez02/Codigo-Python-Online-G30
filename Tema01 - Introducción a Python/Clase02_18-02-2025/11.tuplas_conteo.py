notas = (9,11,16,18,17,13,10,15,16,9,13,9,13)

# Hallamos cuantas veces se repite la nota 13
print('Cantidad de 13s:', notas.count(13))

# Hallar la máxima nota
nota_maxima = max(notas)
print('Nota máxima:', nota_maxima)

# Hallar la mínima nota
nota_minima = min(notas)
print('Nota mínima:', nota_minima)

# Hallar cuantas veces se repite la nota mínima
print('Total de notas mínimas:', notas.count(nota_minima))

# Hallar la suma de todas las notas
suma = sum(notas)
print('Sumatoria:', suma)