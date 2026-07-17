import os
import qrcode

# 1. Definimos el enlace
url_destino = "https://www.google.com"

# 2. Generamos el código QR básico
imagen_qr = qrcode.make(url_destino)

# 3. Obtenemos la ruta de la carpeta donde está ESTE archivo de Python
carpeta_actual = os.path.dirname(os.path.abspath(__file__))

# 4. Creamos la ruta completa para la imagen
ruta_guardado = os.path.join(carpeta_actual, "mi_primer_qr.png")

# 5. Guardamos la imagen en esa ruta
imagen_qr.save(ruta_guardado)

print(f"¡Código QR generado con éxito!")
print(f"Se guardó exactamente en: {ruta_guardado}")
