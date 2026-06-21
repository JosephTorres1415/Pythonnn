#crearemos la super clase Animal, con el encabezado de una función o método
#pero sin el cuerpo, similar a las interfaces de java
class Animal:#creamos la clase Animal
    def comunicarse(self):#solo tiene el encabezado del método comunicarse
        raise NotImplementedError('La subclase debe implementar el'
                                  'método comunicarse()')
    
#crearemos las sub clases que heredarán el método comunicarse pero
#debe implementar su código de diferente forma, según les convenga
#es decir, harán polimorfismo
class Perro(Animal):
    def comunicarse(self):#pudieras conectar a una base de datos
        return 'Soy un perro y ladro, Guuaauuuu!!!'
    
class Gato(Animal):
    def comunicarse(self):#pudieras conectar a un servidor web
        return 'soy un gato y maullo, Miiaaauuuu!!!'
    
class Oso(Animal):
    def comunicarse(self):#pudieras conectar a una API
        return 'soy un oso y gruño, Gggrrrr!!!'

#como tenemos varios objetos, con métodos comunes, podemos meterlos en una
#lista
animales=[Perro(),Gato(),Oso()]
#ahora vamos a recorrer la lista
for animal in animales:#la variable animal, recorre la lista animales
    print(animal.comunicarse())
    input('Presiona enter para continuar...')
