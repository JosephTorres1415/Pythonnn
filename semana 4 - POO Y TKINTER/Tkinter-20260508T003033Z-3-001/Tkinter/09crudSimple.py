import tkinter as tk

def agregar():
    lista.insert(tk.END, entrada.get())
    entrada.delete(0, tk.END)

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Agregar", command=agregar)
boton.pack()

lista = tk.Listbox(ventana)
lista.pack()

ventana.mainloop()