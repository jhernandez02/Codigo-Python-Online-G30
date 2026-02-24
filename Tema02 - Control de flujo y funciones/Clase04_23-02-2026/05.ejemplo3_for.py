# Dada una lista de pacientes, crear el algoritmo que simula la atención de cada uno de ellos.
# Mostrar al final la cantidad de atendidos

pacientes = ('Silvia','Carlos','Miguel','Karen','Luis','Ana')
totalPacientes = len(pacientes)
print('Total pacientes:', totalPacientes)

for i in range(totalPacientes):
    print('-------------------------')
    print('Nro atendidos:', i)
    print('Atendiendo a', pacientes[i])

print('Pacientes atendidos:', totalPacientes)