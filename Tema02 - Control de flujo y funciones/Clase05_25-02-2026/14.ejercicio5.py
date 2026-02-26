# Implementar una función que reciba varias palabras
# y retorne la palabra con mayor cantidad de caracteres.
# Si hay empate, retornar la primera que aparezca.

def calcularPalabraMasLarga(*palabras):
    palabraLarga = palabras[0]
    for palabra in palabras:
        if len(palabra)>len(palabraLarga):
            palabraLarga = palabra
    return palabraLarga

palabra = calcularPalabraMasLarga('sol','computadora','congeladora','mesa')
print('Palabra más larga:', palabra)