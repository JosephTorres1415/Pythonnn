import pooLib33

class UsuariosPremium(pooLib33.Usuario):
    def __init__(self, id, alias, nombre, apellidos,sorteos, puntos):
        super().__init__(id, alias, nombre, apellidos)
        self.sorteos=sorteos
        self.puntos=puntos

    def muestra_datos(self):
        print('\n\n')
        super().muestra_datos()
        print(f'Tienes {self.puntos} puntos para canjear en premios')
        print(f'Tienes derecho a participar en {self.sorteos} sorteos')

#crearemos la instancia de un objeto de clase UsuariosPremium
id=input('ID de usuario: ')
alias=input('Alias: ')
nombre=input('Nombre: ')
apellidos=input('Apellidos: ')
sorteos=25
puntos=500
userPremium=UsuariosPremium(id,alias,nombre,apellidos,sorteos,puntos)
userPremium.muestra_datos()