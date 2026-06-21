import tkinter as tk

def agregar():
    lista.insert(tk.END, entrada.get())
    entrada.delete(0, tk.END)

def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)

ventana = tk.Tk()
ventana.title("Gestor de tareas")

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Agregar", command=agregar).pack()
tk.Button(ventana, text="Eliminar", command=eliminar).pack()

lista = tk.Listbox(ventana)
lista.pack()

ventana.mainloop()