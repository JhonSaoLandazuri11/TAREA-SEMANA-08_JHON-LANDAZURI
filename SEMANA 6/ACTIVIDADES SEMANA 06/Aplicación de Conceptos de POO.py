#Este ejercicio debe cincluir los siguientes elementos:
#Al menos una clase base y una clase derivada, demo strando el concepto de herencia.
#Implementación de encapsulación en al menos una clase.
#Un ejemplo de polimorfismo, ya sea a través de métodos sobrescritos o utilizando argumentos múltiples/variables.

class Vehiculo:
    def __init__(self, marca, modelo, año,):
        self._marca = marca # Atributo privado
        self._modelo = modelo
        self._año = año
        

    # Métodos getter y setter para encapsulación
    def get_marca(self):
        return self._marca

    def set_marca(self, nueva_marca):
        self._marca = nueva_marca
    
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo 

    def get_info(self):
        """Metodó común para conseguir la información de un vehículo"""
        return f"{self._marca} {self._modelo}, Año: {self._año}."
    
    def avanzar(self):
        return f"El vehículo {self._marca} esta en optimas condiciones, esta en movimiento."
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_combustible):
        super().__init__(marca, modelo, año)
        self.tipo_combustible = tipo_combustible # Atributo específico de Coche

    # Sobrescritura de método (polimorfismo)
    def avanzar (self):
        return f"El vehículo {self._marca} está avanzando en modo {self.tipo_combustible}."

    # Polimorfismo con un método que maneja múltiples argumentos
    def carga_combustible(self, cantidad, tipo=None):
        if tipo:
            return f"Se ha cargado {cantidad} litros de {tipo}."
        return f"Se ha cargado {cantidad} litros."
    
        
# Imprimir el Uso del código
if __name__ == "__main__":
    #Instancia del vehículo
    vehiculo = Vehiculo("Mazda","3", 2018)
    print(vehiculo.get_info())
    print(vehiculo.avanzar())

    #Instancia del coche
    coche = Coche ("Chevrolet","Sail",2024, "Manual.")
    print(coche.get_info())
    print(coche.avanzar())

    # Polimorfismo con método que maneja múltiples argumentos
    print(coche.carga_combustible(50, "Manual"))
    print(coche.carga_combustible(40))



