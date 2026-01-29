"""
================================================================================
INTRODUCCIÓN A TENSORFLOW
================================================================================

PREREQUISITOS:
- 01_estructuras_de_datos_arbol.py
- 02_que_es_una_neurona.py
- 03_red_neuronal_desde_cero.py

INSTALACIÓN:
    pip install tensorflow

================================================================================
¿QUÉ ES TENSORFLOW?
================================================================================

TensorFlow es un framework de deep learning desarrollado por Google que permite:

1. Construir redes neuronales de forma declarativa
2. Calcular gradientes automáticamente (autograd)
3. Entrenar en GPU/TPU para mayor velocidad
4. Desplegar modelos en producción

El nombre viene de:
- TENSOR: Estructura de datos multidimensional (generalización de matrices)
- FLOW: Los datos "fluyen" a través del grafo computacional

================================================================================
¿POR QUÉ USAR UN FRAMEWORK?
================================================================================

En el archivo anterior implementamos backpropagation manualmente.
Esto es educativo pero:
- Propenso a errores
- Lento (Python puro)
- Difícil de escalar
- No aprovecha GPU

TensorFlow resuelve todo esto automáticamente.

================================================================================
"""

# ==============================================================================
# IMPORTACIONES Y CONFIGURACIÓN
# ==============================================================================

print("=" * 60)
print("TENSORFLOW: Configuración inicial")
print("=" * 60)

try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers
    import numpy as np

    print(f"TensorFlow versión: {tf.__version__}")
    print(f"GPU disponible: {len(tf.config.list_physical_devices('GPU')) > 0}")
    TF_DISPONIBLE = True

except ImportError:
    print("TensorFlow no está instalado.")
    print("Instálalo con: pip install tensorflow")
    print("\nEste archivo muestra el código que usarías con TensorFlow.")
    TF_DISPONIBLE = False


# ==============================================================================
# TENSORES: La estructura de datos fundamental
# ==============================================================================

if TF_DISPONIBLE:
    print("\n" + "=" * 60)
    print("TENSORES: Estructura de datos de TensorFlow")
    print("=" * 60)

    print("""
    Un tensor es una generalización de vectores y matrices:

    - Escalar (0D): un solo número → tf.constant(5)
    - Vector (1D): lista de números → tf.constant([1, 2, 3])
    - Matriz (2D): tabla de números → tf.constant([[1, 2], [3, 4]])
    - Tensor 3D+: imágenes, videos, etc.
    """)

    # Ejemplos de tensores
    escalar = tf.constant(5)
    vector = tf.constant([1.0, 2.0, 3.0])
    matriz = tf.constant([[1, 2], [3, 4], [5, 6]])
    tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    print(f"Escalar: {escalar}, shape: {escalar.shape}")
    print(f"Vector: {vector}, shape: {vector.shape}")
    print(f"Matriz:\n{matriz}\nshape: {matriz.shape}")
    print(f"Tensor 3D shape: {tensor_3d.shape}")


# ==============================================================================
# EJEMPLO 1: XOR con Keras (API de alto nivel)
# ==============================================================================

if TF_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO 1: Resolver XOR con Keras")
    print("=" * 60)

    print("""
    Keras es la API de alto nivel de TensorFlow.
    Permite construir modelos de forma muy sencilla.
    """)

    # Datos XOR
    X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
    y_xor = np.array([[0], [1], [1], [0]], dtype=np.float32)

    # Construir el modelo
    modelo_xor = keras.Sequential([
        # Capa de entrada: 2 entradas
        layers.Input(shape=(2,)),

        # Capa oculta: 4 neuronas, activación ReLU
        layers.Dense(4, activation='relu', name='capa_oculta'),

        # Capa de salida: 1 neurona, activación sigmoide
        layers.Dense(1, activation='sigmoid', name='capa_salida')
    ])

    # Mostrar arquitectura
    print("\nArquitectura del modelo:")
    modelo_xor.summary()

    # Compilar: definir optimizador y función de pérdida
    modelo_xor.compile(
        optimizer='adam',           # Optimizador (variante de SGD)
        loss='binary_crossentropy', # Función de pérdida para clasificación binaria
        metrics=['accuracy']        # Métrica a monitorear
    )

    # Entrenar
    print("\nEntrenando...")
    historia = modelo_xor.fit(
        X_xor, y_xor,
        epochs=1000,
        verbose=0  # Sin output durante entrenamiento
    )

    # Evaluar
    print("\nPredicciones después de entrenar:")
    predicciones = modelo_xor.predict(X_xor, verbose=0)
    for i, (entrada, pred, real) in enumerate(zip(X_xor, predicciones, y_xor)):
        print(f"  {int(entrada[0])} XOR {int(entrada[1])} = {pred[0]:.4f} → {round(pred[0])} (real: {int(real[0])})")


# ==============================================================================
# EJEMPLO 2: Clasificación de dígitos MNIST
# ==============================================================================

if TF_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO 2: Clasificación de dígitos escritos a mano (MNIST)")
    print("=" * 60)

    print("""
    MNIST es el "Hello World" del deep learning:
    - 60,000 imágenes de entrenamiento
    - 10,000 imágenes de prueba
    - Dígitos del 0 al 9
    - Imágenes de 28x28 píxeles en escala de grises
    """)

    # Cargar datos
    (X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

    # Normalizar: valores de 0-255 a 0-1
    X_train = X_train.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0

    # Aplanar: de 28x28 a 784 (para red densa)
    X_train_flat = X_train.reshape(-1, 784)
    X_test_flat = X_test.reshape(-1, 784)

    print(f"\nForma de datos de entrenamiento: {X_train.shape}")
    print(f"Forma aplanada: {X_train_flat.shape}")

    # Construir modelo
    modelo_mnist = keras.Sequential([
        layers.Input(shape=(784,)),
        layers.Dense(128, activation='relu', name='oculta_1'),
        layers.Dropout(0.2),  # Regularización: apaga 20% de neuronas aleatoriamente
        layers.Dense(64, activation='relu', name='oculta_2'),
        layers.Dropout(0.2),
        layers.Dense(10, activation='softmax', name='salida')  # 10 clases
    ])

    modelo_mnist.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',  # Para etiquetas enteras
        metrics=['accuracy']
    )

    print("\nArquitectura del modelo MNIST:")
    modelo_mnist.summary()

    # Entrenar (solo 5 épocas para demostración)
    print("\nEntrenando (5 épocas)...")
    modelo_mnist.fit(
        X_train_flat, y_train,
        epochs=5,
        batch_size=32,
        validation_split=0.1,
        verbose=1
    )

    # Evaluar en datos de prueba
    loss, accuracy = modelo_mnist.evaluate(X_test_flat, y_test, verbose=0)
    print(f"\nPrecisión en datos de prueba: {accuracy * 100:.2f}%")


# ==============================================================================
# EJEMPLO 3: Guardar y cargar modelos
# ==============================================================================

if TF_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO 3: Guardar y cargar modelos")
    print("=" * 60)

    print("""
    TensorFlow permite guardar modelos entrenados para:
    - Continuar entrenamiento después
    - Usar en producción
    - Compartir con otros

    Formatos:
    - SavedModel: formato nativo de TensorFlow
    - HDF5: formato más portable (.h5)
    """)

    # Guardar modelo (comentado para no crear archivos)
    print("""
    # Guardar en formato SavedModel
    modelo_mnist.save('mi_modelo_mnist')

    # Guardar en formato HDF5
    modelo_mnist.save('mi_modelo_mnist.h5')

    # Cargar modelo
    modelo_cargado = keras.models.load_model('mi_modelo_mnist')

    # Solo guardar pesos
    modelo_mnist.save_weights('pesos_mnist.weights.h5')

    # Cargar pesos en un modelo con la misma arquitectura
    modelo_nuevo = crear_modelo()  # Debe tener misma arquitectura
    modelo_nuevo.load_weights('pesos_mnist.weights.h5')
    """)


# ==============================================================================
# CONCEPTOS CLAVE DE TENSORFLOW/KERAS
# ==============================================================================

print("\n" + "=" * 60)
print("CONCEPTOS CLAVE")
print("=" * 60)

print("""
1. CAPAS COMUNES (layers):
   - Dense: Capa totalmente conectada
   - Conv2D: Convolución para imágenes
   - LSTM/GRU: Para secuencias (texto, series temporales)
   - Dropout: Regularización
   - BatchNormalization: Estabiliza entrenamiento

2. FUNCIONES DE ACTIVACIÓN:
   - relu: max(0, x) - la más común
   - sigmoid: Para clasificación binaria (salida)
   - softmax: Para clasificación multiclase (salida)
   - tanh: Alternativa a sigmoid

3. OPTIMIZADORES:
   - SGD: Descenso de gradiente estocástico básico
   - Adam: SGD con momentum adaptativo (más usado)
   - RMSprop: Bueno para RNNs

4. FUNCIONES DE PÉRDIDA:
   - binary_crossentropy: Clasificación binaria
   - categorical_crossentropy: Multiclase (one-hot)
   - sparse_categorical_crossentropy: Multiclase (enteros)
   - mse: Regresión

5. CALLBACKS (durante entrenamiento):
   - EarlyStopping: Para cuando no mejora
   - ModelCheckpoint: Guarda mejores pesos
   - TensorBoard: Visualización
""")

# ==============================================================================
# EJEMPLO DE CÓDIGO COMPLETO
# ==============================================================================

print("\n" + "=" * 60)
print("PLANTILLA: Modelo completo")
print("=" * 60)

print("""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. PREPARAR DATOS
X_train, y_train = ...  # Tus datos de entrenamiento
X_test, y_test = ...    # Tus datos de prueba

# 2. CONSTRUIR MODELO
modelo = keras.Sequential([
    layers.Input(shape=(num_features,)),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_clases, activation='softmax')
])

# 3. COMPILAR
modelo.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 4. ENTRENAR
callbacks = [
    keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
    keras.callbacks.ModelCheckpoint('mejor_modelo.keras', save_best_only=True)
]

historia = modelo.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=callbacks
)

# 5. EVALUAR
loss, accuracy = modelo.evaluate(X_test, y_test)
print(f"Precisión: {accuracy * 100:.2f}%")

# 6. PREDECIR
predicciones = modelo.predict(X_nuevo)
""")

print("\n" + "=" * 60)
print("PRÓXIMO: 05_pytorch_intro.py - Framework alternativo")
print("=" * 60)
