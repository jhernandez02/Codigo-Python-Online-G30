# Elaborar un algoritmo que solicite 6 números positivos
# e imprima la cantidad de números pares e impares

cont_par = 0
cont_impar = 0

for i in range(6):
    numero = int(input('Número: '))
    if numero%2==0 : 
        cont_par += 1
    else:
        cont_impar += 1

print('Pares:', cont_par)
print('Impares:', cont_par)