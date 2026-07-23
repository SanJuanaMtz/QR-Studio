import os
import qrcode
from PIL import Image

# 1. Definir la ruta base del archivo
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# 2. Configurar los parámetros del QR
url_destino = "https://www.instagram.com/journeysbysan?igsh=MTRsYWRlZ3lyenM1Yg=="
color_qr = "#6E8B3D"       # Un verde elegante
color_fondo = "#F2F1EB"   # Un blanco tipo arena

# 3. Crear el objeto QRCode con Alta Corrección de Errores (ERROR_CORRECT_H)
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # ¡Clave para que funcione con logo!
    box_size=15,
    border=4,
)

# Agregar la URL y generar la matriz
qr.add_data(url_destino)
qr.make(fit=True)

# Crear la imagen base del QR
imagen_qr = qr.make_image(fill_color=color_qr, back_color=color_fondo).convert('RGB')

# 4. Procesar e insertar el Logotipo
ruta_logo = os.path.join(directorio_actual, "logo.png") # Asegúrate de tener logo.png en tu carpeta

if os.path.exists(ruta_logo):
    logo = Image.open(ruta_logo)
    
    # Redimensionar el logo para que no ocupe más del 20% del área del QR
    ancho_qr, alto_qr = imagen_qr.size
    tamaño_max_logo = int(ancho_qr * 0.30) # 22% del tamaño total, por endes de proteccion se configura un tamaño maximo de 30%
    
    logo.thumbnail((tamaño_max_logo, tamaño_max_logo), Image.Resampling.LANCZOS)
    
    # Calcular la posición central
    pos_x = (ancho_qr - logo.size[0]) // 2
    pos_y = (alto_qr - logo.size[1]) // 2
    
    # Pegar el logo en el QR (respetando transparencias si es PNG)
    if logo.mode == 'RGBA':
        imagen_qr.paste(logo, (pos_x, pos_y), logo)
    else:
        imagen_qr.paste(logo, (pos_x, pos_y))
    
    print("✅ Logotipo insertado con éxito.")
else:
    print("⚠️ No se encontró 'logo.png'. Se generará el QR sin logo.")

# 5. Guardar el archivo final
ruta_salida = os.path.join(directorio_actual, "qr_con_logo.png")
imagen_qr.save(ruta_salida)

print(f"🎉 ¡QR con logo guardado en: {ruta_salida}")
