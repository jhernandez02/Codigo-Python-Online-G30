# Implementar un menú para un CRUD

menu = True

while menu:
    print('--- Menú ---')
    print('1.Listar los registros')
    print('2.Ingresar un nuevo registro')
    print('3.Editar un registro')
    print('4.Eliminar un registro')
    print('5. Salir')
    opcion = input('Ingresa una opción:')
    if opcion=='1':
        print('--- Listado ---')
    elif opcion=='2':
        print('--- Nuevo registro ---')
    elif opcion=='3':
        print('--- Editar registro ---')
    elif opcion=='4':
        print('--- Eliminar registro ---')
    elif opcion=='5':
        menu = False
    else:
        print('Opción incorrecta')
