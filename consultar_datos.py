import os
import sqlite3
import pandas as pd

def generar_reporte_multitaba():
    print("🔍 Conectando a la base de datos para generar el reporte ejecutivo multipestaña...")

    db_path = "ecommerce.db"
    if not os.path.exists(db_path):
        print(f"❌ Error: No se encontró la base de datos {db_path}. Ejecutá primero el script de carga.")
        return

    conexion = sqlite3.connect(db_path)
    os.makedirs("data/reports", exist_ok=True)
    
    # Ruta del archivo Excel final multipestaña
    excel_path = "data/reports/reporte_ejecutivo_ecommerce.xlsx"

    # Diccionario con las consultas de negocio clave
    consultas = {
        "Top Productos": """
            SELECT p.titulo, p.categoria, SUM(dc.cantidad) as total_unidades_vendidas, SUM(dc.precio_total) as ingresos_totales
            FROM detalle_carritos dc
            JOIN productos p ON dc.id_producto = p.id_producto
            GROUP BY p.id_producto, p.titulo, p.categoria
            ORDER BY ingresos_totales DESC
            LIMIT 5;
        """,
        "Ventas por Estado": """
            SELECT c.estado, COUNT(car.id_carrito) as total_compras, SUM(car.total) as facturacion_total
            FROM carritos car
            JOIN clientes c ON car.id_usuario = c.id_usuario
            GROUP BY c.estado
            ORDER BY facturacion_total DESC;
        """,
        "Top Clientes": """
            SELECT c.nombre || ' ' || c.apellido as cliente, c.email, c.estado, COUNT(car.id_carrito) as cantidad_pedidos, SUM(car.total) as gasto_total
            FROM carritos car
            JOIN clientes c ON car.id_usuario = c.id_usuario
            GROUP BY c.id_usuario, c.nombre, c.apellido, c.email, c.estado
            ORDER BY gasto_total DESC
            LIMIT 5;
        """,
        "Ventas por Categoria": """
            SELECT p.categoria, COUNT(dc.id_producto) as total_unidades_vendidas, SUM(dc.precio_total) as facturacion_total
            FROM detalle_carritos dc
            JOIN productos p ON dc.id_producto = p.id_producto
            GROUP BY p.categoria
            ORDER BY facturacion_total DESC;
        """,
        "Impacto Descuentos": """
            SELECT p.categoria, AVG(dc.porcentaje_descuento) as promedio_descuento_porcentual, SUM(dc.precio_total) as ingresos_sin_descuento, SUM(dc.precio_con_descuento) as ingresos_con_descuento_aplicado
            FROM detalle_carritos dc
            JOIN productos p ON dc.id_producto = p.id_producto
            GROUP BY p.categoria
            ORDER BY promedio_descuento_porcentual DESC;
        """,
        "Demografia": """
            SELECT c.genero, c.edad, COUNT(car.id_carrito) as cantidad_compras, SUM(car.total) as gasto_total
            FROM carritos car
            JOIN clientes c ON car.id_usuario = c.id_usuario
            GROUP BY c.genero, c.edad
            ORDER BY gasto_total DESC;
        """
    }

    # Usamos Pandas ExcelWriter para escribir cada DataFrame en una solapa distinta del mismo archivo
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for nombre_pestana, query in consultas.items():
            df = pd.read_sql_query(query, conexion)
            # Guardamos cada tabla en su solapa correspondiente
            df.to_excel(writer, sheet_name=nombre_pestana, index=False)
            print(f"📑 Pestaña '{nombre_pestana}' agregada al reporte.")

    conexion.close()
    print(f"\n🎉 ¡Reporte ejecutivo multipestaña generado con éxito en: {excel_path}!")

if __name__ == "__main__":
    generar_reporte_multitaba()