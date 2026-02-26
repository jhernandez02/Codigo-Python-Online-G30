# Elaborar una función que tome como parámetro
# tres números enteros y devuelva el mayor
# Ej: 10, 18 y 5 => 18

def devolverNumeroMayor(num1, num2, num3):
    numMayor = num1
    if num2 > numMayor:
        numMayor = num2
    if num3 > numMayor:
        numMayor = num3
    return numMayor

numMayor = devolverNumeroMayor(12,16,8)
print(f"El número mayor es: {numMayor}")

def devolverNumeroMayor2(num1, num2, num3):
    tupla = (num1,num2,num3)
    return max(tupla)

numMayor = devolverNumeroMayor2(14,16,81)
print(f"El número mayor es: {numMayor}")