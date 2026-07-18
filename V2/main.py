import os
import qrcode

# 1. Definimos la información y los colores que queremos
url_destino = "https://www.google.com"

# Puedes usar nombres de colores en inglés o códigos HEX (#RRGGBB)
color_qr = "#6E8B3D"      # Un verde elegante
color_fondo = "#F2F1EB"   # Un blanco tipo arena

# 2. Configuramos los parámetros avanzados del QR
qr = qrcode.QRCode(
    version=1,                           # Tamaño de la matriz (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección bajo (suficiente para cambios de color)
    box_size=15,                         # Tamaño de cada cuadrito en píxeles (más alto = mayor resolución)
    border=4                             # Grosor del borde/margen de seguridad
)

# 3. Añadimos los datos al objeto QR
qr.add_data(url_destino)
qr.make(fit=True)

# 4. Generamos la imagen aplicando nuestros colores personalizados
imagen_disenada = qr.make_image(
    fill_color=color_qr, 
    back_color=color_fondo
)

# 5. Buscamos la carpeta actual para guardar la imagen justo al lado del script
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_guardado = os.path.join(carpeta_actual, "qr_personalizado.png")

# 6. Guardamos la imagen
imagen_disenada.save(ruta_guardado)

print("¡Código QR Personalizado Generado!")
print(f"Color QR: {color_qr} | Color Fondo: {color_fondo}")
print(f"Guardado en: {ruta_guardado}")
