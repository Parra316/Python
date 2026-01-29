"""
================================================================================
PANDAS: ANÁLISIS Y MANIPULACIÓN DE DATOS
================================================================================

¿QUÉ ES PANDAS?
---------------
Pandas es la librería principal para análisis de datos en Python.
Proporciona estructuras de datos flexibles y herramientas para:

1. Cargar datos de archivos (CSV, Excel, SQL, JSON, etc.)
2. Limpiar y transformar datos
3. Analizar y agregar datos
4. Visualización básica

ESTRUCTURAS PRINCIPALES:
- Series: Array 1D con índice (como columna de Excel)
- DataFrame: Tabla 2D con índices (como hoja de Excel)

INSTALACIÓN:
    pip install pandas

================================================================================
"""

import pandas as pd
import numpy as np

# ==============================================================================
# SERIES: Arrays 1D con índice
# ==============================================================================

print("=" * 60)
print("SERIES: Array 1D con índice")
print("=" * 60)

# Crear Series desde lista
temperaturas = pd.Series([22, 25, 19, 28, 24])
print(f"Serie básica:\n{temperaturas}\n")

# Serie con índice personalizado
temperaturas = pd.Series(
    [22, 25, 19, 28, 24],
    index=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    name='Temperatura'
)
print(f"Serie con índice:\n{temperaturas}\n")

# Acceso por índice
print(f"Temperatura del Martes: {temperaturas['Martes']}")
print(f"Temperaturas > 23:\n{temperaturas[temperaturas > 23]}\n")

# Operaciones
print(f"Media: {temperaturas.mean():.1f}")
print(f"Máximo: {temperaturas.max()}")
print(f"Índice del máximo: {temperaturas.idxmax()}")


# ==============================================================================
# DATAFRAME: Tabla 2D
# ==============================================================================

print("\n" + "=" * 60)
print("DATAFRAME: Tabla 2D")
print("=" * 60)

# Crear desde diccionario
datos = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena'],
    'edad': [28, 34, 29, 42, 31],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla', 'Barcelona'],
    'salario': [35000, 42000, 38000, 55000, 41000]
}
df = pd.DataFrame(datos)
print(f"DataFrame:\n{df}\n")

# Información básica
print(f"Shape (filas, columnas): {df.shape}")
print(f"Columnas: {list(df.columns)}")
print(f"Tipos de datos:\n{df.dtypes}\n")

# Primeras y últimas filas
print(f"Primeras 2 filas:\n{df.head(2)}\n")
print(f"Últimas 2 filas:\n{df.tail(2)}\n")

# Descripción estadística
print(f"Estadísticas:\n{df.describe()}\n")


# ==============================================================================
# SELECCIÓN DE DATOS
# ==============================================================================

print("=" * 60)
print("SELECCIÓN DE DATOS")
print("=" * 60)

# Seleccionar columna
print(f"Columna 'nombre':\n{df['nombre']}\n")

# Múltiples columnas
print(f"Columnas nombre y edad:\n{df[['nombre', 'edad']]}\n")

# Seleccionar filas por índice (iloc = integer location)
print(f"Primera fila (iloc[0]):\n{df.iloc[0]}\n")
print(f"Filas 1-3 (iloc[1:4]):\n{df.iloc[1:4]}\n")

# Seleccionar por etiqueta (loc)
df_indexado = df.set_index('nombre')
print(f"DataFrame con índice 'nombre':\n{df_indexado}\n")
print(f"Datos de María:\n{df_indexado.loc['María']}\n")

# Selección condicional
print(f"Personas mayores de 30:\n{df[df['edad'] > 30]}\n")
print(f"Personas de Madrid:\n{df[df['ciudad'] == 'Madrid']}\n")

# Múltiples condiciones
print(f"Edad > 30 Y salario > 40000:")
print(df[(df['edad'] > 30) & (df['salario'] > 40000)])


# ==============================================================================
# MANIPULACIÓN DE DATOS
# ==============================================================================

print("\n" + "=" * 60)
print("MANIPULACIÓN DE DATOS")
print("=" * 60)

# Copia del DataFrame para no modificar el original
df_trabajo = df.copy()

# Añadir columna
df_trabajo['bonus'] = df_trabajo['salario'] * 0.1
print(f"Con columna bonus:\n{df_trabajo}\n")

# Modificar valores
df_trabajo.loc[df_trabajo['nombre'] == 'Ana', 'salario'] = 37000
print(f"Salario de Ana actualizado:\n{df_trabajo[df_trabajo['nombre'] == 'Ana']}\n")

# Eliminar columna
df_sin_bonus = df_trabajo.drop('bonus', axis=1)
print(f"Sin columna bonus:\n{df_sin_bonus.head(2)}\n")

# Renombrar columnas
df_renombrado = df.rename(columns={'nombre': 'empleado', 'salario': 'sueldo'})
print(f"Columnas renombradas:\n{df_renombrado.head(2)}\n")

# Ordenar
print(f"Ordenado por salario (descendente):\n{df.sort_values('salario', ascending=False)}\n")

# Aplicar función a columna
df_trabajo['edad_grupo'] = df_trabajo['edad'].apply(
    lambda x: 'Joven' if x < 30 else 'Adulto' if x < 40 else 'Senior'
)
print(f"Con categoría de edad:\n{df_trabajo[['nombre', 'edad', 'edad_grupo']]}\n")


# ==============================================================================
# DATOS FALTANTES
# ==============================================================================

print("=" * 60)
print("MANEJO DE DATOS FALTANTES")
print("=" * 60)

# Crear DataFrame con valores faltantes
datos_faltantes = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}
df_na = pd.DataFrame(datos_faltantes)
print(f"DataFrame con NaN:\n{df_na}\n")

# Detectar valores faltantes
print(f"¿Es NaN?:\n{df_na.isna()}\n")
print(f"Cuenta de NaN por columna:\n{df_na.isna().sum()}\n")

# Eliminar filas con NaN
print(f"Sin filas con NaN:\n{df_na.dropna()}\n")

# Rellenar NaN
print(f"NaN reemplazado por 0:\n{df_na.fillna(0)}\n")
print(f"NaN reemplazado por media de columna:\n{df_na.fillna(df_na.mean())}\n")


# ==============================================================================
# AGRUPACIÓN Y AGREGACIÓN
# ==============================================================================

print("=" * 60)
print("AGRUPACIÓN Y AGREGACIÓN (groupby)")
print("=" * 60)

# Agrupar por ciudad
print(f"Datos originales:\n{df}\n")
print(f"Salario medio por ciudad:\n{df.groupby('ciudad')['salario'].mean()}\n")

# Múltiples agregaciones
agregaciones = df.groupby('ciudad').agg({
    'salario': ['mean', 'min', 'max'],
    'edad': 'mean'
})
print(f"Múltiples agregaciones por ciudad:\n{agregaciones}\n")

# Contar valores
print(f"Personas por ciudad:\n{df['ciudad'].value_counts()}\n")


# ==============================================================================
# LECTURA Y ESCRITURA DE ARCHIVOS
# ==============================================================================

print("=" * 60)
print("LECTURA Y ESCRITURA DE ARCHIVOS")
print("=" * 60)

print("""
FORMATOS SOPORTADOS:

CSV:
    df = pd.read_csv('archivo.csv')
    df.to_csv('salida.csv', index=False)

Excel:
    df = pd.read_excel('archivo.xlsx', sheet_name='Hoja1')
    df.to_excel('salida.xlsx', index=False)

JSON:
    df = pd.read_json('archivo.json')
    df.to_json('salida.json')

SQL:
    import sqlite3
    conn = sqlite3.connect('base_datos.db')
    df = pd.read_sql('SELECT * FROM tabla', conn)
    df.to_sql('tabla', conn, if_exists='replace')

Parquet (eficiente para big data):
    df = pd.read_parquet('archivo.parquet')
    df.to_parquet('salida.parquet')
""")

# Ejemplo: guardar y cargar CSV (en memoria)
import io
csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)
csv_buffer.seek(0)
df_leido = pd.read_csv(csv_buffer)
print(f"DataFrame leído de CSV:\n{df_leido.head(2)}\n")


# ==============================================================================
# EJEMPLO PRÁCTICO: ANÁLISIS DE VENTAS
# ==============================================================================

print("=" * 60)
print("EJEMPLO PRÁCTICO: Análisis de Ventas")
print("=" * 60)

# Crear datos de ejemplo
np.random.seed(42)
fechas = pd.date_range('2024-01-01', periods=100, freq='D')
ventas = pd.DataFrame({
    'fecha': fechas,
    'producto': np.random.choice(['A', 'B', 'C'], 100),
    'region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 100),
    'unidades': np.random.randint(10, 100, 100),
    'precio_unitario': np.random.uniform(10, 50, 100).round(2)
})
ventas['total'] = ventas['unidades'] * ventas['precio_unitario']
ventas['mes'] = ventas['fecha'].dt.month

print(f"Primeras filas de ventas:\n{ventas.head()}\n")

# Análisis
print(f"Total de ventas: ${ventas['total'].sum():,.2f}")
print(f"Venta promedio: ${ventas['total'].mean():,.2f}")
print(f"\nVentas por producto:\n{ventas.groupby('producto')['total'].sum().round(2)}\n")
print(f"Ventas por región:\n{ventas.groupby('region')['total'].sum().round(2)}\n")

# Tabla cruzada
tabla_cruzada = pd.pivot_table(
    ventas,
    values='total',
    index='region',
    columns='producto',
    aggfunc='sum'
)
print(f"Tabla cruzada (región x producto):\n{tabla_cruzada.round(2)}\n")

print("=" * 60)
print("PRÓXIMO: 03_visualizacion_matplotlib.py")
print("=" * 60)
