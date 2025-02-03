#Metodo de Abstracción
#Utilizando el código de ejemplo como guía, Crea un nuevo repositorio en tu cuenta de GitHub para este ejercicio.

from abc import ABC, abstractmethod

# Clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        #Método abstracto que debe implementarse en las subclases
        pass
    
    def dormir(self):
        #Método concreto que pueden usar todas las subclases
        print("El animal está durmiendo.")

# Subclase que implementa el método abstracto
class vaca(Animal):
    def hacer_sonido(self):
        print("Muu!")

# Subclase que implementa el método abstracto
class gato(Animal):
    def hacer_sonido(self):
        print("Miau miau!")

# Uso de las clases
def animal_sonido_demo(animal: Animal):
    animal.hacer_sonido()
    animal.dormir()

# Instanciando objetos de las subclases
vaca = vaca()
gato = gato()

# Usando la función de demostración
animal_sonido_demo(vaca) 
animal_sonido_demo(gato) 
