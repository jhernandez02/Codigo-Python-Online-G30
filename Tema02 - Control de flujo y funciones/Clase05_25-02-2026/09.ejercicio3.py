# Implementar una función que solicite un texto
# y que devuelva la cantidad de vocales.
# Ej: "Hola mundo" => Output: 4

def contarVocales(texto):
    contador = 0
    vocales = ('a','e','i','o','u')
    texto = texto.lower()

    for letra in texto:
        if letra in vocales:
            contador += 1

    return contador

texto = input('Ingrese un texto: ')
print('Vocales:',contarVocales(texto))