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
ventana.title(" ")
ventana.geometry("500x400")

# Cambiar el icono de la ventana
ventana.iconbitmap('C:/Python/TraductorDeChino/china.ico')  # Asegúrate de que la ruta al archivo .ico sea correcta

# Centrar la ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')

# Definir fuentes y colores
fuente_general = font.Font(family='System', size=14)
color_fondo = "#EE1C25"
color_boton = "#cec30f"
color_texto_boton = "#000000"  # Cambiado a negro
color_barra_titulo = "#cec30f"  # Color de la barra de título personalizada
color_texto_barra_titulo = "#FFFFFF"  # Color del texto en la barra de título

ventana.configure(bg=color_fondo)

# Crear una barra de título personalizada
barra_titulo = tk.Frame(ventana, bg=color_barra_titulo, relief='raised', bd=2)
barra_titulo.pack(side='top', fill='x')

label_titulo = tk.Label(barra_titulo, text="Traductor Chino-Español", font=font.Font(family='System', size=20), bg=color_barra_titulo, fg=color_texto_barra_titulo)
label_titulo.pack(side='left', padx=10)

# Crear marcos (frames) para una mejor organización
frame_entrada = tk.Frame(ventana, bg=color_fondo)
frame_entrada.pack(pady=10)

frame_botones = tk.Frame(ventana, bg=color_fondo)
frame_botones.pack(pady=11)

frame_salida = tk.Frame(ventana, bg=color_fondo)
frame_salida.pack(pady=10)

# Widgets de la interfaz
label_entrada = tk.Label(frame_entrada, text="Texto en Chino:", font=font.Font(family='System', size=17), bg=color_fondo)
label_entrada.pack(anchor='w')

entrada_texto = tk.Text(frame_entrada, height=5, width=50, font=fuente_general)
entrada_texto.pack(pady=5)

boton_traducir = tk.Button(frame_botones, text="Traducir", command=traducir, font=font.Font(family='System', size=16), bg=color_boton, fg=color_texto_boton)
boton_traducir.pack()

label_salida = tk.Label(frame_salida, text="Traducción en Español:", font=font.Font(family='System', size=17), bg=color_fondo)
label_salida.pack(anchor='w')

salida_texto = tk.Text(frame_salida, height=5, width=50, font=font.Font(family='System', size=16))
salida_texto.pack(pady=5)

# Inicializar el traductor
traductor = Translator()

# Iniciar la aplicación
ventana.mainloop()
