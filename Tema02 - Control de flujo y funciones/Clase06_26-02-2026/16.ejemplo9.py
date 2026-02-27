class ConexionError(Exception):
    pass

def conectar(estado):
    try:
        if not estado:
            raise ConexionError('No se pudo conectar al servidor')
        print('Conexión exitosa')
    finally:
        print('Intento de conexión finalizada')

try:
    conectar(False)
except ConexionError as e:
    print('Error:', e)