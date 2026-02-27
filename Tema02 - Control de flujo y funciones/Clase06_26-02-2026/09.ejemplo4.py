password = None

def login():
    try:
        global password
        password = input('Ingresa tu clave:')
        print('Enviando datos...')
        if password !='123456':
            print('Contraseña incorrecta')
    except Exception:
        print('Ha ocurrido un error')
    else:
        print('Acceso concedido!')
    finally:
        password=None
        print('Password eliminada de la memoria')
login()
print(password)