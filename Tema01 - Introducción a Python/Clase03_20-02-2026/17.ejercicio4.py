# Crear un programa que cuente cuantas veces aparece cada letra en una palabra
# Solicitar la palabra al usuario.
# Input: casa -> Output: c:1,a:2,s:1

frecuencia = {} # {'c':1, 'a':2, 's':1}
palabra = input("Ingresa una palabra: ").lower()
for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra] +=1
    else:
        frecuencia[letra] = 1

print(frecuencia)