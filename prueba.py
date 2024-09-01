import tkinter as tk
from tkinter import font

ventana = tk.Tk()
fuentes_disponibles = list(font.families())
ventana.destroy()

for fuente in fuentes_disponibles:
    print(fuente)
