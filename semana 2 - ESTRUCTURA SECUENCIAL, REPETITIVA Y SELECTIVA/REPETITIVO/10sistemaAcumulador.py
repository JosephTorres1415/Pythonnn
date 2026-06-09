
total = 0

precio = float(input("Ingresa el precio del producto (0 para terminar): "))

while precio != 0:
    total += precio
    precio = float(input("Ingresa el precio del producto (0 para terminar): "))

print("Total a pagar:", total)

"""
con while True
total = 0

while True:
    try:
        precio = float(input("Ingresa el precio del producto (0 para terminar): "))

        if precio == 0:
            break

        total += precio

    except ValueError:
        print("Error: debes ingresar un número válido")

print("Total a pagar:", total)"""