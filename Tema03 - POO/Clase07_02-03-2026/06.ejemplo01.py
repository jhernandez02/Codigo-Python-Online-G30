class Libro:
    def __init__(self, genero, titulo, autor):
        self.genero = genero
        self.titulo = titulo
        self.autor = autor
    
    def info(self):
        print('Género:', self.genero)
        print('Título:', self.titulo)
        print('Autor: ', self.autor)

libro1 = Libro('Novela','Vacaciones en París','Felipe Gonzales')
libro1.info()
print('---------------------------------------')
libro2 = Libro('Terror','La chancla de mi mama','Cecilia Morales')
libro2.info()