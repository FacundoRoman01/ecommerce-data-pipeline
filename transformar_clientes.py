import os
import json
import pandas as pd

def transformar_clientes():
    archivo_raw = "data/raw/clientes_raw.json"
    
    print("🧹 Iniciando la transformación de clientes...")

    # 1. Verificamos que exista el archivo crudo
    if not os.path.exists(archivo_raw):
        print(f"❌ Error: No se encontró el archivo {archivo_raw}. Ejecutá primero la extracción de clientes.")
        return

    # 2. Leemos el archivo JSON crudo
    with open(archivo_raw, "r", encoding="utf-8") as f:
        datos_json = json.load(f)

    lista_usuarios = datos_json.get('users', [])
    print(f"📊 Total de clientes leídos desde el JSON crudo: {len(lista_usuarios)}")

    # 3. Recorremos y extraemos los datos clave para el negocio
    datos_clientes_limpios = []
    
    for user in lista_usuarios:
        # Algunos datos de dirección vienen anidados, los manejamos con seguridad
        direccion = user.get('address', {})
        
        datos_clientes_limpios.append({
            'id_usuario': user.get('id'),
            'nombre': user.get('firstName'),
            'apellido': user.get('lastName'),
            'email': user.get('email'),
            'genero': user.get('gender'),
            'edad': user.get('age'),
            'ciudad': direccion.get('city'),
            'estado': direccion.get('state'),
            'pais': direccion.get('country')
        })

    # 4. Convertimos la lista limpia en un DataFrame de Pandas
    df_clientes = pd.DataFrame(datos_clientes_limpios)

    # 5. Limpieza básica de calidad de datos
    df_clientes['edad'] = pd.to_numeric(df_clientes['edad'], errors='coerce')
    df_clientes['email'] = df_clientes['email'].fillna('sin_correo@dummy.com')
    df_clientes['ciudad'] = df_clientes['ciudad'].fillna('Desconocida')

    # 6. Guardamos el resultado en la carpeta procesada (`data/processed`)
    os.makedirs("data/processed", exist_ok=True)
    archivo_procesado = "data/processed/clientes_limpios.csv"
    
    df_clientes.to_csv(archivo_procesado, index=False)
    
    print(f"💾 ¡Clientes transformados y guardados con éxito en: {archivo_procesado}!")
    print("\n🔍 Vista previa de cómo quedó la tabla limpia de clientes:")
    print(df_clientes.head(3))

if __name__ == "__main__":
    transformar_clientes()