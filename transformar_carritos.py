import os
import json
import pandas as pd

def transformar_carritos():
    archivo_raw = "data/raw/carrito_raw.json"
    
    print("🧹 Iniciando la transformación de carritos y transacciones...")

    # 1. Verificamos que exista el archivo crudo
    if not os.path.exists(archivo_raw):
        print(f"❌ Error: No se encontró el archivo {archivo_raw}. Ejecutá primero la extracción.")
        return

    # 2. Leemos el archivo JSON crudo
    with open(archivo_raw, "r", encoding="utf-8") as f:
        datos_json = json.load(f)

    lista_carritos = datos_json.get('carts', [])
    print(f"📊 Total de carritos leídos desde el JSON crudo: {len(lista_carritos)}")

    # 3. Listas para almacenar los datos transformados
    datos_transacciones = []
    datos_detalle_items = []

    # 4. Recorremos cada carrito para "aplanar" la estructura anidada
    for carrito in lista_carritos:
        carrito_id = carrito.get('id')
        user_id = carrito.get('userId')
        total = carrito.get('total')
        discounted_total = carrito.get('discountedTotal')
        total_products = carrito.get('totalProducts')
        total_quantity = carrito.get('totalQuantity')

        # Guardamos la info general de la venta (Cabecera del Carrito)
        datos_transacciones.append({
            'id_carrito': carrito_id,
            'id_usuario': user_id,
            'total': total,
            'total_con_descuento': discounted_total,
            'cantidad_tipos_productos': total_products,
            'cantidad_total_unidades': total_quantity
        })

        # Como cada carrito tiene una lista de productos adentro ('products'), la recorremos
        productos_en_carrito = carrito.get('products', [])
        for prod in productos_en_carrito:
            datos_detalle_items.append({
                'id_carrito': carrito_id,
                'id_producto': prod.get('id'),
                'titulo_producto': prod.get('title'),
                'precio_unitario': prod.get('price'),
                'cantidad': prod.get('quantity'),
                'precio_total': prod.get('total'),
                'porcentaje_descuento': prod.get('discountPercentage'),
                'precio_con_descuento': prod.get('discountedTotal')
            })

    # 5. Convertimos nuestras listas en DataFrames de Pandas
    df_carritos = pd.DataFrame(datos_transacciones)
    df_detalles = pd.DataFrame(datos_detalle_items)

    # 6. Guardamos los resultados limpios en la carpeta procesada (`data/processed`)
    os.makedirs("data/processed", exist_ok=True)
    
    archivo_carritos_procesado = "data/processed/carritos_limpios.csv"
    archivo_detalles_procesado = "data/processed/detalle_carritos_limpios.csv"

    df_carritos.to_csv(archivo_carritos_procesado, index=False)
    df_detalles.to_csv(archivo_detalles_procesado, index=False)

    print(f"💾 ¡Cabeceras de carritos guardadas en: {archivo_carritos_procesado}!")
    print(f"💾 ¡Detalle de ítems guardados en: {archivo_detalles_procesado}!")
    
    print("\n🔍 Vista previa de las Transacciones (Carritos):")
    print(df_carritos.head(3))
    
    print("\n🔍 Vista previa del Detalle de Ítems (Productos comprados):")
    print(df_detalles.head(3))

if __name__ == "__main__":
    transformar_carritos()