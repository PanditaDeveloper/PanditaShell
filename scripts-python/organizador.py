import os
import shutil

# Ruta que deseas limpiar (puedes cambiarla por tu carpeta de Descargas)
# Usamos os.path.expanduser para que apunte automáticamente a tu usuario
ruta_origen = os.path.expanduser("~/Downloads")

# Diccionario con las extensiones y sus carpetas destino
formatos = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Instaladores": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".7z"]
}

print("Iniciando el ordenamiento de: " + ruta_origen)

# Revisar los archivos en la carpeta
for archivo in os.listdir(ruta_origen):
    ruta_archivo = os.path.join(ruta_origen, archivo)
    
    # Ignorar si es una carpeta
    if os.path.isdir(ruta_archivo):
        continue
        
    # Obtener la extensión del archivo
    nombre, extension = os.path.splitext(archivo)
    extension = extension.lower()
    
    # Buscar a qué carpeta pertenece
    for carpeta, extensiones in formatos.items():
        if extension in extensiones:
            ruta_destino = os.path.join(ruta_origen, carpeta)
            
            # Crear la carpeta si no existe
            if not os.path.exists(ruta_destino):
                os.makedirs(ruta_destino)
                
            # Mover el archivo
            shutil.move(ruta_archivo, os.path.join(ruta_destino, archivo))
            print(f"Movido: {archivo} -> {carpeta}")

print("¡Proceso terminado, Pandita Dev!")
