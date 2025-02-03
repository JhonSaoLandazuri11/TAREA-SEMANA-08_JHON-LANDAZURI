#Metodo de Herencia
# Clase base o superclase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Clase derivada o subclase
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamar al constructor de la superclase
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        # Extender el método de la superclase
        super().presentarse()
        print(f"Soy estudiante de la carrera de {self.carrera}.")

# Otra subclase
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def presentarse(self):
        super().presentarse()
        print(f"Soy profesor y enseño la materia de {self.materia}.")

# Uso de las clases
persona = Persona("Juan Pérez", 40)
estudiante = Estudiante("Ana López", 20, "Ingeniería")
profesor = Profesor("Carlos García", 50, "Matemáticas")

# Llamando a los métodos
persona.presentarse()
estudiante.presentarse()
profesor.presentarse()

