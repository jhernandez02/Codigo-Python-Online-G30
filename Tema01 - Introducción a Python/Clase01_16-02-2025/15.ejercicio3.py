# Elabora un programa que solicite 3 notas
# y obtenga el promedio
n1 = int(input("Ingresa nota1: "))
n2 = int(input("Ingresa nota2: "))
n3 = int(input("Ingresa nota3: "))
total = n1 + n2+ n3
promedio = total/3
# .2 -> 2 decimales
# f -> formato tipo float
print(f"Promedio: {promedio:.2f}")