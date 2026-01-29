"""
================================================================================
RED NEURONAL DESDE CERO
================================================================================

PREREQUISITOS:
- 01_estructuras_de_datos_arbol.py (estructura jerárquica)
- 02_que_es_una_neurona.py (neurona individual)

================================================================================
¿QUÉ ES UNA RED NEURONAL?
================================================================================

Una red neuronal es un conjunto de neuronas organizadas en CAPAS que trabajan
juntas para aprender patrones complejos en los datos.

Estructura básica:

    CAPA DE           CAPA(S)            CAPA DE
    ENTRADA           OCULTA(S)          SALIDA

    [x₁] ─────┐     ┌─[h₁]─┐           ┌─[y₁]
              ├─────┤      ├───────────┤
    [x₂] ─────┤     └─[h₂]─┘           └─[y₂]
              │
    [x₃] ─────┘

Donde:
- Capa de entrada: Recibe los datos crudos
- Capas ocultas: Procesan y transforman los datos
- Capa de salida: Produce el resultado final

================================================================================
¿POR QUÉ MÚLTIPLES CAPAS?
================================================================================

Recordemos el problema XOR: una neurona no puede resolverlo.
Con múltiples neuronas organizadas en capas, SÍ podemos.

XOR = (A AND NOT B) OR (NOT A AND B)

Podemos descomponerlo así:

Capa oculta:
- Neurona 1: calcula (A AND NOT B)
- Neurona 2: calcula (NOT A AND B)

Capa de salida:
- Neurona 3: OR de las salidas anteriores

================================================================================
"""

import math
import random

# Configuramos semilla para reproducibilidad
random.seed(42)


# ==============================================================================
# FUNCIONES DE ACTIVACIÓN Y SUS DERIVADAS
# ==============================================================================

def sigmoide(x):
    """Función sigmoide: σ(x) = 1 / (1 + e^(-x))"""
    # Evitamos overflow para valores muy negativos
    if x < -500:
        return 0.0
    return 1 / (1 + math.exp(-x))


def derivada_sigmoide(x):
    """
    Derivada de la sigmoide: σ'(x) = σ(x) * (1 - σ(x))

    La derivada es crucial para el aprendizaje (backpropagation).
    Nos dice "cuánto cambia la salida si cambiamos un poco la entrada".
    """
    s = sigmoide(x)
    return s * (1 - s)


# ==============================================================================
# CLASE NEURONA MEJORADA (con derivada para aprendizaje)
# ==============================================================================

class Neurona:
    """
    Neurona con capacidad de aprendizaje.

    Mejoras sobre la versión anterior:
    - Almacena las entradas para backpropagation
    - Puede calcular derivadas
    - Tiene métodos para actualizar pesos
    """

    def __init__(self, n_entradas):
        """
        Inicializa la neurona.

        Args:
            n_entradas: Número de conexiones de entrada
        """
        self.n_entradas = n_entradas

        # Inicialización Xavier/Glorot: mejora el aprendizaje
        limite = math.sqrt(6 / (n_entradas + 1))
        self.pesos = [random.uniform(-limite, limite) for _ in range(n_entradas)]
        self.sesgo = random.uniform(-limite, limite)

        # Valores guardados para backpropagation
        self.entradas = []
        self.suma_ponderada = 0
        self.salida = 0

    def forward(self, entradas):
        """
        Propagación hacia adelante (forward propagation).

        Calcula la salida de la neurona y guarda valores intermedios.

        Args:
            entradas: Lista de valores de entrada

        Returns:
            float: Salida de la neurona (después de activación)
        """
        self.entradas = entradas

        # Suma ponderada
        self.suma_ponderada = sum(
            e * p for e, p in zip(entradas, self.pesos)
        ) + self.sesgo

        # Activación sigmoide
        self.salida = sigmoide(self.suma_ponderada)

        return self.salida

    def __str__(self):
        pesos_str = [f"{p:.4f}" for p in self.pesos]
        return f"Neurona(pesos={pesos_str}, sesgo={self.sesgo:.4f})"


# ==============================================================================
# CLASE CAPA: Conjunto de neuronas
# ==============================================================================

class Capa:
    """
    Una capa de la red neuronal.

    Una capa contiene múltiples neuronas que procesan las mismas entradas
    pero con diferentes pesos, produciendo múltiples salidas.
    """

    def __init__(self, n_neuronas, n_entradas_por_neurona):
        """
        Crea una capa con el número especificado de neuronas.

        Args:
            n_neuronas: Cuántas neuronas tendrá esta capa
            n_entradas_por_neurona: Cuántas entradas recibe cada neurona
        """
        self.neuronas = [
            Neurona(n_entradas_por_neurona) for _ in range(n_neuronas)
        ]
        self.salidas = []

    def forward(self, entradas):
        """
        Propaga las entradas a través de todas las neuronas de la capa.

        Args:
            entradas: Lista de valores de entrada

        Returns:
            list: Lista de salidas (una por neurona)
        """
        self.salidas = [neurona.forward(entradas) for neurona in self.neuronas]
        return self.salidas

    def __str__(self):
        return f"Capa({len(self.neuronas)} neuronas)"


# ==============================================================================
# CLASE RED NEURONAL
# ==============================================================================

class RedNeuronal:
    """
    Red neuronal multicapa (Multilayer Perceptron - MLP).

    Arquitectura:
    - Capa de entrada: solo pasa los datos (no es una capa real de neuronas)
    - Capas ocultas: procesan la información
    - Capa de salida: produce el resultado final

    Ejemplo de arquitectura [2, 3, 1]:
    - 2 entradas
    - 1 capa oculta con 3 neuronas
    - 1 salida
    """

    def __init__(self, arquitectura):
        """
        Crea la red neuronal según la arquitectura especificada.

        Args:
            arquitectura: Lista con el número de neuronas por capa.
                         El primer número son las entradas,
                         el último es la salida.

        Ejemplo:
            RedNeuronal([2, 4, 3, 1])
            - 2 entradas
            - Primera capa oculta: 4 neuronas
            - Segunda capa oculta: 3 neuronas
            - Capa de salida: 1 neurona
        """
        self.arquitectura = arquitectura
        self.capas = []

        # Creamos las capas (empezando desde la primera capa oculta)
        for i in range(1, len(arquitectura)):
            n_neuronas = arquitectura[i]
            n_entradas = arquitectura[i - 1]
            capa = Capa(n_neuronas, n_entradas)
            self.capas.append(capa)

        print(f"Red creada con arquitectura: {arquitectura}")
        print(f"Total de capas (sin contar entrada): {len(self.capas)}")

    def forward(self, entradas):
        """
        Propagación hacia adelante a través de toda la red.

        Los datos fluyen:
        entrada → capa_oculta_1 → ... → capa_oculta_n → salida

        Args:
            entradas: Lista de valores de entrada

        Returns:
            list: Salidas de la última capa
        """
        salida_actual = entradas

        # Propagamos a través de cada capa
        for capa in self.capas:
            salida_actual = capa.forward(salida_actual)

        return salida_actual

    def predecir(self, entradas):
        """
        Realiza una predicción (alias más intuitivo de forward).

        Args:
            entradas: Datos de entrada

        Returns:
            list: Predicción de la red
        """
        return self.forward(entradas)


# ==============================================================================
# EJEMPLO 1: RED SIMPLE PARA XOR
# ==============================================================================

print("=" * 60)
print("EJEMPLO 1: Red neuronal para el problema XOR")
print("=" * 60)

print("""
Problema XOR:
  A | B | A XOR B
  0 | 0 |    0
  0 | 1 |    1
  1 | 0 |    1
  1 | 1 |    0

Arquitectura: [2, 2, 1]
- 2 entradas (A y B)
- 1 capa oculta con 2 neuronas
- 1 salida
""")

# Creamos la red
red_xor = RedNeuronal([2, 2, 1])

# Datos de entrenamiento XOR
datos_xor = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

print("\nPredicciones ANTES de entrenar (pesos aleatorios):")
print("-" * 40)
for entrada, esperado in datos_xor:
    prediccion = red_xor.predecir(entrada)
    print(f"  Entrada: {entrada} → Predicción: {prediccion[0]:.4f} (esperado: {esperado})")


# ==============================================================================
# ENTRENAMIENTO: BACKPROPAGATION
# ==============================================================================

print("\n" + "=" * 60)
print("ENTRENAMIENTO: Algoritmo de Backpropagation")
print("=" * 60)

print("""
¿Cómo aprende una red neuronal?

1. FORWARD PROPAGATION: Calculamos la predicción
2. CALCULAR ERROR: Comparamos predicción con valor real
3. BACKPROPAGATION: Propagamos el error hacia atrás
4. ACTUALIZAR PESOS: Ajustamos pesos para reducir el error

Este proceso se repite miles de veces (épocas).

El algoritmo backpropagation usa la REGLA DE LA CADENA del cálculo
para determinar cuánto contribuye cada peso al error final.
""")


def entrenar_red(red, datos, epocas=10000, tasa_aprendizaje=0.5):
    """
    Entrena la red neuronal usando backpropagation.

    Args:
        red: La red neuronal a entrenar
        datos: Lista de tuplas (entrada, salida_esperada)
        epocas: Número de iteraciones de entrenamiento
        tasa_aprendizaje: Qué tan grandes son los ajustes (learning rate)

    Returns:
        list: Historial del error por época
    """
    historial_error = []

    for epoca in range(epocas):
        error_total = 0

        for entrada, esperado in datos:
            # ============================================
            # PASO 1: FORWARD PROPAGATION
            # ============================================
            salida = red.forward(entrada)

            # ============================================
            # PASO 2: CALCULAR ERROR
            # ============================================
            # Error cuadrático: (esperado - obtenido)²
            if isinstance(esperado, list):
                error = sum((e - s) ** 2 for e, s in zip(esperado, salida))
            else:
                error = (esperado - salida[0]) ** 2
            error_total += error

            # ============================================
            # PASO 3: BACKPROPAGATION
            # ============================================
            # Calculamos los deltas (gradientes) para cada capa

            # Para la capa de salida
            capa_salida = red.capas[-1]
            deltas_salida = []

            for i, neurona in enumerate(capa_salida.neuronas):
                if isinstance(esperado, list):
                    error_neurona = esperado[i] - neurona.salida
                else:
                    error_neurona = esperado - neurona.salida

                # delta = error * derivada de la activación
                delta = error_neurona * derivada_sigmoide(neurona.suma_ponderada)
                deltas_salida.append(delta)

            # Para las capas ocultas (propagamos hacia atrás)
            deltas_por_capa = [deltas_salida]

            for l in range(len(red.capas) - 2, -1, -1):
                capa_actual = red.capas[l]
                capa_siguiente = red.capas[l + 1]
                deltas_anterior = deltas_por_capa[0]

                deltas_capa = []
                for i, neurona in enumerate(capa_actual.neuronas):
                    # Suma de errores propagados desde la capa siguiente
                    error_propagado = sum(
                        deltas_anterior[j] * capa_siguiente.neuronas[j].pesos[i]
                        for j in range(len(capa_siguiente.neuronas))
                    )
                    delta = error_propagado * derivada_sigmoide(neurona.suma_ponderada)
                    deltas_capa.append(delta)

                deltas_por_capa.insert(0, deltas_capa)

            # ============================================
            # PASO 4: ACTUALIZAR PESOS
            # ============================================
            for l, capa in enumerate(red.capas):
                if l == 0:
                    entradas_capa = entrada
                else:
                    entradas_capa = red.capas[l - 1].salidas

                for i, neurona in enumerate(capa.neuronas):
                    delta = deltas_por_capa[l][i]

                    # Actualizar cada peso
                    for j in range(len(neurona.pesos)):
                        neurona.pesos[j] += tasa_aprendizaje * delta * entradas_capa[j]

                    # Actualizar sesgo
                    neurona.sesgo += tasa_aprendizaje * delta

        # Guardamos el error promedio de esta época
        error_promedio = error_total / len(datos)
        historial_error.append(error_promedio)

        # Mostramos progreso cada 1000 épocas
        if (epoca + 1) % 2000 == 0:
            print(f"  Época {epoca + 1:5d}: Error = {error_promedio:.6f}")

    return historial_error


# Entrenamos la red XOR
print("\nEntrenando la red XOR...")
print("-" * 40)
historial = entrenar_red(red_xor, datos_xor, epocas=10000, tasa_aprendizaje=0.5)

print("\nPredicciones DESPUÉS de entrenar:")
print("-" * 40)
for entrada, esperado in datos_xor:
    prediccion = red_xor.predecir(entrada)
    redondeado = round(prediccion[0])
    correcto = "✓" if redondeado == esperado else "✗"
    print(f"  {entrada[0]} XOR {entrada[1]} = {prediccion[0]:.4f} → {redondeado} (esperado: {esperado}) {correcto}")


# ==============================================================================
# EJEMPLO 2: CLASIFICACIÓN DE PUNTOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO 2: Clasificación de puntos en un plano")
print("=" * 60)

print("""
Problema: Clasificar puntos según si están dentro o fuera de un círculo.

Puntos dentro del círculo (radio 0.5, centro en 0.5, 0.5) → Clase 1
Puntos fuera → Clase 0
""")

# Generamos datos de entrenamiento
def generar_datos_circulo(n_puntos):
    """
    Genera puntos aleatorios y los clasifica según un círculo.
    """
    datos = []
    centro_x, centro_y = 0.5, 0.5
    radio = 0.35

    for _ in range(n_puntos):
        x = random.random()
        y = random.random()

        # Distancia al centro
        distancia = math.sqrt((x - centro_x)**2 + (y - centro_y)**2)

        # Clase: 1 si está dentro del círculo, 0 si está fuera
        clase = 1 if distancia < radio else 0

        datos.append(([x, y], clase))

    return datos


# Generamos datos
datos_circulo = generar_datos_circulo(200)

# Creamos una red más grande para este problema
red_circulo = RedNeuronal([2, 8, 4, 1])

print("\nEntrenando red para clasificar puntos...")
print("-" * 40)
historial_circulo = entrenar_red(
    red_circulo,
    datos_circulo,
    epocas=5000,
    tasa_aprendizaje=0.3
)

# Evaluamos la precisión
aciertos = 0
for entrada, esperado in datos_circulo:
    prediccion = red_circulo.predecir(entrada)
    if round(prediccion[0]) == esperado:
        aciertos += 1

precision = aciertos / len(datos_circulo) * 100
print(f"\nPrecisión en datos de entrenamiento: {precision:.1f}%")


# ==============================================================================
# VISUALIZACIÓN DEL APRENDIZAJE
# ==============================================================================

print("\n" + "=" * 60)
print("VISUALIZACIÓN: Evolución del error")
print("=" * 60)

print("""
Gráfica ASCII del error durante el entrenamiento de XOR:
(Error más bajo = mejor aprendizaje)
""")

# Tomamos muestras del historial para graficar
muestras = 20
paso = len(historial) // muestras

errores_muestra = [historial[i * paso] for i in range(muestras)]
max_error = max(errores_muestra)

print("Error")
print("  │")
for i, error in enumerate(errores_muestra):
    barras = int((error / max_error) * 40)
    epoca = i * paso
    print(f"  │{'█' * barras}")
print("  └" + "─" * 42 + "→ Época")
print(f"   0{' ' * 18}{len(historial)//2}{' ' * 17}{len(historial)}")


# ==============================================================================
# RESUMEN Y PRÓXIMOS PASOS
# ==============================================================================

print("\n" + "=" * 60)
print("RESUMEN: Lo que hemos aprendido")
print("=" * 60)

print("""
1. ESTRUCTURA DE UNA RED NEURONAL:
   - Capas de entrada, ocultas y salida
   - Cada neurona conectada con la capa siguiente
   - Los pesos determinan la fuerza de cada conexión

2. FORWARD PROPAGATION:
   - Los datos fluyen de entrada a salida
   - Cada neurona: suma ponderada → activación → salida

3. BACKPROPAGATION:
   - Calcula cuánto contribuye cada peso al error
   - Usa la regla de la cadena para propagar gradientes
   - Permite ajustar millones de pesos eficientemente

4. ENTRENAMIENTO:
   - Repetir forward + backward miles de veces
   - La tasa de aprendizaje controla el tamaño de los ajustes
   - El error disminuye gradualmente

PRÓXIMOS PASOS:
- 04_tensorflow_intro.py: Usar frameworks profesionales
- 05_pytorch_intro.py: Alternativa popular para investigación
- Estos frameworks hacen todo esto automáticamente y más rápido
""")

print("=" * 60)
print("Archivo completado. La red funciona, ¡ahora usa frameworks!")
print("=" * 60)
