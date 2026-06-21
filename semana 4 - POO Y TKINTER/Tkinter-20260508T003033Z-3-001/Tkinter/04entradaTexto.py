import tkinter as tk

def mostrar_texto():
    print(entrada.get())

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack()

ventana.mainloop()