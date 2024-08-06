from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Cargar la imagen plantilla
plantilla = Image.open('fondo.jpg')  # Asegúrate de que el archivo esté en el mismo directorio

# Obtener el número del día del mes actual
fecha_actual = datetime.now()
# Formatear la fecha en el formato "día-mes-año"
dia_del_mes = fecha_actual.strftime("%d-%m-%Y")

# Crear un objeto ImageDraw para dibujar sobre la imagen
draw = ImageDraw.Draw(plantilla)

# Cargar una fuente (puedes cambiar el tamaño de la fuente y la ruta según lo necesites)
try:
    fuente = ImageFont.truetype("arialbd.ttf", 36)  # Arial Bold
except IOError:
    fuente = ImageFont.load_default()  # Usar fuente predeterminada si no se puede cargar

# Especificar la posición y el color del texto (RGB)
posicion = (50, 50)  # Cambia según la ubicación deseada
color = (255, 255, 255)  # Rojo, puedes cambiar el color según lo necesites

# Dibujar el texto sobre la imagen
draw.text(posicion, str(dia_del_mes), font=fuente, fill=color)

# Guardar la imagen resultante
plantilla.save('resultado.png')

print('Imagen procesada y guardada como resultado.png')
