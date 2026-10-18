import os
import requests
import json

def extraer_y_guardar_carrito():
    url = "https://dummyjson.com/carts"
    
    print(f"🌐 Conectándome a la API: {url}...")
    response = requests.get(url)
    
    # Validamos que la extracción fue exitosa (alineado con la variable 'url')
    if response.status_code == 200:
        print("✅ Datos extraídos correctamente.")
        datos_json = response.json()

        os.makedirs("data/raw", exist_ok=True)
        archivo_salida = "data/raw/carrito_raw.json" 

        with open(archivo_salida, "w", encoding="utf-8") as f:
            json.dump(datos_json, f, ensure_ascii=False, indent=4)
                    
        print(f"💾 ¡Datos crudos guardados con éxito en: {archivo_salida}!")
             
        carrito = datos_json.get('carts', [])
        print(f"📦 Total de carts guardados: {len(carrito)}")
    else:
        # Corregido para que se alinee perfectamente dentro del else
        print(f"❌ Error al conectar: {response.status_code}")

# Llamada al ras del margen izquierdo y usando el nombre correcto de la función
extraer_y_guardar_carrito()
