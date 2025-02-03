# Desarrollar habilidades prácticas en la Programación Tradicional y la Programación Orientada a Objetos (POO) mediante la implementación de un programa en Python para determinar el promedio semanal del clima.
# Solución en Programación Tradicional

def ingresar_temperaturas_tradicional():
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas


def calcular_promedio_tradicional(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)


def main_tradicional():
    print("== Programa en Programación Tradicional ==")
    temperaturas = ingresar_temperaturas_tradicional()
    promedio = calcular_promedio_tradicional(temperaturas)

    print("\nTemperaturas ingresadas:", temperaturas)
    print(f"El promedio de la temperatura semanal es: {promedio:.2f}")

# Solución en Programación Orientada a Objetos (POO)

class ClimaSemana:
    def __init__(self):
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            while True:
                try:
                    temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.__temperaturas.append(temperatura)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_temperaturas(self):
        return self.__temperaturas


def main_poo():
    print("\n== Programa en Programación Orientada a Objetos (POO) ==")
    clima = ClimaSemana()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print("\nTemperaturas ingresadas:", clima.mostrar_temperaturas())
    print(f"El promedio de la temperatura semanal es: {promedio:.2f}")


# Programa principal que ejecuta ambas soluciones
if __name__ == "__main__":
    print("=== Comparación: Tradicional vs POO ===\n")
    
    # Ejecución en Programación Tradicional
    main_tradicional()

    # Ejecución en Programación Orientada a Objetos
    main_poo()
    