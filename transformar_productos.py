import os
import json
import pandas as pd

def transformar_productos():
    archivo_raw = "data/raw/productos_raw.json"
    
    print(" Iniciando la transformación de productos...")

    # 1. Verificamos que el archivo crudo exista
    if not os.path.exists(archivo_raw):
        print(f" Error: No se encontró el archivo {archivo_raw}. Ejecutá primero la extracción.")
        return

    # 2. Leemos el archivo JSON crudo que guardamos antes
    with open(archivo_raw, "r", encoding="utf-8") as f:
        datos_json = json.load(f)

    # 3. Extraemos la lista de productos que está dentro de la llave 'products'
    lista_productos = datos_json.get('products', [])
    print(f"📊 Total de registros leídos desde el JSON crudo: {len(lista_productos)}")

    # 4. Convertimos esa lista de diccionarios en un DataFrame de Pandas (una tabla formal)
    df = pd.DataFrame(lista_productos)

    # 5. SELECCIÓN Y LIMPIEZA DE COLUMNAS (Foco de Negocio)
    # Nos quedamos solo con las columnas que nos interesan para el análisis y el reporte
    columnas_utiles = ['id', 'title', 'category', 'price', 'stock', 'rating', 'brand']
    
    # Filtramos el DataFrame para conservar únicamente esas columnas
    df_limpio = df[columnas_utiles].copy()

    # Opcional: Renombramos las columnas al español para que queden impecables en la base de datos y Looker Studio
    df_limpio.columns = ['id_producto', 'titulo', 'categoria', 'precio', 'stock', 'calificacion', 'marca']

    # 6. Limpieza básica de calidad de datos
    # Nos aseguramos de que el precio y el stock no tengan valores nulos o raros
    df_limpio['precio'] = pd.to_numeric(df_limpio['precio'], errors='coerce')
    df_limpio['stock'] = pd.to_numeric(df_limpio['stock'], errors='coerce')
    
    # Rellenamos marcas vacías con 'Desconocida' por si acaso
    df_limpio['marca'] = df_limpio['marca'].fillna('Desconocida')

    # 7. Guardamos el resultado limpio en una nueva carpeta de procesados (`data/processed`)
    os.makedirs("data/processed", exist_ok=True)
    archivo_procesado = "data/processed/productos_limpios.csv"
    
    df_limpio.to_csv(archivo_procesado, index=False)
    
    print(f"¡Datos transformados y guardados con éxito en: {archivo_procesado}!")
    print("\n Vista previa de cómo quedó la tabla limpia:")
    print(df_limpio.head(5))

if __name__ == "__main__":
    transformar_productos()