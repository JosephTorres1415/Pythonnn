num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
opcion = int(input("Elige operación (1 suma, 2 resta, 3 multiplicación, 4 división): "))

if opcion == 1:
    print("Resultado:", num1 + num2)
elif opcion == 2:
    print("Resultado:", num1 - num2)
elif opcion == 3:
    print("Resultado:", num1 * num2)
elif opcion == 4:
    print("Resultado:", num1 / num2)
else:
    print("Opción no válida")