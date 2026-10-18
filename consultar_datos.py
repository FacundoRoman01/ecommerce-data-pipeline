import os
import sqlite3
import pandas as pd

def generar_consultas_y_reportes():
    print("🔍 Conectando a la base de datos para extraer insights de negocio...")

    # 1. Nos conectamos a nuestra base de datos SQLite que ya creamos antes
    db_path = "ecommerce.db"
    if not os.path.exists(db_path):
        print(f"❌ Error: No se encontró la base de datos {db_path}. Ejecutá primero el script de carga.")
        return

    conexion = sqlite3.connect(db_path)

    # Creamos la carpeta por si queremos exportar los reportes en CSV
    os.makedirs("data/reports", exist_ok=True)

    # ==========================================
    # CONSULTA 1: Top 5 Productos más vendidos por ingresos
    # ==========================================
    # Explicación: Cruzamos la tabla de ítems con la de productos para sumar cuánto dinero nos dejó cada uno.
    query_productos = """
        SELECT 
            p.titulo,
            p.categoria,
            SUM(dc.cantidad) as total_unidades_vendidas,
            SUM(dc.precio_total) as ingresos_totales
        FROM detalle_carritos dc
        JOIN productos p ON dc.id_producto = p.id_producto
        GROUP BY p.id_producto, p.titulo, p.categoria
        ORDER BY ingresos_totales DESC
        LIMIT 5;
    """
    
    df_top_productos = pd.read_sql_query(query_productos, conexion)
    print("\n🏆 --- TOP 5 PRODUCTOS QUE MÁS DINERO GENERAN ---")
    print(df_top_productos)
    df_top_productos.to_csv("data/reports/top_productos.csv", index=False)

    # ==========================================
    # CONSULTA 2: Ventas por Estado (Región)
    # ==========================================
    # Explicación: Cruzamos los carritos (ventas) con los clientes para saber de qué estado de EE.UU. vienen las compras.
    query_estados = """
        SELECT 
            c.estado,
            COUNT(car.id_carrito) as total_compras,
            SUM(car.total) as facturacion_total
        FROM carritos car
        JOIN clientes c ON car.id_usuario = c.id_usuario
        GROUP BY c.estado
        ORDER BY facturacion_total DESC;
    """
    
    df_estados = pd.read_sql_query(query_estados, conexion)
    print("\n📍 --- VENTAS Y FACTURACIÓN POR ESTADO ---")
    print(df_estados.head(5))
    df_estados.to_csv("data/reports/ventas_por_estado.csv", index=False)

    # ==========================================
    # CONSULTA 3: Mejores Clientes (Lifetime Value)
    # ==========================================
    # Explicación: Vemos qué clientes individuales compraron más y cuánto gastaron en total.
    query_clientes = """
        SELECT 
            c.nombre || ' ' || c.apellido as cliente,
            c.email,
            c.estado,
            COUNT(car.id_carrito) as cantidad_pedidos,
            SUM(car.total) as gasto_total
        FROM carritos car
        JOIN clientes c ON car.id_usuario = c.id_usuario
        GROUP BY c.id_usuario, c.nombre, c.apellido, c.email, c.estado
        ORDER BY gasto_total DESC
        LIMIT 5;
    """
    
    df_clientes = pd.read_sql_query(query_clientes, conexion)
    print("\n💎 --- TOP 5 MEJORES CLIENTES ---")
    print(df_clientes)
    df_clientes.to_csv("data/reports/top_clientes.csv", index=False)



    query_categorias = """
        SELECT 
            p.categoria,
            COUNT(dc.id_producto) as total_unidades_vendidas,
            SUM(dc.precio_total) as facturacion_total
        FROM detalle_carritos dc
        JOIN productos p ON dc.id_producto = p.id_producto
        GROUP BY p.categoria
        ORDER BY facturacion_total DESC;
    """
    
    df_categorias = pd.read_sql_query(query_categorias, conexion)
    print("\n🛍️ --- FACTURACIÓN POR CATEGORÍA DE PRODUCTO ---")
    print(df_categorias)
    df_categorias.to_csv("data/reports/ventas_por_categoria.csv", index=False)




    query_descuentos = """
        SELECT 
            p.categoria,
            AVG(dc.porcentaje_descuento) as promedio_descuento_porcentual,
            SUM(dc.precio_total) as ingresos_sin_descuento,
            SUM(dc.precio_con_descuento) as ingresos_con_descuento_aplicado
        FROM detalle_carritos dc
        JOIN productos p ON dc.id_producto = p.id_producto
        GROUP BY p.categoria
        ORDER BY promedio_descuento_porcentual DESC;
    """
    
    df_descuentos = pd.read_sql_query(query_descuentos, conexion)
    print("\n🏷️ --- IMPACTO DE DESCUENTOS POR CATEGORÍA ---")
    print(df_descuentos)
    df_descuentos.to_csv("data/reports/impacto_descuentos.csv", index=False)



    query_demografia = """
        SELECT 
            c.genero,
            c.edad,
            COUNT(car.id_carrito) as cantidad_compras,
            SUM(car.total) as gasto_total
        FROM carritos car
        JOIN clientes c ON car.id_usuario = c.id_usuario
        GROUP BY c.genero, c.edad
        ORDER BY gasto_total DESC;
    """
    
    df_demografia = pd.read_sql_query(query_demografia, conexion)
    print("\n👥 --- COMPORTAMIENTO POR GÉNERO Y EDAD ---")
    print(df_demografia.head(5))
    df_demografia.to_csv("data/reports/comportamiento_demografico.csv", index=False)


    # Cerramos la conexión
    conexion.close()
    print("\n💾 ¡Todos los reportes de negocio fueron generados y guardados en la carpeta 'data/reports/'!")

if __name__ == "__main__":
    generar_consultas_y_reportes()