numero = int(input("Ingresa un número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("El factorial es:", factorial)