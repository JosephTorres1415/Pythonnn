# ======================================
# Programa 3: Clase Venta
# ======================================
import sabCliente
import sabProducto
class Venta:
    def __init__(self, sabCliente, sabProducto, cantidad):
        self.__cliente = cliente
        self.__producto = producto
        self.__cantidad = cantidad
        self.__total = 0.0

    # Métodos get
    def get_cliente(self):
        return self.__cliente

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def get_total(self):
        return self.__total

    # Métodos set
    def set_cantidad(self, cantidad):
        if cantidad > 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad debe ser positiva.")

    # Método para calcular el total
    def calcular_total(self):
        precio_producto = self.__producto.get_precio()
        self.__total = precio_producto * self.__cantidad
        return self.__total

    # Método para mostrar detalles de la venta
    def mostrar_venta(self):
        print(f"Cliente: {self.__cliente.get_nombre()}")
        print(f"Producto: {self.__producto.get_nombre()}")
        print(f"Cantidad: {self.__cantidad}")
        print(f"Total: ${self.__total:.2f}")
        print("=" * 40)


# ======= Ejemplo de uso =======
# Reutilizamos clases anteriores
cliente = sabCliente.Cliente("Carlos Pérez", "carlos.perez@example.com", "555-9876")
producto = sabProducto.Producto("Teléfono Samsung", 8500, 5)

# Creamos la venta
venta1 = Venta(cliente, producto, 2)
venta1.calcular_total()
venta1.mostrar_venta()
