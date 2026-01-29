"""
================================================================================
VISUALIZACIÓN DE DATOS: MATPLOTLIB Y SEABORN
================================================================================

¿POR QUÉ VISUALIZAR DATOS?
--------------------------
- "Una imagen vale más que mil palabras"
- Identificar patrones, tendencias y anomalías
- Comunicar resultados de forma efectiva
- Explorar datos antes de modelar

LIBRERÍAS:
- Matplotlib: Base de visualización en Python
- Seaborn: Visualizaciones estadísticas atractivas (basado en Matplotlib)

INSTALACIÓN:
    pip install matplotlib seaborn

================================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# Intentar importar seaborn
try:
    import seaborn as sns
    SEABORN_DISPONIBLE = True
except ImportError:
    print("Seaborn no instalado. Instálalo con: pip install seaborn")
    SEABORN_DISPONIBLE = False


# ==============================================================================
# CONFIGURACIÓN BÁSICA
# ==============================================================================

print("=" * 60)
print("MATPLOTLIB: Configuración y gráficos básicos")
print("=" * 60)

# Estilo (opcional, hace los gráficos más bonitos)
plt.style.use('seaborn-v0_8-whitegrid')


# ==============================================================================
# GRÁFICO DE LÍNEAS
# ==============================================================================

print("""
1. GRÁFICO DE LÍNEAS
   - Ideal para: Series temporales, tendencias
   - Función: plt.plot()
""")

# Datos de ejemplo: temperatura durante el día
horas = np.arange(0, 24)
temperatura = 15 + 10 * np.sin((horas - 6) * np.pi / 12) + np.random.randn(24)

plt.figure(figsize=(10, 5))
plt.plot(horas, temperatura, 'b-', linewidth=2, label='Temperatura')
plt.xlabel('Hora del día')
plt.ylabel('Temperatura (°C)')
plt.title('Variación de Temperatura Durante el Día')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(range(0, 25, 3))
plt.tight_layout()
plt.savefig('/tmp/01_lineas.png', dpi=100)
plt.close()
print("Gráfico guardado en /tmp/01_lineas.png")


# ==============================================================================
# GRÁFICO DE DISPERSIÓN (SCATTER)
# ==============================================================================

print("""
2. GRÁFICO DE DISPERSIÓN (SCATTER)
   - Ideal para: Relación entre dos variables
   - Función: plt.scatter()
""")

# Datos de ejemplo: relación altura-peso
np.random.seed(42)
alturas = np.random.normal(170, 10, 100)
pesos = alturas * 0.5 + np.random.normal(0, 5, 100)
genero = np.random.choice(['M', 'F'], 100)

plt.figure(figsize=(10, 6))
colores = ['blue' if g == 'M' else 'red' for g in genero]
plt.scatter(alturas, pesos, c=colores, alpha=0.6, s=50)
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relación Altura-Peso')

# Leyenda manual
from matplotlib.patches import Patch
leyenda = [Patch(color='blue', label='Masculino'),
           Patch(color='red', label='Femenino')]
plt.legend(handles=leyenda)
plt.tight_layout()
plt.savefig('/tmp/02_scatter.png', dpi=100)
plt.close()
print("Gráfico guardado en /tmp/02_scatter.png")


# ==============================================================================
# GRÁFICO DE BARRAS
# ==============================================================================

print("""
3. GRÁFICO DE BARRAS
   - Ideal para: Comparar categorías
   - Función: plt.bar() / plt.barh()
""")

# Datos de ejemplo: ventas por producto
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
ventas_q1 = [120, 90, 150, 80, 110]
ventas_q2 = [130, 100, 140, 95, 125]

x = np.arange(len(productos))
ancho = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
barras1 = ax.bar(x - ancho/2, ventas_q1, ancho, label='Q1', color='steelblue')
barras2 = ax.bar(x + ancho/2, ventas_q2, ancho, label='Q2', color='coral')

ax.set_xlabel('Productos')
ax.set_ylabel('Ventas (miles)')
ax.set_title('Ventas por Producto: Q1 vs Q2')
ax.set_xticks(x)
ax.set_xticklabels(productos)
ax.legend()

# Añadir valores sobre las barras
for barra in barras1:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('/tmp/03_barras.png', dpi=100)
plt.close()
print("Gráfico guardado en /tmp/03_barras.png")


# ==============================================================================
# HISTOGRAMA
# ==============================================================================

print("""
4. HISTOGRAMA
   - Ideal para: Distribución de una variable
   - Función: plt.hist()
""")

# Datos de ejemplo: notas de estudiantes
np.random.seed(42)
notas = np.concatenate([
    np.random.normal(6, 1.5, 150),   # Grupo principal
    np.random.normal(9, 0.5, 50)     # Estudiantes destacados
])
notas = np.clip(notas, 0, 10)  # Limitar entre 0 y 10

plt.figure(figsize=(10, 6))
plt.hist(notas, bins=20, edgecolor='black', alpha=0.7, color='steelblue')
plt.axvline(notas.mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {notas.mean():.1f}')
plt.axvline(np.median(notas), color='green', linestyle='--', linewidth=2, label=f'Mediana: {np.median(notas):.1f}')
plt.xlabel('Nota')
plt.ylabel('Frecuencia')
plt.title('Distribución de Notas')
plt.legend()
plt.tight_layout()
plt.savefig('/tmp/04_histograma.png', dpi=100)
plt.close()
print("Gráfico guardado en /tmp/04_histograma.png")


# ==============================================================================
# GRÁFICO CIRCULAR (PIE)
# ==============================================================================

print("""
5. GRÁFICO CIRCULAR (PIE)
   - Ideal para: Proporciones de un total
   - Función: plt.pie()
   - Nota: Usar con moderación (barras suelen ser mejores)
""")

# Datos de ejemplo: cuota de mercado
empresas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D', 'Otros']
cuotas = [35, 25, 20, 12, 8]
colores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.05, 0, 0, 0, 0)  # Destacar el primero

plt.figure(figsize=(8, 8))
plt.pie(cuotas, explode=explode, labels=empresas, colors=colores,
        autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Cuota de Mercado')
plt.axis('equal')
plt.tight_layout()
plt.savefig('/tmp/05_pie.png', dpi=100)
plt.close()
print("Gráfico guardado en /tmp/05_pie.png")


# ==============================================================================
# BOXPLOT (DIAGRAMA DE CAJA)
# ==============================================================================

print("""
6. BOXPLOT (Diagrama de Caja)
   - Ideal para: Ver distribución y outliers
   - Muestra: mediana, cuartiles, valores atípicos
   - Función: plt.boxplot()
""")

# Datos de ejemplo: salarios por departamento
np.random.seed(42)
ventas = np.random.normal(45000, 10000, 50)
marketing = np.random.normal(42000, 8000, 40)
tech = np.random.normal(60000, 15000, 45)
rrhh = np.random.normal(38000, 5000, 35)

datos_salarios = [ventas, marketing, tech, rrhh]
etiquetas = ['Ventas', 'Marketing', 'Tecnología', 'RRHH']

plt.figure(figsize=(10, 6))
bp = plt.boxplot(datos_salarios, labels=etiquetas, patch_artist=True)

colores_box = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink']
for patch, color in zip(bp['boxes'], colores_box):
    patch.set_facecolor(color)

plt.ylabel('Salario ($)')
plt.title('Distribución de Salarios por Departamento')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/tmp/06_boxplot.png', dpi=100)
plt.close()
print("Gráfico guardado en /tmp/06_boxplot.png")


# ==============================================================================
# SUBPLOTS: MÚLTIPLES GRÁFICOS
# ==============================================================================

print("""
7. SUBPLOTS: Múltiples gráficos en una figura
   - Función: plt.subplots(filas, columnas)
""")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico 1: Líneas
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), label='sin(x)')
axes[0, 0].plot(x, np.cos(x), label='cos(x)')
axes[0, 0].set_title('Funciones Trigonométricas')
axes[0, 0].legend()

# Gráfico 2: Scatter
axes[0, 1].scatter(np.random.randn(50), np.random.randn(50), alpha=0.6)
axes[0, 1].set_title('Scatter Aleatorio')

# Gráfico 3: Barras
categorias = ['A', 'B', 'C', 'D']
valores = [23, 45, 56, 78]
axes[1, 0].bar(categorias, valores, color='teal')
axes[1, 0].set_title('Gráfico de Barras')

# Gráfico 4: Histograma
datos = np.random.normal(0, 1, 1000)
axes[1, 1].hist(datos, bins=30, edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Distribución Normal')

plt.tight_layout()
plt.savefig('/tmp/07_subplots.png', dpi=100)
plt.close()
print("Gráfico guardado en /tmp/07_subplots.png")


# ==============================================================================
# SEABORN: VISUALIZACIÓN ESTADÍSTICA
# ==============================================================================

if SEABORN_DISPONIBLE:
    print("""
8. SEABORN: Visualización estadística elegante
   - Basado en Matplotlib pero con API más simple
   - Diseñado para DataFrames de Pandas
   - Gráficos estadísticos integrados
""")

    import pandas as pd

    # Crear DataFrame de ejemplo
    np.random.seed(42)
    n = 200
    df = pd.DataFrame({
        'x': np.random.randn(n),
        'y': np.random.randn(n) + np.random.randn(n) * 0.5,
        'categoria': np.random.choice(['A', 'B', 'C'], n),
        'valor': np.random.exponential(10, n)
    })

    # Configurar estilo seaborn
    sns.set_theme(style="whitegrid")

    # Pairplot: matriz de scatter plots
    fig = plt.figure(figsize=(10, 8))

    # Heatmap de correlación
    plt.figure(figsize=(8, 6))
    corr_matrix = df[['x', 'y', 'valor']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    plt.savefig('/tmp/08_heatmap.png', dpi=100)
    plt.close()
    print("Gráfico guardado en /tmp/08_heatmap.png")

    # Violin plot
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x='categoria', y='valor', palette='muted')
    plt.title('Violin Plot por Categoría')
    plt.tight_layout()
    plt.savefig('/tmp/09_violin.png', dpi=100)
    plt.close()
    print("Gráfico guardado en /tmp/09_violin.png")

    # Jointplot
    g = sns.jointplot(data=df, x='x', y='y', kind='hex', color='steelblue')
    g.fig.suptitle('Joint Plot', y=1.02)
    g.savefig('/tmp/10_jointplot.png', dpi=100)
    plt.close()
    print("Gráfico guardado en /tmp/10_jointplot.png")


# ==============================================================================
# RESUMEN DE FUNCIONES
# ==============================================================================

print("\n" + "=" * 60)
print("RESUMEN DE FUNCIONES DE VISUALIZACIÓN")
print("=" * 60)

print("""
MATPLOTLIB:
-----------
plt.plot()      - Gráfico de líneas
plt.scatter()   - Gráfico de dispersión
plt.bar()       - Gráfico de barras vertical
plt.barh()      - Gráfico de barras horizontal
plt.hist()      - Histograma
plt.pie()       - Gráfico circular
plt.boxplot()   - Diagrama de caja
plt.subplots()  - Múltiples gráficos

CONFIGURACIÓN:
plt.figure(figsize=(ancho, alto))
plt.xlabel(), plt.ylabel()
plt.title()
plt.legend()
plt.grid()
plt.savefig()
plt.show()

SEABORN:
--------
sns.scatterplot()  - Scatter con categorías
sns.lineplot()     - Líneas con intervalos de confianza
sns.barplot()      - Barras con error bars
sns.histplot()     - Histograma mejorado
sns.boxplot()      - Boxplot por categoría
sns.violinplot()   - Violin plot
sns.heatmap()      - Mapa de calor
sns.pairplot()     - Matriz de gráficos
sns.jointplot()    - Scatter + distribuciones marginales
""")

print("\n" + "=" * 60)
print("Gráficos guardados en /tmp/")
print("Abre los archivos .png para verlos")
print("=" * 60)
