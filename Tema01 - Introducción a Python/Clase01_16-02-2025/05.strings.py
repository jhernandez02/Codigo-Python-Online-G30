mensaje = "Mi nuevo mensaej"
print(mensaje)
print("Primer caracter:", mensaje[0])
print("Primer espacio en blanco:", mensaje[2])
total = len(mensaje) # Obtenemos el total de caracteres
print("Total caracteres:", total)
print("Último caracter:", mensaje[total-1])
print("Penúltimo caracter:", mensaje[-2])

print("------------------------")
mensaje = "Python Es CHevEre"
print(mensaje)
print(mensaje.upper())  # convierte a mayúsculas
print(mensaje.lower())  # convierte a minúsculas
# convierte mayus a minus y minus a mayus
print(mensaje.swapcase())
# convierte todo a minus y mayus solo el primer caracter
print(mensaje.capitalize())

