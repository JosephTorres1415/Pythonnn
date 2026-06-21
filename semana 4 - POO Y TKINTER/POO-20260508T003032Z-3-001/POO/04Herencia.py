#mostraremos como se comporta la herencia en python
#crearemos la super clase, clase base o clase padre
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def comer(self):
        print(f'{self.nombre} está comiendo...')#hasta aquí no hay herencia

#crearemos la sub clase, clase derivada o clase hija
class Perro(Animal):#la clase Perro hereda de la super clase Animal
    def __init__(self,nombre,raza):
        super().__init__(nombre)#declaración del atributo heredado
        self.raza=raza#declaración del atributo local
    
    def ladrar(self):
        print(f'{self.nombre} es de la raza {self.raza} y está ladrando...')
        #la clase Perro tiene 2 métodos: comer(que es heredado) y ladrar(que es propio)

#crearemos el objeto de clase Perro
print('Crearemos el objeto miPerro, de clase Perro\n'
      'que hereda atributos de la super clase Animal\n'
      'su nombre será Simba y su raza Labrador\n')
miPerro=Perro('Simba','Labrador')
miPerro.comer()#este método es de la super clase
miPerro.ladrar()#este método es de la sub clase