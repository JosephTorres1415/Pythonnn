#crearemos la clase un objeto normales para ejemplificar la creación de
#librerías
class Usuario:
    def __init__(self,id,alias,nombre, apellidos):
        self.id=id
        self.alias=alias
        self.nombre=nombre
        self.apellidos=apellidos

    def muestra_datos(self):
        print('Datos del Cliente:')
        print('Id:',self.id)
        print('Alias',self.alias)
        print('Nombre:',self.nombre)
        print('Apellidos:',self.apellidos)

#probaremos, creando un objeto y usando su método, este código se debe
#comentar despues de probar
#user=Usuario(13,'Fer','Fernando','Cruz')
#user.muestra_datos()