# Dada una lista de pacientes, crear el algoritmo que simula la atención de cada uno de ellos.
# Mostrar al final la cantidad de atendidos

pacientes = ('Silvia','Carlos','Miguel','Karen','Luis','Ana')
atendidos = 0
totalPacientes = len(pacientes)
print('Total pacientes:', totalPacientes)

while atendidos<totalPacientes:
    print('-------------------------')
    print('Nro atendidos:',atendidos)
    print('Atendiendo a', pacientes[atendidos])
    atendidos += 1

print('Pacientes atendidos:', atendidos)