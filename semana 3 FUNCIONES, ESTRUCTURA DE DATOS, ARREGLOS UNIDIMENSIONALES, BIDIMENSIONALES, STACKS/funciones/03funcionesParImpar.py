#Número par o impar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Ingresa un número: "))
if es_par(num):
    print("Es par")
else:
    print("Es impar")