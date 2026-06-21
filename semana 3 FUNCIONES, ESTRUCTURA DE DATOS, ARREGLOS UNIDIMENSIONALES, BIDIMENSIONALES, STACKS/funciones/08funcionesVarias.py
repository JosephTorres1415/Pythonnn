def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def menu():
    print("1. Sumar")
    print("2. Restar")

menu()
opcion = int(input("Elige una opción: "))
a = int(input("Número 1: "))
b = int(input("Número 2: "))

if opcion == 1:
    print("Resultado:", suma(a, b))
elif opcion == 2:
    print("Resultado:", resta(a, b))