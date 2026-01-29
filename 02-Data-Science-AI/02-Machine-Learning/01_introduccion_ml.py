"""
================================================================================
INTRODUCCIÓN AL MACHINE LEARNING
================================================================================

¿QUÉ ES MACHINE LEARNING?
-------------------------
Machine Learning (Aprendizaje Automático) es una rama de la IA que permite
a las computadoras aprender patrones de los datos sin ser programadas
explícitamente para cada tarea.

En lugar de escribir reglas:
    SI temperatura > 30 Y humedad < 40 ENTONCES "día caluroso"

El modelo aprende las reglas a partir de ejemplos:
    Datos históricos → Entrenamiento → Modelo → Predicciones

================================================================================
TIPOS DE MACHINE LEARNING
================================================================================

1. APRENDIZAJE SUPERVISADO
   - Tenemos datos etiquetados (input → output conocido)
   - El modelo aprende la relación input → output
   - Ejemplos: clasificación de emails, predicción de precios

2. APRENDIZAJE NO SUPERVISADO
   - Solo tenemos inputs, sin etiquetas
   - El modelo encuentra patrones/estructuras ocultas
   - Ejemplos: segmentación de clientes, reducción dimensional

3. APRENDIZAJE POR REFUERZO
   - Un agente aprende mediante prueba y error
   - Recibe recompensas/penalizaciones por sus acciones
   - Ejemplos: juegos, robótica, trading

================================================================================
"""

import numpy as np

# ==============================================================================
# CONCEPTOS FUNDAMENTALES
# ==============================================================================

print("=" * 60)
print("CONCEPTOS FUNDAMENTALES DE MACHINE LEARNING")
print("=" * 60)

print("""
TERMINOLOGÍA BÁSICA:
-------------------

1. FEATURES (Características/Variables):
   - Los atributos de entrada que usa el modelo
   - Ejemplo: [edad, peso, altura] para predecir diabetes
   - También llamadas: variables independientes, X

2. TARGET (Objetivo/Etiqueta):
   - Lo que queremos predecir
   - Ejemplo: tiene_diabetes (Sí/No)
   - También llamada: variable dependiente, y

3. DATASET (Conjunto de datos):
   - Colección de ejemplos con features y targets
   - Se divide en: entrenamiento, validación, prueba

4. MODELO:
   - El algoritmo que aprende los patrones
   - Ejemplos: Regresión, Árboles de decisión, Redes neuronales

5. ENTRENAMIENTO (Training):
   - Proceso de ajustar el modelo a los datos
   - El modelo encuentra los parámetros óptimos

6. PREDICCIÓN (Inference):
   - Usar el modelo entrenado con datos nuevos
""")


# ==============================================================================
# EJEMPLO: REGRESIÓN LINEAL DESDE CERO
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO: Regresión Lineal (el modelo más simple)")
print("=" * 60)

print("""
La regresión lineal busca una línea que mejor se ajuste a los datos:

    y = mx + b

Donde:
- m = pendiente (slope)
- b = intercepto (bias)

El modelo aprende los valores óptimos de m y b.
""")


class RegresionLinealSimple:
    """
    Implementación de regresión lineal desde cero.

    Usa descenso de gradiente para encontrar los parámetros óptimos.
    """

    def __init__(self, tasa_aprendizaje=0.01):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.m = 0  # pendiente
        self.b = 0  # intercepto
        self.historial_error = []

    def predecir(self, X):
        """Predice y = mX + b"""
        return self.m * X + self.b

    def calcular_error(self, X, y):
        """
        Calcula el Error Cuadrático Medio (MSE).

        MSE = (1/n) * Σ(y_real - y_predicho)²
        """
        predicciones = self.predecir(X)
        return np.mean((y - predicciones) ** 2)

    def entrenar(self, X, y, epocas=1000):
        """
        Entrena el modelo usando descenso de gradiente.

        En cada época:
        1. Calcula predicciones
        2. Calcula gradientes (derivadas del error)
        3. Actualiza m y b en la dirección que reduce el error
        """
        n = len(X)

        for epoca in range(epocas):
            # Predicciones actuales
            y_pred = self.predecir(X)

            # Gradientes (derivadas parciales del MSE)
            # ∂MSE/∂m = (-2/n) * Σ(y - y_pred) * X
            # ∂MSE/∂b = (-2/n) * Σ(y - y_pred)
            gradiente_m = (-2/n) * np.sum((y - y_pred) * X)
            gradiente_b = (-2/n) * np.sum(y - y_pred)

            # Actualizar parámetros
            self.m -= self.tasa_aprendizaje * gradiente_m
            self.b -= self.tasa_aprendizaje * gradiente_b

            # Guardar error
            error = self.calcular_error(X, y)
            self.historial_error.append(error)

            if (epoca + 1) % 200 == 0:
                print(f"  Época {epoca + 1}: Error = {error:.4f}, m = {self.m:.4f}, b = {self.b:.4f}")

        return self


# Crear datos de ejemplo: y = 2x + 1 + ruido
np.random.seed(42)
X = np.linspace(0, 10, 50)
y = 2 * X + 1 + np.random.randn(50) * 2  # y = 2x + 1 + ruido

print("\nDatos de entrenamiento:")
print(f"  X: valores de 0 a 10")
print(f"  y: aproximadamente 2*X + 1 + ruido")

# Entrenar modelo
modelo = RegresionLinealSimple(tasa_aprendizaje=0.01)
print("\nEntrenando...")
modelo.entrenar(X, y, epocas=1000)

print(f"\nParámetros aprendidos:")
print(f"  m (pendiente) = {modelo.m:.4f} (real: 2)")
print(f"  b (intercepto) = {modelo.b:.4f} (real: 1)")

# Predicción
nuevo_x = 15
prediccion = modelo.predecir(nuevo_x)
print(f"\nPredicción para x={nuevo_x}: y = {prediccion:.2f}")


# ==============================================================================
# DIVISIÓN DE DATOS: TRAIN/TEST SPLIT
# ==============================================================================

print("\n" + "=" * 60)
print("DIVISIÓN DE DATOS: Entrenamiento y Prueba")
print("=" * 60)

print("""
¿Por qué dividir los datos?

Si evaluamos el modelo con los mismos datos de entrenamiento,
no sabemos si realmente aprendió patrones generales o solo
memorizó los datos (OVERFITTING).

División típica:
- Entrenamiento (70-80%): Para que el modelo aprenda
- Prueba (20-30%): Para evaluar rendimiento real

División avanzada:
- Entrenamiento (60%): Aprender
- Validación (20%): Ajustar hiperparámetros
- Prueba (20%): Evaluación final
""")


def train_test_split(X, y, test_size=0.2, random_state=None):
    """
    Divide los datos en conjuntos de entrenamiento y prueba.

    Args:
        X: Features
        y: Target
        test_size: Proporción para prueba (0-1)
        random_state: Semilla para reproducibilidad
    """
    if random_state is not None:
        np.random.seed(random_state)

    n = len(X)
    indices = np.random.permutation(n)

    n_test = int(n * test_size)
    test_indices = indices[:n_test]
    train_indices = indices[n_test:]

    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]


# Ejemplo de división
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Datos totales: {len(X)}")
print(f"Entrenamiento: {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
print(f"Prueba: {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")


# ==============================================================================
# MÉTRICAS DE EVALUACIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTRICAS DE EVALUACIÓN")
print("=" * 60)

print("""
REGRESIÓN (predecir valores continuos):
---------------------------------------
- MSE (Mean Squared Error): Error cuadrático medio
- RMSE (Root MSE): Raíz del MSE (mismas unidades que y)
- MAE (Mean Absolute Error): Error absoluto medio
- R² (Coeficiente de determinación): Qué tan bien se ajusta (0-1)

CLASIFICACIÓN (predecir categorías):
-----------------------------------
- Accuracy: % de predicciones correctas
- Precision: De los predichos positivos, % realmente positivos
- Recall: De los realmente positivos, % predichos correctamente
- F1-Score: Media armónica de Precision y Recall
""")


def calcular_metricas_regresion(y_real, y_pred):
    """Calcula métricas comunes de regresión."""
    mse = np.mean((y_real - y_pred) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(y_real - y_pred))

    # R² = 1 - (SS_res / SS_tot)
    ss_res = np.sum((y_real - y_pred) ** 2)
    ss_tot = np.sum((y_real - np.mean(y_real)) ** 2)
    r2 = 1 - (ss_res / ss_tot)

    return {
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae,
        'R²': r2
    }


# Evaluar nuestro modelo
y_pred_test = modelo.predecir(X_test)
metricas = calcular_metricas_regresion(y_test, y_pred_test)

print("\nMétricas en datos de prueba:")
for nombre, valor in metricas.items():
    print(f"  {nombre}: {valor:.4f}")


# ==============================================================================
# FLUJO DE TRABAJO ML
# ==============================================================================

print("\n" + "=" * 60)
print("FLUJO DE TRABAJO DE MACHINE LEARNING")
print("=" * 60)

print("""
1. DEFINIR EL PROBLEMA
   - ¿Qué queremos predecir?
   - ¿Supervisado o no supervisado?
   - ¿Clasificación o regresión?

2. RECOLECTAR Y EXPLORAR DATOS
   - Obtener datos relevantes
   - Análisis exploratorio (EDA)
   - Visualizar distribuciones y relaciones

3. PREPARAR DATOS
   - Limpiar: valores faltantes, outliers
   - Transformar: normalización, encoding
   - Feature engineering: crear nuevas variables

4. SELECCIONAR Y ENTRENAR MODELOS
   - Probar varios algoritmos
   - Ajustar hiperparámetros
   - Validación cruzada

5. EVALUAR
   - Métricas en datos de prueba
   - Analizar errores
   - Verificar overfitting/underfitting

6. DESPLEGAR Y MONITOREAR
   - Poner en producción
   - Monitorear rendimiento
   - Re-entrenar cuando sea necesario

PRÓXIMO ARCHIVO: Aprenderemos a usar Scikit-learn
para hacer todo esto de forma práctica y eficiente.
""")

print("=" * 60)
print("PRÓXIMO: 02_scikit_learn_basico.py")
print("=" * 60)
