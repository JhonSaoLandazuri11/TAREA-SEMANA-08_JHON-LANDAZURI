#Ejercicio N1
#Tienda de Productos Sencilla

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append(Producto(nombre, precio))

    def mostrar_productos(self):
        print("Productos en la tienda:")
        for prod in self.productos:
            print(f"{prod.nombre}, Precio: ${prod.precio}")


# Crear tienda y productos
tienda = Tienda("Tienda Simplificada")
tienda.agregar_producto("Laptop", 1000)
tienda.agregar_producto("Mouse", 20)

# Mostrar productos
tienda.mostrar_productos()
