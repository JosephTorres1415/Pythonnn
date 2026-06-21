def tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingresa un número: "))
tabla(num)