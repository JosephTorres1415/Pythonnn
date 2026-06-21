#Crearemos la clase Triangulo, con una función para calcular el área
class Triangulo:#creamos la clase
    #definimos el constructor
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):#definimos la función área
        return (self.base * self.altura)/2
    
#inicia nuestro programa
base=float(input('Escribe la base del triangulo: '))
altura=float(input('Escribe la altura del triangulo: '))
#ahora construiremos el objeto
triangulo=Triangulo(base,altura)
base=float(input('Escribe la base del triangulo: '))
altura=float(input('Escribe la altura del triangulo: '))
triangulo2=Triangulo(base,altura)
base=float(input('Escribe la base del triangulo: '))
altura=float(input('Escribe la altura del triangulo: '))
triangulo3=Triangulo(base,altura)
#invocamos el método area
print('El área del triangulo es:',triangulo.area())
print('El área del triangulo es:',triangulo2.area())
print('El área del triangulo es:',triangulo3.area())