total = float(input("Ingresa el total de la compra: "))

if total > 100:
    descuento = total * 0.10
    total_final = total - descuento
    print("Total con descuento:", total_final)
else:
    print("Total a pagar:", total)