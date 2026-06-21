import tkinter as tk

ventana = tk.Tk()

lista = tk.Listbox(ventana)
lista.pack()

for item in ["Python", "Java", "C++", "JavaScript"]:
    lista.insert(tk.END, item)

ventana.mainloop()