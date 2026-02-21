# Solicitar 2 frases, y mostrar las palabras que no se repiten.
# Input1: python es chevere
# Input2: python es bacán
# Output: chevere, bacán
# Input1: La casa de mi primo y de mi tia es muy bonita
# Input2: La piscina es muy bonita
# Output: casa,de,mi,primo,y,tia,piscina

frase1 = input("Frase1: ").lower()
frase2 = input("Frase2: ").lower()
lista1 = frase1.split(" ")
lista2 = frase2.split(" ")
# print(lista1,lista2)
fraseSet1 = set(lista1)
fraseSet2 = set(lista2)
#print(fraseSet1,fraseSet2)
print(fraseSet1 ^ fraseSet2) # Mostramos las palabras diferentes de cada frase