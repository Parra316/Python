"""
================================================================================
NUMPY: FUNDAMENTOS PARA DATA SCIENCE
================================================================================

¿QUÉ ES NUMPY?
--------------
NumPy (Numerical Python) es la librería fundamental para computación científica
en Python. Proporciona:

1. Arrays multidimensionales eficientes (ndarray)
2. Operaciones matemáticas vectorizadas (sin loops)
3. Funciones de álgebra lineal, estadística, etc.
4. Base para Pandas, Scikit-learn, TensorFlow, PyTorch

INSTALACIÓN:
    pip install numpy

================================================================================
¿POR QUÉ NUMPY Y NO LISTAS DE PYTHON?
================================================================================

Las listas de Python son lentas para cálculos numéricos porque:
- Cada elemento puede ser de diferente tipo
- Los elementos están dispersos en memoria
- Las operaciones requieren loops explícitos

NumPy arrays son rápidos porque:
- Todos los elementos son del mismo tipo
- Datos contiguos en memoria (mejor uso de caché)
- Operaciones implementadas en C/Fortran

================================================================================
"""

import numpy as np
import time

# ==============================================================================
# CREACIÓN DE ARRAYS
# ==============================================================================

print("=" * 60)
print("CREACIÓN DE ARRAYS NUMPY")
print("=" * 60)

# Desde listas de Python
lista = [1, 2, 3, 4, 5]
array_1d = np.array(lista)
print(f"Array 1D: {array_1d}")
print(f"Tipo: {type(array_1d)}")
print(f"Dtype (tipo de datos internos): {array_1d.dtype}")

# Array 2D (matriz)
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\nMatriz 2D:\n{matriz}")
print(f"Forma (shape): {matriz.shape}")  # (filas, columnas)
print(f"Dimensiones: {matriz.ndim}")
print(f"Total elementos: {matriz.size}")

# Arrays especiales
print("\n--- Arrays especiales ---")
print(f"Zeros (3x4):\n{np.zeros((3, 4))}")
print(f"\nOnes (2x3):\n{np.ones((2, 3))}")
print(f"\nIdentidad (3x3):\n{np.eye(3)}")
print(f"\nRango 0-9: {np.arange(10)}")
print(f"Rango con paso: {np.arange(0, 10, 2)}")  # 0, 2, 4, 6, 8
print(f"Linspace (5 valores entre 0 y 1): {np.linspace(0, 1, 5)}")

# Arrays aleatorios
print("\n--- Arrays aleatorios ---")
np.random.seed(42)  # Para reproducibilidad
print(f"Uniforme [0,1): {np.random.random(5)}")
print(f"Enteros [0,10): {np.random.randint(0, 10, 5)}")
print(f"Normal (media=0, std=1): {np.random.randn(5)}")


# ==============================================================================
# INDEXACIÓN Y SLICING
# ==============================================================================

print("\n" + "=" * 60)
print("INDEXACIÓN Y SLICING")
print("=" * 60)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"Array original: {arr}")

# Indexación básica
print(f"\nPrimer elemento (índice 0): {arr[0]}")
print(f"Último elemento (índice -1): {arr[-1]}")
print(f"Elementos 2-5 (índices 2:5): {arr[2:5]}")
print(f"Cada 2 elementos: {arr[::2]}")
print(f"Invertido: {arr[::-1]}")

# Indexación 2D
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\nMatriz:\n{matriz}")
print(f"Elemento [1,2]: {matriz[1, 2]}")  # Fila 1, columna 2 = 6
print(f"Primera fila: {matriz[0]}")
print(f"Primera columna: {matriz[:, 0]}")
print(f"Submatriz 2x2:\n{matriz[:2, :2]}")

# Indexación booleana (muy útil para filtrar datos)
print("\n--- Indexación booleana ---")
datos = np.array([15, 23, 8, 42, 31, 5, 19])
print(f"Datos: {datos}")
print(f"Mayores que 20: {datos[datos > 20]}")
print(f"Pares: {datos[datos % 2 == 0]}")
print(f"Entre 10 y 30: {datos[(datos >= 10) & (datos <= 30)]}")


# ==============================================================================
# OPERACIONES VECTORIZADAS
# ==============================================================================

print("\n" + "=" * 60)
print("OPERACIONES VECTORIZADAS")
print("=" * 60)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a = {a}")
print(f"b = {b}")
print(f"\nSuma: a + b = {a + b}")
print(f"Resta: a - b = {a - b}")
print(f"Multiplicación: a * b = {a * b}")
print(f"División: a / b = {a / b}")
print(f"Potencia: a ** 2 = {a ** 2}")
print(f"Raíz cuadrada: sqrt(a) = {np.sqrt(a)}")

# Comparación de velocidad
print("\n--- Velocidad: NumPy vs Listas ---")
size = 1000000

# Con listas
lista_python = list(range(size))
inicio = time.time()
resultado_lista = [x * 2 for x in lista_python]
tiempo_lista = time.time() - inicio

# Con NumPy
array_numpy = np.arange(size)
inicio = time.time()
resultado_numpy = array_numpy * 2
tiempo_numpy = time.time() - inicio

print(f"Lista Python: {tiempo_lista:.4f} segundos")
print(f"NumPy array:  {tiempo_numpy:.4f} segundos")
print(f"NumPy es {tiempo_lista/tiempo_numpy:.1f}x más rápido")


# ==============================================================================
# FUNCIONES ESTADÍSTICAS
# ==============================================================================

print("\n" + "=" * 60)
print("FUNCIONES ESTADÍSTICAS")
print("=" * 60)

datos = np.array([23, 45, 12, 67, 34, 89, 21, 56, 78, 43])
print(f"Datos: {datos}")
print(f"\nSuma: {np.sum(datos)}")
print(f"Media: {np.mean(datos)}")
print(f"Mediana: {np.median(datos)}")
print(f"Desviación estándar: {np.std(datos):.2f}")
print(f"Varianza: {np.var(datos):.2f}")
print(f"Mínimo: {np.min(datos)}")
print(f"Máximo: {np.max(datos)}")
print(f"Índice del máximo: {np.argmax(datos)}")
print(f"Rango (max - min): {np.ptp(datos)}")

# Operaciones por eje en matrices
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\nMatriz:\n{matriz}")
print(f"Suma total: {np.sum(matriz)}")
print(f"Suma por columnas (axis=0): {np.sum(matriz, axis=0)}")
print(f"Suma por filas (axis=1): {np.sum(matriz, axis=1)}")


# ==============================================================================
# ÁLGEBRA LINEAL
# ==============================================================================

print("\n" + "=" * 60)
print("ÁLGEBRA LINEAL")
print("=" * 60)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"Matriz A:\n{A}")
print(f"Matriz B:\n{B}")

# Producto matricial
print(f"\nProducto matricial A @ B:\n{A @ B}")
print(f"Equivalente: np.dot(A, B):\n{np.dot(A, B)}")

# Transpuesta
print(f"\nTranspuesta de A:\n{A.T}")

# Determinante
print(f"\nDeterminante de A: {np.linalg.det(A):.2f}")

# Inversa
print(f"\nInversa de A:\n{np.linalg.inv(A)}")

# Autovalores y autovectores
autovalores, autovectores = np.linalg.eig(A)
print(f"\nAutovalores de A: {autovalores}")


# ==============================================================================
# RESHAPE Y MANIPULACIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("RESHAPE Y MANIPULACIÓN DE ARRAYS")
print("=" * 60)

arr = np.arange(12)
print(f"Array original: {arr}")
print(f"Shape: {arr.shape}")

# Reshape
print(f"\nReshape a (3, 4):\n{arr.reshape(3, 4)}")
print(f"Reshape a (4, 3):\n{arr.reshape(4, 3)}")
print(f"Reshape a (2, 2, 3):\n{arr.reshape(2, 2, 3)}")

# Flatten y ravel
matriz = arr.reshape(3, 4)
print(f"\nMatriz:\n{matriz}")
print(f"Flatten: {matriz.flatten()}")

# Concatenar
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"\nConcatenar: {np.concatenate([a, b])}")

# Apilar
print(f"Apilar vertical:\n{np.vstack([a, b])}")
print(f"Apilar horizontal: {np.hstack([a, b])}")


# ==============================================================================
# BROADCASTING
# ==============================================================================

print("\n" + "=" * 60)
print("BROADCASTING")
print("=" * 60)

print("""
Broadcasting permite operar arrays de diferentes shapes.
NumPy automáticamente "expande" el array más pequeño.

Reglas:
1. Si tienen diferente número de dimensiones, se añaden 1s a la izquierda
2. Las dimensiones se comparan de derecha a izquierda
3. Son compatibles si son iguales o una de ellas es 1
""")

# Escalar + array
arr = np.array([1, 2, 3])
print(f"Array: {arr}")
print(f"Array + 10: {arr + 10}")

# Array 2D + array 1D
matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])
fila = np.array([10, 20, 30])
print(f"\nMatriz:\n{matriz}")
print(f"Fila: {fila}")
print(f"Matriz + Fila:\n{matriz + fila}")

# Operación entre columna y fila
columna = np.array([[1], [2], [3]])
fila = np.array([10, 20, 30])
print(f"\nColumna:\n{columna}")
print(f"Fila: {fila}")
print(f"Columna + Fila (crea matriz):\n{columna + fila}")


# ==============================================================================
# EJEMPLO PRÁCTICO: NORMALIZACIÓN DE DATOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO: Normalización de datos para ML")
print("=" * 60)

# Datos de ejemplo (como features para ML)
datos = np.array([
    [150, 60, 25],   # altura, peso, edad
    [165, 70, 30],
    [180, 85, 35],
    [155, 55, 22],
    [170, 75, 28]
])
print(f"Datos originales:\n{datos}")

# Min-Max normalization: escala a [0, 1]
min_vals = datos.min(axis=0)
max_vals = datos.max(axis=0)
datos_minmax = (datos - min_vals) / (max_vals - min_vals)
print(f"\nNormalización Min-Max [0,1]:\n{np.round(datos_minmax, 3)}")

# Z-score normalization: media=0, std=1
media = datos.mean(axis=0)
std = datos.std(axis=0)
datos_zscore = (datos - media) / std
print(f"\nNormalización Z-score:\n{np.round(datos_zscore, 3)}")

print("\n" + "=" * 60)
print("PRÓXIMO: 02_pandas_fundamentos.py")
print("=" * 60)
