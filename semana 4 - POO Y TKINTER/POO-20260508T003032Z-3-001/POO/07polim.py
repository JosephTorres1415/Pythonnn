# Clase base
class Empleado:
    def calcular_pago(self):
        raise NotImplementedError("Cada tipo de empleado debe implementar este método")

# Clases hijas
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcular_pago(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, horas, pago_por_hora):
        self.horas = horas
        self.pago_por_hora = pago_por_hora

    def calcular_pago(self):
        return self.horas * self.pago_por_hora

class EmpleadoFreelance(Empleado):
    def __init__(self, proyectos):
        self.proyectos = proyectos

    def calcular_pago(self):
        return sum(self.proyectos)

# Lista de empleados (polimorfismo)
empleados = [
    EmpleadoTiempoCompleto(15000),
    EmpleadoPorHoras(40, 100),
    EmpleadoFreelance([2000, 3500, 1500])
]

# Recorrido
for emp in empleados:
    print("Pago:", emp.calcular_pago())