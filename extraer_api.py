import os
import requests
import json

def extraer_y_guardar_productos():
    url = "https://dummyjson.com/products"
    
    print(f"🌐 Conectándome a la API: {url}...")
    response = requests.get(url)

    print(f"📡 Código de respuesta HTTP: {response.status_code}")

    if response.status_code == 200:
        print("✅ ¡Conexión exitosa con la API!")
        
        # 1. Convertimos la respuesta a un diccionario de Python (JSON)
        datos_json = response.json()
        
        # 2. Creamos la carpeta 'data/raw' automáticamente si no existe
        # (os.makedirs se encarga de crear las carpetas en tu computadora)
        os.makedirs("data/raw", exist_ok=True)
        
        # 3. Definimos la ruta donde vamos a guardar el archivo crudo
        archivo_salida = "data/raw/productos_raw.json"
        
        # 4. Guardamos el diccionario completo en un archivo JSON local
        with open(archivo_salida, "w", encoding="utf-8") as f:
            json.dump(datos_json, f, ensure_ascii=False, indent=4)
            
        print(f"💾 ¡Datos crudos guardados con éxito en: {archivo_salida}!")
        
        # Verificamos cuántos productos se guardaron
        productos = datos_json.get('products', [])
        print(f"📦 Total de productos guardados: {len(productos)}")
        
    else:
        print("❌ Error al conectarse a la API.")

if __name__ == "__main__":
    extraer_y_guardar_productos()