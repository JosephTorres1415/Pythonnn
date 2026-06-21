import tkinter as tk

def sumar():
    resultado = int(e1.get()) + int(e2.get())
    etiqueta.config(text=f"Resultado: {resultado}")

ventana = tk.Tk()

e1 = tk.Entry(ventana)
e1.pack()

e2 = tk.Entry(ventana)
e2.pack()

boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()