import time

# Importamos las funciones principales de tus módulos
from extraer_api import extraer_y_guardar_productos
from extraer_carritos import extraer_y_guardar_carrito
from extraer_datos_clientes import extraer_y_guardar_clientes

from transformar_productos import transformar_productos
from transformar_clientes import transformar_clientes
from transformar_carritos import transformar_carritos

from cargar_a_sqlite import cargar_datos_a_sqlite
from consultar_datos import generar_reporte_multitaba

def ejecutar_pipeline_completo():
    inicio_total = time.time()
    print(" ==================================================")
    print(" INICIANDO PIPELINE ETL COMPLETO DE E-COMMERCE")
    print(" ==================================================\n")

    try:
        # FASE 1: EXTRACCIÓN
        print("📥 [FASE 1/4] Extrayendo datos desde las APIs...")
        extraer_y_guardar_productos()
        extraer_y_guardar_clientes()
        extraer_y_guardar_carrito()
        print("✅ Extracción finalizada con éxito.\n")

        # FASE 2: TRANSFORMACIÓN
        print("🧹 [FASE 2/4] Transformando y limpiando datos con Pandas...")
        transformar_productos()
        transformar_clientes()
        transformar_carritos()
        print("✅ Transformación finalizada con éxito.\n")

        # FASE 3: CARGA
        print("💾 [FASE 3/4] Cargando datos limpios a SQLite...")
        cargar_datos_a_sqlite()
        print("✅ Carga a base de datos finalizada con éxito.\n")

        # FASE 4: REPORTES Y CONSULTAS ANALÍTICAS
        print("📊 [FASE 4/4] Generando reportes de negocio y consultas SQL...")
        generar_reporte_multitaba()
        print("✅ Reportes generados con éxito.\n")

        tiempo_total = time.time() - inicio_total
        print("🎉 ==================================================")
        print(f"🎉 ¡PIPELINE EJECUTADO DE PUNTA A PUNTA CON ÉXITO!")
        print(f"⏱️  Tiempo total de ejecución: {tiempo_total:.2f} segundos.")
        print("🎉 ==================================================")

    except Exception as e:
        print(f"\n❌ Ocurrió un error crítico durante la ejecución del pipeline: {e}")

if __name__ == "__main__":
    ejecutar_pipeline_completo()