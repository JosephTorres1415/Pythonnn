# ======================================
# Programa 2: Clase Producto
# ======================================

class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Métodos get
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # Métodos set
    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("El stock no puede ser negativo.")

    # Método para aplicar un descuento
    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje < 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
            print(f"Descuento del {porcentaje}% aplicado correctamente.")
        else:
            print("Porcentaje inválido.")

    # Método para mostrar detalles del producto
    def mostrar_info(self):
        print(f"Producto: {self.__nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Stock disponible: {self.__stock}")
        print("-" * 30)


# ======= Ejemplo de uso =======
producto1 = Producto("Laptop HP", 15000, 10)
producto1.mostrar_info()

producto1.aplicar_descuento(10)
producto1.mostrar_info()
