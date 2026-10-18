import os
import pandas as pd
import sqlite3

def cargar_datos_a_sqlite():
    print("🚀 Iniciando la carga de datos hacia SQLite...")

    # 1. Definimos la ruta de nuestra base de datos SQLite
    # Se creará un archivo llamado 'ecommerce.db' en la raíz de tu proyecto
    db_path = "ecommerce.db"
    
    # Nos conectamos a la base de datos (si no existe, SQLite la crea sola)
    conexion = sqlite3.connect(db_path)
    print(f"📦 Base de datos conectada/creada en: {db_path}")

    # 2. Definimos los archivos CSV procesados que queremos cargar
    archivos_a_cargar = {
        "productos": "data/processed/productos_limpios.csv",
        "clientes": "data/processed/clientes_limpios.csv",
        "carritos": "data/processed/carritos_limpios.csv",
        "detalle_carritos": "data/processed/detalle_carritos_limpios.csv"
    }

    # 3. Recorremos cada diccionario, leemos el CSV y lo cargamos a la tabla correspondiente
    for nombre_tabla, ruta_csv in archivos_a_cargar.items():
        if os.path.exists(ruta_csv):
            # Leemos el CSV con Pandas
            df = pd.read_csv(ruta_csv)
            
            # Cargamos el DataFrame a la tabla SQLite
            # if_exists='replace' significa que si ya existe la tabla, la sobrescribe limpia (ideal para pruebas y pipelines repetibles)
            # index=False evita que Pandas guarde el índice numérico como una columna extra
            df.to_sql(nombre_tabla, conexion, if_exists='replace', index=False)
            
            print(f"✅ Tabla '{nombre_tabla}' cargada con éxito ({len(df)} filas insertadas).")
        else:
            print(f"❌ Advertencia: No se encontró el archivo {ruta_csv}. Saltando esta tabla.")

    # 4. Cerramos la conexión a la base de datos de manera prolija
    conexion.close()
    print("\n🎉 ¡Proceso de Carga (Load) finalizado con éxito! La base de datos 'ecommerce.db' está lista.")

if __name__ == "__main__":
    cargar_datos_a_sqlite()