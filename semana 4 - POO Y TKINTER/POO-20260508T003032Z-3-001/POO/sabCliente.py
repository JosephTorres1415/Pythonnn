# ======================================
# Programa 1: Clase Cliente
# ======================================

class Cliente:
    def __init__(self, nombre, correo, telefono):
        # Atributos privados
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Métodos get
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Métodos set
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_correo(self, correo):
        self.__correo = correo

    def set_telefono(self, telefono):
        self.__telefono = telefono

    # Método para mostrar información
    def mostrar_info(self):
        print(f"Cliente: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")
        print("-" * 30)


# ======= Ejemplo de uso =======
cliente1 = Cliente("Ana López", "ana.lopez@example.com", "555-1234")
cliente1.mostrar_info()

# Modificamos un dato
cliente1.set_correo("ana.actualizado@example.com")
print("Correo actualizado:", cliente1.get_correo())
