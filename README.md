🛒 Pipeline ETL de E-commerce & Business Intelligence Ejecutivo

Proyecto integral de ingeniería de datos y análisis (ETL - Extract, Transform, Load) desarrollado en Python. Este sistema automatiza la extracción de datos de comercio electrónico desde APIs públicas, los limpia y normaliza mediante modelado relacional utilizando Pandas, los almacena en un Data Warehouse local con SQLite y genera un reporte ejecutivo multipestaña en Excel listo para su visualización interactiva en Looker Studio.

🏗️ Arquitectura del Pipeline ETL
El proyecto cuenta con un script orquestador (main.py) que automatiza la ejecución de todo el flujo de punta a punta:

Extraction (Extracción): Conexión a endpoints externos para consumir datos crudos (raw) de productos, usuarios y carritos/transacciones, guardándolos en formato JSON.

Transformation (Transformación): Limpieza de nulos, estandarización de tipos de datos, creación de campos calculados (como el precio con descuento) y estructuración de tablas relacionales.

Load (Carga): Creación e inserción de los datos limpios en una base de datos relacional local (ecommerce.db).

Reporting (Generación de Reportes): Ejecución de consultas analíticas SQL avanzadas para exportar un libro de Excel corporativo multipestaña (.xlsx).



📊 Insights Clave de Negocio y Consultas SQL

El motor de reportes ejecuta operaciones avanzadas de SQL (JOIN, GROUP BY, agregaciones) para responder preguntas críticas de negocio:

Top Productos Generadores de Ingresos: Identifica los artículos con mayor facturación y volumen de unidades vendidas.

Distribución Geográfica de Ventas: Rastrea el volumen total de pedidos y facturación desglosado por estado de EE. UU.

Valor del Cliente (Lifetime Value / LTV): Clasifica a los mejores compradores para respaldar estrategias de retención.

Rendimiento por Categoría: Evalúa la participación de mercado y la contribución financiera de cada categoría de productos.

Efectividad de Descuentos: Analiza las tasas de descuento promedio frente a los márgenes de ingresos reales por categoría.




📈 Dashboard Ejecutivo en Looker Studio
<img width="1920" height="2420" alt="screencapture-datastudio-google-u-0-reporting-e9a61b94-c2bf-4097-aaaf-13766a422fec-page-aDZBG-2026-10-18-21_30_07" src="https://github.com/user-attachments/assets/65af2a68-9c07-40c4-817e-a9376e7aac75" />


El reporte ejecutivo multipestaña generado (data/reports/reporte_ejecutivo_ecommerce.xlsx) alimenta de forma directa el Dashboard Interactivo en Looker Studio, el cual incluye:

KPIs de Alto Nivel: Ingresos Totales, Unidades Vendidas y Ticket Promedio (AOV).

Desglose por Categoría: Gráficos circulares interactivos que muestran la participación de mercado.

Análisis Geográfico: Gráficos de barras que destacan los estados con mayor volumen de ventas.

Tabla de Mejores Clientes: Seguimiento detallado de cuentas de alto valor.


🛠️ Stack Tecnológico

Lenguaje: Python

Manipulación de Datos: Pandas, NumPy

Base de Datos y SQL: SQLite

Automatización de Archivos: OpenPyXL (generación de Excel multipestaña)

Visualización: Looker Studio

Control de Versiones: Git & GitHub
