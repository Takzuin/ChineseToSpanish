from googletrans import Translator
import tkinter as tk
from tkinter import messagebox, font

# Función para traducir texto
def traducir():
    texto = entrada_texto.get("1.0", "end-1c")
    if texto:
        try:
            traduccion = traductor.translate(texto, src='zh-cn', dest='es')
            salida_texto.delete("1.0", "end")
            salida_texto.insert("end", traduccion.text)
        except Exception as e:
            messagebox.showerror("Error", "Error al traducir el texto. Inténtalo de nuevo.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce el texto que deseas traducir.")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Traductor Chino-Español")
ventana.geometry("500x400")

# Centrar la ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')

# Definir fuentes y colores
fuente_titulo = font.Font(family='Helvetica', size=16, weight='bold')
fuente_texto = font.Font(family='Helvetica', size=12)
color_fondo = "#f0f0f0"
color_boton = "#4CAF50"
color_texto_boton = "#ffffff"

ventana.configure(bg=color_fondo)

# Crear marcos (frames) para una mejor organización
frame_entrada = tk.Frame(ventana, bg=color_fondo)
frame_entrada.pack(pady=10)

frame_botones = tk.Frame(ventana, bg=color_fondo)
frame_botones.pack(pady=10)

frame_salida = tk.Frame(ventana, bg=color_fondo)
frame_salida.pack(pady=10)

# Widgets de la interfaz
label_titulo = tk.Label(ventana, text="Traductor Chino-Español", font=fuente_titulo, bg=color_fondo)
label_titulo.pack(pady=10)

label_entrada = tk.Label(frame_entrada, text="Texto en Chino:", font=fuente_texto, bg=color_fondo)
label_entrada.pack(anchor='w')

entrada_texto = tk.Text(frame_entrada, height=5, width=50, font=fuente_texto)
entrada_texto.pack(pady=5)

boton_traducir = tk.Button(frame_botones, text="Traducir", command=traducir, font=fuente_texto, bg=color_boton, fg=color_texto_boton)
boton_traducir.pack()

label_salida = tk.Label(frame_salida, text="Traducción en Español:", font=fuente_texto, bg=color_fondo)
label_salida.pack(anchor='w')

salida_texto = tk.Text(frame_salida, height=5, width=50, font=fuente_texto)
salida_texto.pack(pady=5)

# Inicializar el traductor
traductor = Translator()

# Iniciar la aplicación
ventana.mainloop()
