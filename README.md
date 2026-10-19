🛒 Pipeline ETL de E-commerce & Business Intelligence Ejecutivo

Proyecto integral de ingeniería de datos y análisis (ETL - Extract, Transform, Load) desarrollado en Python. Este sistema automatiza la extracción de datos de comercio electrónico desde APIs públicas, los limpia y normaliza mediante modelado relacional utilizando Pandas, los almacena en un Data Warehouse local con SQLite y genera un reporte ejecutivo multipestaña en Excel listo para su visualización interactiva en Looker Studio.

🏗️ Arquitectura y Flujo del Pipeline

El proyecto implementa una arquitectura modular de software, garantizando una separación clara de responsabilidades entre las capas de extracción, transformación, almacenamiento y generación de reportes.

[ API DummyJSON ] 
       │
       ▼ (Extracción)
[ data/raw/ (*.json) ]
       │
       ▼ (Transformación con Pandas)
[ data/processed/ (*.csv) ]
       │
       ▼ (Carga / Load)
[ Data Warehouse SQLite (ecommerce.db) ]
       │
       ▼ (Consultas SQL Analíticas y Exportación Multipestaña)
[ Reporte Ejecutivo (reporte_ejecutivo_ecommerce.xlsx) ]
       │
       ▼
[ Dashboard Interactivo en Looker Studio ]


📂 Estructura del Proyecto

analisis-datos-etl/
│
├── data/
│   ├── raw/                  # Datos crudos extraídos de la API en formato JSON (excluidos en Git)
│   ├── processed/            # Tablas limpias y normalizadas en formato CSV (excluidas en Git)
│   └── reports/              # Reporte ejecutivo en Excel multipestaña para consumo de BI
│
├── .gitignore                # Excluye bases de datos locales, cachés y binarios
├── ecommerce.db              # Base de datos relacional SQLite local (excluida en Git)
├── extraer_api.py            # Módulo de extracción para productos
├── extraer_carritos.py       # Módulo de extracción para carritos y transacciones
├── extraer_datos_clientes.py # Módulo de extracción para usuarios y clientes
├── transformar_productos.py  # Pipeline de limpieza y normalización de productos
├── transformar_clientes.py   # Pipeline de limpieza y normalización geográfica de clientes
├── transformar_carritos.py   # Procesamiento y aplanamiento de transacciones anidadas
├── cargar_a_sqlite.py        # Script de carga que mapea CSVs a tablas SQL relacionales
├── consultar_datos.py        # Motor de consultas SQL analíticas y exportación a Excel
├── main.py                   # Script orquestador central que ejecuta todo el flujo ETL
└── README.md                 # Documentación técnica del proyecto


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
