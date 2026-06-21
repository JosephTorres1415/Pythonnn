def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir entre cero"

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("Resultado:", dividir(num1, num2))