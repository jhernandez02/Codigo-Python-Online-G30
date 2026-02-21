# Crear una aplicacion que solicite al usuario una palabra,
# y muestre la cantidad de vocales diferentes
# Utilizar conjuntos
# Input: murcielago -> Output: 5
# Input: casa -> Output: 1
# Input: justicia -> Output: 3 

#  Input: zozobra
palabra = input("Ingresa una palabra: ").lower()
vocalesSet = {'a','e','i','o','u'}
palabraSet = set(palabra)
print(palabraSet) # {'o', 'b', 'r', 'z', 'a'}
interseccion = vocalesSet & palabraSet
print(interseccion) # {''o','a'}
print('Cantidad de vocales:', len(interseccion))
