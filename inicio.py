import tkinter as tk
from tkinter import ttk

from Proforma import abrir_proforma
ventana = tk.Tk()

ventana.title("Tangerine Unlimited")
ventana.geometry("600x450")
titulo = ttk.Label(
    ventana,
    text="Hola usuario, ¿qué desea realizar?",
    font=("Arial", 20, "bold")
)

titulo.pack(pady=50)
boton_proforma = ttk.Button(
    ventana,
    text="Proforma",
    command=abrir_proforma
)

boton_proforma.pack(pady=10)
boton_factura = ttk.Button(
    ventana,
    text="Factura",
    state="disabled"
)

boton_factura.pack(pady=10)


boton_empaque = ttk.Button(
    ventana,
    text="Lista de empaque",
    state="disabled"
)

boton_empaque.pack(pady=10)
ventana.mainloop()