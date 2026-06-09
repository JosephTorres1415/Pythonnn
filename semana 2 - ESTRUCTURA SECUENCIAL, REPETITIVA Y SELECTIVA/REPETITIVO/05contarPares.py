contador = 0

for i in range(1, 51):
    if i % 2 == 0:
        contador += 1

print("Cantidad de números pares:", contador)

"""
contar impares
contador_impares = 0

for i in range(5):
    try:
        numero = int(input("Ingresa un número: "))

        if numero % 2 != 0:
            contador_impares += 1

    except ValueError:
        print("Error: debes ingresar un número entero")

print("Cantidad de números impares:", contador_impares)
"""