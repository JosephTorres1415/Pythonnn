import tkinter as tk

ventana = tk.Tk()

frame = tk.Frame(ventana)
frame.pack()

tk.Label(frame, text="Usuario").grid(row=0, column=0)
tk.Entry(frame).grid(row=0, column=1)

tk.Label(frame, text="Contraseña").grid(row=1, column=0)
tk.Entry(frame, show="*").grid(row=1, column=1)

tk.Button(frame, text="Login").grid(row=2, columnspan=2)

ventana.mainloop()