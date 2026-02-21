# Solicitar el nombre de un mes
# y mostrar la cantidad de días que tiene ese mes
# Validar la existencia del mes
# Input -> abril
# Output -> 30

nombreMes = input("Ingrese el mes: ").lower()

meses = {
    'enero':31,
    'febrero':28,
    'marzo':31,
    'abril':30,
    'mayo':31,
    'junio':30,
    'julio':31,
    'agosto':31,
    'septiembre':30,
    'octubre':31,
    'noviembre':30,
    'diciembre':31
}

if nombreMes in meses.keys():
    print(meses[nombreMes])
else:
    print('El mes no existe')
