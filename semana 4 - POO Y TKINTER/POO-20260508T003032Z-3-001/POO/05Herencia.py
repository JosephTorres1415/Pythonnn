#crearemos una super clase llamada figura, con un atributo color y
#un método dibujar
class Figura:
    def __init__(self,color):
        self.color=color

    def dibujar(self):
        print(f'Estamos dibujando una figura de color: {self.color}')
#crearemos la subclase llamada Rectángulo que hereda de figura
class Rectangulo(Figura):#Rectangulo hereda de Figura
    def __init__(self,color,ancho, alto):
        super().__init__(color)#el atributo esta inicializado en la super clase
        self.ancho=ancho
        self.alto=alto
    
    def calcular_area(self):
        return self.alto*self.ancho

class Circulo(Figura):
    def __init__(self, color,radio):
        super().__init__(color)
        self.radio=radio
    
    def calcular_area(self):
        return 3.14*(self.radio**2)
    
#comienza nuestro programa
#construiremos los objetos
miRectangulo=Rectangulo('Azul',9.3,13.7)
miCirculo=Circulo('Amarillo',21.6)
#usaremos los métodos de la clase Rectángulo
miRectangulo.dibujar()
print('El área del rectangulo es:',miRectangulo.calcular_area())
miCirculo.dibujar()
print('El área del circulo es:',miCirculo.calcular_area())