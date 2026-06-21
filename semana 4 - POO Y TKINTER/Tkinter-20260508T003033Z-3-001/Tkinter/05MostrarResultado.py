import tkinter as tk

def mostrar():
    etiqueta.config(text=entrada.get())

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

boton = tk.Button(ventana, text="Actualizar", command=mostrar)
boton.pack()

ventana.mainloop()