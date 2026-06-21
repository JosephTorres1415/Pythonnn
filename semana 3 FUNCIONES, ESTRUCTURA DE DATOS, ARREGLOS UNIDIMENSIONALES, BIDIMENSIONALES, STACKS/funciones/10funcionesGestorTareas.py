tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)

def mostrar_tareas():
    for i, t in enumerate(tareas):
        print(f"{i+1}. {t}")

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)

while True:
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        i = int(input("Número de tarea a eliminar: ")) - 1
        eliminar_tarea(i)
    elif opcion == "4":
        break