import tkinter as tk

def saludar():
    print("Hola desde el botón")

ventana = tk.Tk()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()