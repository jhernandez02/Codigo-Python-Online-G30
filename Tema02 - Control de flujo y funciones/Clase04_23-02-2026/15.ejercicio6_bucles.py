# Elaborar un algotimo que solcite un número
# e imprimir el factorial del número
# Ej: 5! = 1x 1x2x3x4x5
# Ej: 7! = 1x 1x2x3x4x5x6x7

factorial = 1
numero = int(input('Número: ')) # 5

for i in range(1,numero+1):
    factorial *=i

print(f"Factorial de {numero} es {factorial}")
