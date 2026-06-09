clave_correcta = "1234"
clave = ""

while clave != clave_correcta:
    clave = input("Ingresa la contraseña: ")

print("Acceso permitido")

"""
con 3 intentos
clave_correcta = "1234"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    clave = input("Ingresa la contraseña: ")

    if clave == clave_correcta:
        print("Acceso permitido")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta")

if intentos == max_intentos:
    print("Acceso bloqueado")
"""