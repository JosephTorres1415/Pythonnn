producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad: "))

total = precio * cantidad

print("----- RESUMEN DE COMPRA -----")
print("Producto:", producto)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Total a pagar:", total)