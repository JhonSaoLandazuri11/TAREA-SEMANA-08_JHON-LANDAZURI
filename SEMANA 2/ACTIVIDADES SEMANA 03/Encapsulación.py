#Metodo de Encapsulación

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado ${cantidad}. Nuevo saldo: ${self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado ${cantidad}. Nuevo saldo: ${self.__saldo}")
        else:
            print("Cantidad inválida o saldo insuficiente.")

    def obtener_saldo(self):
        # Método público para acceder al saldo
        return self.__saldo

    def __str__(self):
        # Método para representar el objeto como cadena
        return f"Cuenta de {self.__titular}, Saldo: ${self.__saldo}"

# Uso de la clase
cuenta = CuentaBancaria("Juan Pérez", 500)

print(cuenta)  # Cuenta de Juan Pérez, Saldo: $500
cuenta.depositar(200)  # Se han depositado $200. Nuevo saldo: $700
cuenta.retirar(100)    # Se han retirado $100. Nuevo saldo: $600

# Intento de acceder directamente a los atributos privados (no permitido)
# print(cuenta.__saldo)  # AttributeError: 'CuentaBancaria' object has no attribute '__saldo'

# Acceso al saldo mediante el método público
print(f"Saldo actual: ${cuenta.obtener_saldo()}")  # Saldo actual: $600
