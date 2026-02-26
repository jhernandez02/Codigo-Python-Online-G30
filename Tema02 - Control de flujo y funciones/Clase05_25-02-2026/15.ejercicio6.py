# Implementar una función que reciba varias palabras
# y retorne True is algún valor se repite
# Si las palabras son únicas, retorna False

def verificarPalabrasRepetidas(*palabras):
    repetido = False
    vistos = []
    for palabra in palabras:
        if palabra in vistos:
            # Detiene la iteración y devuelve True
            return True
        vistos.append(palabra)
    return repetido

print(verificarPalabrasRepetidas('sol','mas','calor'))
print(verificarPalabrasRepetidas('sol','mas','calor','rio','sol','verde'))