producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio: "))
cantidad = int(input("Ingresa la cantidad: "))

total = precio * cantidad

if total > 500:
    descuento = total * 0.20
elif total > 200:
    descuento = total * 0.10
else:
    descuento = 0

total_final = total - descuento

print("Producto:", producto)
print("Total original:", total)
print("Descuento:", descuento)
print("Total a pagar:", total_final)