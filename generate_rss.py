import os
from datetime import datetime

# CONFIGURACIÓN
BASE_URL = "https://www.firepartshub.com/"
RSS_FILENAME = "rss.xml"
TITLE = "Fire Alarm Parts Hub"
DESCRIPTION = "New fire alarm parts added to our catalog."

def generate_rss():
    # Encabezado del XML
    rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>{TITLE}</title>
 <description>{DESCRIPTION}</description>
 <link>{BASE_URL}</link>
 <lastBuildDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>
"""
    
    # Busca todos los archivos .html en la carpeta
    files = [f for f in os.listdir('.') if f.endswith('.html') and "yandex" not in f and "pinterest" not in f]
    
    # Limitar a los ultimos 50 o 100 para no hacer un RSS gigante (opcional, Pinterest lee hasta 50-100 items nuevos)
    # files = files[:100] 

    for filename in files:
        # Crea un título legible basado en el nombre del archivo
        # Ejemplo: "000-xc60-s80.html" -> "000 xc60 s80"
        title = filename.replace(".html", "").replace("-", " ").capitalize()
        link = BASE_URL + filename
        
        rss_content += f""" <item>
  <title>{title}</title>
  <link>{link}</link>
  <description>New part available: {title}</description>
  <guid>{link}</guid>
 </item>
"""

    # Cierre del XML
    rss_content += """</channel>
</rss>"""

    with open(RSS_FILENAME, "w", encoding="utf-8") as f:
        f.write(rss_content)
    print(f"Archivo {RSS_FILENAME} generado exitosamente con {len(files)} items.")

if __name__ == "__main__":
    generate_rss()