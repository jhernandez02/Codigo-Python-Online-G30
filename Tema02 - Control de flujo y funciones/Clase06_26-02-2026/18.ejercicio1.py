'''
Crear una función que recibar una lista de string.
Debe convertirlos a entero, si falla una conversión,
mostrar que valor falló y continuar con los demás valores
'''

def convertirLista(lista):
    numeros = []
    for valor in lista:
        try:
            numero = int(valor)
            numeros.append(numero)
        except ValueError:
            print(f"No se pudo convertir: {valor}")
    return numeros

lista = ['10','20','abc','30','ma','50']
print(convertirLista(lista))