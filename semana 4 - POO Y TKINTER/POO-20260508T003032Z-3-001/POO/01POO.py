#crearemos la clase Persona
class Persona:# inciamos la clase Persona
    #constructor de la clase (parte privada del objeto)
    def __init__(self, nombre, edad):#inicializamos el constructor
        self.nombre=nombre
        self.edad=edad

    #métodos(no retorna valores) o funciones(si retorna valores) 
    #(parte pública del objeto)
    def saludar(self):#inicia el método saludar
        print(f'Hola, mi nombre es: {self.nombre} y mi edad es: {self.edad}')

#inicia nuestro programa, crearemos los objetos de la clase Persona
persona1=Persona('Juan',25)
persona2=Persona('Ana',31)
print('Se construyeron 2 objetos, persona1 y persona2\n')
#accederemos a los atributos de estos objetos, de forma individual
print('El nombre de la persona1 es:',persona1.nombre)
print('La edad de la persona1 es:',persona1.edad)
print(f'El nombre de la persona2 es: {persona2.nombre} y su edad: {persona2.edad}')
#accederemos a los métodos de los objetos
persona1.saludar()
persona2.saludar()