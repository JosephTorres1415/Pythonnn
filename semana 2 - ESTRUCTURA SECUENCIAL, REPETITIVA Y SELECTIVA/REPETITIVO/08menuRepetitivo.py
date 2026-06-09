opcion = 0

while opcion != 3:
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print("Adiós")

print("Programa terminado")

"""
con while True
while True:
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    
    try:
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            print("Hola")
        elif opcion == 2:
            print("Adiós")
        elif opcion == 3:
            print("Programa terminado")
            break
        else:
            print("Opción no válida")

    except ValueError:
        print("Error: debes ingresar un número")
        
"""