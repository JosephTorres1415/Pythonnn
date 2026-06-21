import sqlite3


def agregar_producto(conexion):
    try:
        cursor = conexion.cursor()

        print("\n--- AGREGAR PRODUCTO ---")
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría (ropa/zapatos): ")
        talla = input("Talla: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        cursor.execute("""
            INSERT INTO productos (nombre, categoria, talla, precio, stock)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, categoria, talla, precio, stock))

        conexion.commit()
        print("✅ Producto agregado correctamente")

    except ValueError:
        print("❌ Error: precio debe ser número y stock entero")
    except sqlite3.Error as e:
        print(f"❌ Error en la base de datos: {e}")



def listar_productos(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        print("\n--- LISTA DE PRODUCTOS ---")

        if not productos:
            print("📭 No hay productos registrados")
            return

        for producto in productos:
            print(f"""
ID: {producto[0]}
Nombre: {producto[1]}
Categoría: {producto[2]}
Talla: {producto[3]}
Precio: ${producto[4]}
Stock: {producto[5]}
---------------------------
""")

    except sqlite3.Error as e:
        print(f"❌ Error al listar productos: {e}")



def actualizar_producto(conexion):
    try:
        cursor = conexion.cursor()

        print("\n--- ACTUALIZAR PRODUCTO ---")
        id_producto = int(input("Ingresa el ID del producto a actualizar: "))

        # Verificar si existe
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print("❌ Producto no encontrado")
            return

        print("\n🔎 Producto actual:")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[2]}")
        print(f"Talla: {producto[3]}")
        print(f"Precio: ${producto[4]}")
        print(f"Stock: {producto[5]}")

        print("\n✏️ Ingresa los nuevos datos")

        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        talla = input("Nueva talla: ")
        precio = float(input("Nuevo precio: "))
        stock = int(input("Nuevo stock: "))

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, categoria = ?, talla = ?, precio = ?, stock = ?
            WHERE id = ?
        """, (nombre, categoria, talla, precio, stock, id_producto))

        conexion.commit()
        print("✅ Producto actualizado correctamente")

    except ValueError:
        print("❌ Error: precio debe ser número y stock entero")
    except sqlite3.Error as e:
        print(f"❌ Error en la base de datos: {e}")



def eliminar_producto(conexion):
    try:
        cursor = conexion.cursor()

        print("\n--- ELIMINAR PRODUCTO ---")
        id_producto = int(input("Ingresa el ID del producto a eliminar: "))

        # Verificar si existe
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print("❌ Producto no encontrado")
            return

        print("\n⚠️ Producto encontrado:")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[2]}")
        print(f"Precio: ${producto[4]}")

        confirmacion = input("¿Seguro que deseas eliminarlo? (s/n): ").lower()

        if confirmacion == "s":
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conexion.commit()
            print("🗑️ Producto eliminado correctamente")
        else:
            print("❎ Eliminación cancelada")

    except ValueError:
        print("❌ Error: el ID debe ser un número entero")
    except sqlite3.Error as e:
        print(f"❌ Error en la base de datos: {e}")



def conectar():
    try:
        conexion = sqlite3.connect("tienda.db")
        return conexion
    except sqlite3.Error as e:
        print(f"Error: {e}")

def crear_tabla(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                talla TEXT,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """)
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")

# 🧭 MENÚ PRINCIPAL
def mostrar_menu():
    print("\n===== TIENDA DEPORTIVA =====")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def main():
    conexion = conectar()
    conn = conectar()
    if conn:
        crear_tabla(conn)

        while True:
            mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                agregar_producto(conexion)
            elif opcion == "2":
                listar_productos(conexion)
            elif opcion == "3":
                actualizar_producto(conexion)
            elif opcion == "4":
                eliminar_producto(conexion)
            elif opcion == "5":
                print("👋 Saliendo del sistema...")
                break
            else:
                print("❌ Opción inválida, intenta de nuevo")

        conn.close()

if __name__ == "__main__":
    main()

