#Metodo de Polimorfismo
# Clases base y derivadas con métodos del mismo nombre

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau!"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu!"

# Función que demuestra el polimorfismo
def reproducir_sonido(animal):
    print(animal.hacer_sonido())

# Uso del polimorfismo
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    reproducir_sonido(animal)
