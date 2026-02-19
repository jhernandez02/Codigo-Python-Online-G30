# Hallar la cantidad de correos

correos = "pp@mail.com,kj@mail.com,jj@mail.com"
print(correos)
print(len(correos))

# split(), divide el texto en partes usando un separador (parámetro)
# y devuelve una lista con los fragmentos resultantes
lista_correos = correos.split(',')
print(type(lista_correos))
print(lista_correos)
print(len(lista_correos))