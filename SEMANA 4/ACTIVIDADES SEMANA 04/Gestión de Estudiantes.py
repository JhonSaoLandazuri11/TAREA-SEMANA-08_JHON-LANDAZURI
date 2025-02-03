# Programa 2: Gestión de Estudiantes

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, nombre, edad):
        self.estudiantes.append(Estudiante(nombre, edad))

    def mostrar_estudiantes(self):
        print("Lista de estudiantes:")
        for estudiante in self.estudiantes:
            estudiante.mostrar_informacion()


# Crear escuela y agregar estudiantes
escuela = Escuela("Escuela Python")
escuela.agregar_estudiante("Ana", 12)
escuela.agregar_estudiante("Carlos", 14)

# Mostrar estudiantes
escuela.mostrar_estudiantes()