#Aplicar los conocimientos adquiridos sobre tipos de datos, identificadores y convenciones de nomenclatura en Python para desarrollar un pequeño programa. El código será implementado en el IDE PyCharm o  Visual Studio Code y posteriormente publicado en el repositorio de GitHub de cada estudiante.
#Conversor de Unidades de Medida
# Conversor de Unidades de Medida
# Este programa permite convertir distintas unidades de medida: metros a centímetros, kilómetros a metros,

# Función para convertir metros a centímetros
def metros_a_centimetros(metros):
    return metros * 100

# Función para convertir kilómetros a metros
def kilometros_a_metros(kilometros):
    return kilometros * 1000

# Función para convertir centímetros a metros
def centimetros_a_metros(centimetros):
    return centimetros / 100

# Función para convertir metros a kilómetros
def metros_a_kilometros(metros):
    return metros / 1000

# Inicio del programa
print("Este programa convertirá Unidades de Medida")
print("¿Qué unidad de medida quieres convertir?: ")
print("1. Metros a centímetros")
print("2. Kilómetros a metros")
print("3. Centímetros a metros")
print("4. Metros a kilómetros")

# Solicita al usuario que seleccione una opción
try:
    opcion_seleccionada = int(input("\nSelecciona una opción (1-4): "))
    
    if opcion_seleccionada in [1, 2, 3, 4]:
        valor_a_convertir = float(input("Ingresa el valor que deseas convertir: "))
        
        if opcion_seleccionada == 1:
            resultado = metros_a_centimetros(valor_a_convertir)
            print(f"{valor_a_convertir} metros equivalen a {resultado} centímetros.")
        elif opcion_seleccionada == 2:
            resultado = kilometros_a_metros(valor_a_convertir)
            print(f"{valor_a_convertir} kilómetros equivalen a {resultado} metros.")
        elif opcion_seleccionada == 3:
            resultado = centimetros_a_metros(valor_a_convertir)
            print(f"{valor_a_convertir} centímetros equivalen a {resultado} metros.")
        elif opcion_seleccionada == 4:
            resultado = metros_a_kilometros(valor_a_convertir)
            print(f"{valor_a_convertir} metros equivalen a {resultado} kilómetros.")
    else:
        print("Opción inválida. Por favor, selecciona un número entre 1 y 4.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números solamente.")

