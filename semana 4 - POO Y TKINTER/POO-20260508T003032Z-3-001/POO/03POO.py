#crearemos una clase que manipula información de vehiculos
#usaremos un método para imprimir su ficha técnica
class Vehiculo:
    def __init__(self,marca, tipo, modelo, color):
        self.marca=marca
        self.tipo=tipo
        self.modelo=modelo
        self.color=color
    
    def ficha_tecnica(self):
        print('\n---FICHA TÉCNICA DEL VEHICULO---\n')
        print('Marca:',self.marca)
        print('Tipo:',self.tipo)
        print('Modelo:',self.modelo)
        print('Color:',self.color)
#inicia el programa
vehiculo=Vehiculo('Toyota','Tacoma',2025,'Blanco')
vehiculo.ficha_tecnica()
marca=input('Escribe la marca del vehiculo: ')
tipo=input('Tipo de vehiculo: ')
modelo=input('Modelo de vehiculo: ')
color=input('Color de vehiculo: ')
input('Presiona enter para continuar...')
vehiculo2=Vehiculo(marca,tipo,modelo,color)
vehiculo2.ficha_tecnica()

#encapsulamiento (se refiere al nivel de acceso que puede tener una 
# variable) 

__costoDolar=19.5       #esto indica que no deberíamos modificar este valor
_nombreMoneda='dolar'   #indica que solo algunas personas puede modificar
                        #el valor
ganancia=1.5            #indica que cualquiera puede modificar la variable
'''python no bloquea el acceso a las variables, esto sería tarea del 
programador, más bien python confia en tus buenas prácticas de programación
y en que NO HARAS MAL USO DE ESAS VARIABLES'''