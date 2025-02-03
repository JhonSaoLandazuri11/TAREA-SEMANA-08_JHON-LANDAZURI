#Aplicar los conceptos aprendidos sobre constructores y destructores para desarrollar un programa en Python. El trabajo se realizará en el IDE PyCharm y posteriormente será publicado en el repositorio personal de GitHub de cada estudiante.

class Libro:
    def __init__ (self, titulo, autor, numero_paginas, año_de_lanzamiento):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.año_de_lanzamiento = año_de_lanzamiento
        print(f"El libro '{self.titulo} ha sido creado")

    def mostrar_detalles(self): # Método para mostrar detalles del libro
        print (f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de paginas que contiene el libro: {self.numero_paginas}")
        print(f"Año de lanzamiento del libro: {self.año_de_lanzamiento}")
        print("-" * 40)

# Destructor: Libera recursos cuando el objeto es eliminado
    def __del__(self):
        print(f"El libro '{self.titulo} ha sido eliminado")

# Crear un objeto de la clase Libro
if __name__ == "__main__":
    libro1 = Libro("El amor en los tiempos del cólera" , "Gabriel García Márquez" , 348 , "1985")
    libro2 = Libro("Orgullo y prejuicio" , "Jane Austen" , 432 , "1813")
    libro3 = Libro("Crimen y castigo" , "Fiódor Dostoyevski" , 671 , "1866")
    libro4 = Libro("Don Quijote de la Mancha" , "Miguel de Cervantes" , 863 , "1605")

    # Mostrar los detalles del libro
    libro1.mostrar_detalles()
    libro2.mostrar_detalles()
    libro3.mostrar_detalles()
    libro4.mostrar_detalles()

    print("Fin del Programa.")
