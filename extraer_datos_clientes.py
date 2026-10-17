import os
import requests
import json

def extraer_y_guardar_clientes(): 

    url = "https://dummyjson.com/users"

    print(f"🌐 Conectándome a la API: {url}...")
    response = requests.get(url)

    # Validamos que la extracción fue exitosa
    if response.status_code == 200:
        print("✅ Datos extraídos correctamente.")
        # Aquí puedes agregar el código para guardar o transformar el JSON
        datos_json = response.json()

        os.makedirs("data/raw", exist_ok=True)

        archivo_salida = "data/raw/clientes_raw.json" 

        with open(archivo_salida, "w", encoding="utf-8") as f:
            json.dump(datos_json, f, ensure_ascii=False, indent=4)
                    
        print(f"💾 ¡Datos crudos guardados con éxito en: {archivo_salida}!")
              # Verificamos cuántos productos se guardaron
              # Verificamos cuántos clientes/usuarios se guardaron
        usuarios = datos_json.get('users', [])
        print(f"📦 Total de usuarios guardados: {len(usuarios)}")

        
    else:
        print(f"❌ Error al conectar: {response.status_code}")



        

   

extraer_y_guardar_clientes()  