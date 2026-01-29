"""
================================================================================
¿QUÉ ES UNA NEURONA? - De la biología a las matemáticas
================================================================================

PREREQUISITOS:
- Entender estructuras básicas de datos (ver 01_estructuras_de_datos_arbol.py)
- Conocimientos básicos de Python (funciones, clases)

================================================================================
LA NEURONA BIOLÓGICA
================================================================================

Una neurona biológica es una célula del sistema nervioso que:

1. RECIBE señales de otras neuronas a través de DENDRITAS
2. PROCESA las señales en el CUERPO CELULAR (soma)
3. Si la señal supera un UMBRAL, genera un impulso eléctrico
4. TRANSMITE el impulso a través del AXÓN hacia otras neuronas

Representación simplificada:

    [Entrada 1] ──┐
                  │
    [Entrada 2] ──┼──→ [SOMA] ──→ [AXÓN] ──→ [Salida]
                  │      ↑
    [Entrada 3] ──┘   umbral
                      (threshold)

================================================================================
LA NEURONA ARTIFICIAL (Perceptrón)
================================================================================

La neurona artificial imita este proceso:

1. ENTRADAS (x₁, x₂, ..., xₙ): Los datos que recibe
2. PESOS (w₁, w₂, ..., wₙ): Importancia de cada entrada
3. SUMA PONDERADA: Σ(xᵢ * wᵢ) + sesgo
4. FUNCIÓN DE ACTIVACIÓN: Decide si la neurona "se activa"
5. SALIDA: El resultado final

Matemáticamente:
    salida = f(Σ(xᵢ * wᵢ) + b)

    Donde:
    - xᵢ = entradas
    - wᵢ = pesos (weights)
    - b = sesgo (bias)
    - f = función de activación

================================================================================
"""

import math
import random

# ==============================================================================
# PASO 1: SUMA PONDERADA (Sin función de activación)
# ==============================================================================

print("=" * 60)
print("PASO 1: Entendiendo la suma ponderada")
print("=" * 60)

def suma_ponderada(entradas, pesos, sesgo=0):
    """
    Calcula la suma ponderada de las entradas.

    La suma ponderada es el "corazón" de la neurona. Combina todas
    las entradas multiplicadas por su peso correspondiente.

    Args:
        entradas: Lista de valores de entrada [x₁, x₂, ..., xₙ]
        pesos: Lista de pesos [w₁, w₂, ..., wₙ]
        sesgo: Valor de sesgo (bias) que se suma al final

    Returns:
        float: El resultado de Σ(xᵢ * wᵢ) + sesgo

    Ejemplo:
        entradas = [2, 3]
        pesos = [0.5, 0.5]
        sesgo = 1
        resultado = (2 * 0.5) + (3 * 0.5) + 1 = 1 + 1.5 + 1 = 3.5
    """
    # Verificamos que tenemos el mismo número de entradas y pesos
    if len(entradas) != len(pesos):
        raise ValueError("El número de entradas debe ser igual al de pesos")

    # Calculamos la suma ponderada
    suma = 0
    for i in range(len(entradas)):
        suma += entradas[i] * pesos[i]

    # Agregamos el sesgo
    suma += sesgo

    return suma


# Ejemplo práctico: Decidir si comprar un producto
print("""
Ejemplo: ¿Debería comprar este producto?

Factores (entradas):
- Precio bajo: 0.8 (de 0 a 1, donde 1 = muy bajo)
- Buenas reseñas: 0.9
- Lo necesito: 0.3

Importancia de cada factor (pesos):
- Precio: 0.4 (moderadamente importante)
- Reseñas: 0.3 (algo importante)
- Necesidad: 0.5 (bastante importante)

Sesgo: -0.5 (tendencia a no comprar impulsivamente)
""")

entradas_compra = [0.8, 0.9, 0.3]  # precio_bajo, buenas_reseñas, necesidad
pesos_compra = [0.4, 0.3, 0.5]     # importancia de cada factor
sesgo_compra = -0.5

resultado = suma_ponderada(entradas_compra, pesos_compra, sesgo_compra)
print(f"Suma ponderada: {resultado:.2f}")
print(f"Cálculo: (0.8×0.4) + (0.9×0.3) + (0.3×0.5) + (-0.5)")
print(f"       = 0.32 + 0.27 + 0.15 - 0.5 = {resultado:.2f}")


# ==============================================================================
# PASO 2: FUNCIONES DE ACTIVACIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("PASO 2: Funciones de Activación")
print("=" * 60)

print("""
¿Por qué necesitamos funciones de activación?

Sin ellas, una red neuronal sería solo una combinación lineal de entradas.
No podría aprender patrones complejos.

Las funciones de activación introducen NO LINEALIDAD, permitiendo que
la red aprenda relaciones complejas en los datos.

Funciones más comunes:
1. Escalón (Step): Salida binaria (0 o 1)
2. Sigmoide: Salida entre 0 y 1 (suave)
3. ReLU: max(0, x) - muy usada en deep learning
4. Tanh: Salida entre -1 y 1
""")


def activacion_escalon(x):
    """
    Función escalón (Step function / Heaviside).

    La más simple: si x > 0, retorna 1; si no, retorna 0.

    Uso: Clasificación binaria simple.
    Problema: No es diferenciable, no permite aprendizaje gradual.

         1 |     ________
           |    |
         0 |____|
           +----|----+--→ x
               0
    """
    if x > 0:
        return 1
    else:
        return 0


def activacion_sigmoide(x):
    """
    Función sigmoide (logística).

    Fórmula: σ(x) = 1 / (1 + e^(-x))

    Características:
    - Salida siempre entre 0 y 1
    - Suave y diferenciable (permite backpropagation)
    - σ(0) = 0.5
    - Valores muy negativos → cercano a 0
    - Valores muy positivos → cercano a 1

         1 |          _____
           |        /
       0.5 |-------*-------
           |      /
         0 |_____/
           +---------------→ x
                0

    Problema: "Vanishing gradient" en valores extremos.
    """
    return 1 / (1 + math.exp(-x))


def activacion_relu(x):
    """
    Función ReLU (Rectified Linear Unit).

    Fórmula: ReLU(x) = max(0, x)

    Características:
    - Si x < 0: salida = 0
    - Si x ≥ 0: salida = x
    - Computacionalmente eficiente
    - Muy usada en redes profundas

           y|    /
            |   /
            |  /
            | /
          0 |/________
            +---------------→ x
                0

    Problema: "Dying ReLU" - neuronas que siempre dan 0.
    """
    return max(0, x)


def activacion_tanh(x):
    """
    Función tangente hiperbólica.

    Fórmula: tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))

    Características:
    - Salida entre -1 y 1
    - Centrada en 0 (a diferencia de sigmoide)
    - Útil cuando queremos salidas negativas

         1 |          _____
           |        /
         0 |-------*-------
           |      /
        -1 |_____/
           +---------------→ x
                0
    """
    return math.tanh(x)


# Demostración de las funciones de activación
print("\nComparación de funciones de activación:")
print("-" * 50)
valores_prueba = [-2, -1, -0.5, 0, 0.5, 1, 2]

print(f"{'x':>6} | {'Escalón':>8} | {'Sigmoide':>8} | {'ReLU':>8} | {'Tanh':>8}")
print("-" * 50)

for x in valores_prueba:
    esc = activacion_escalon(x)
    sig = activacion_sigmoide(x)
    relu = activacion_relu(x)
    tanh = activacion_tanh(x)
    print(f"{x:>6.1f} | {esc:>8.2f} | {sig:>8.4f} | {relu:>8.2f} | {tanh:>8.4f}")


# ==============================================================================
# PASO 3: LA NEURONA COMPLETA
# ==============================================================================

print("\n" + "=" * 60)
print("PASO 3: Implementación de una Neurona Completa")
print("=" * 60)


class Neurona:
    """
    Implementación de una neurona artificial (Perceptrón).

    Una neurona:
    1. Recibe múltiples entradas
    2. Cada entrada tiene un peso asociado
    3. Calcula la suma ponderada + sesgo
    4. Aplica una función de activación
    5. Produce una salida

    Atributos:
        n_entradas: Número de entradas que acepta
        pesos: Lista de pesos para cada entrada
        sesgo: Valor de sesgo (bias)
        funcion_activacion: Nombre de la función a usar
    """

    def __init__(self, n_entradas, funcion_activacion="sigmoide"):
        """
        Inicializa la neurona.

        Args:
            n_entradas: Cuántas entradas tendrá la neurona
            funcion_activacion: "escalon", "sigmoide", "relu", o "tanh"
        """
        self.n_entradas = n_entradas
        self.funcion_activacion = funcion_activacion

        # Inicializamos pesos aleatorios entre -1 y 1
        # En la práctica, la inicialización de pesos es crucial para el aprendizaje
        self.pesos = [random.uniform(-1, 1) for _ in range(n_entradas)]

        # Sesgo también aleatorio
        self.sesgo = random.uniform(-1, 1)

        # Guardamos la última salida y suma (útil para backpropagation)
        self.ultima_suma = 0
        self.ultima_salida = 0

    def _aplicar_activacion(self, x):
        """
        Aplica la función de activación configurada.

        Args:
            x: Valor de entrada (suma ponderada)

        Returns:
            float: Valor después de la activación
        """
        if self.funcion_activacion == "escalon":
            return activacion_escalon(x)
        elif self.funcion_activacion == "sigmoide":
            return activacion_sigmoide(x)
        elif self.funcion_activacion == "relu":
            return activacion_relu(x)
        elif self.funcion_activacion == "tanh":
            return activacion_tanh(x)
        else:
            raise ValueError(f"Función desconocida: {self.funcion_activacion}")

    def calcular_salida(self, entradas):
        """
        Calcula la salida de la neurona dadas las entradas.

        Proceso:
        1. Suma ponderada: Σ(xᵢ * wᵢ) + sesgo
        2. Aplicar función de activación

        Args:
            entradas: Lista de valores de entrada

        Returns:
            float: La salida de la neurona
        """
        if len(entradas) != self.n_entradas:
            raise ValueError(
                f"Se esperaban {self.n_entradas} entradas, se recibieron {len(entradas)}"
            )

        # Paso 1: Suma ponderada
        self.ultima_suma = sum(
            entrada * peso for entrada, peso in zip(entradas, self.pesos)
        )
        self.ultima_suma += self.sesgo

        # Paso 2: Función de activación
        self.ultima_salida = self._aplicar_activacion(self.ultima_suma)

        return self.ultima_salida

    def __str__(self):
        """Representación en texto de la neurona."""
        return (
            f"Neurona(\n"
            f"  entradas: {self.n_entradas}\n"
            f"  pesos: {[round(p, 4) for p in self.pesos]}\n"
            f"  sesgo: {round(self.sesgo, 4)}\n"
            f"  activación: {self.funcion_activacion}\n"
            f")"
        )


# Ejemplo: Crear y usar una neurona
print("\nCreando una neurona con 3 entradas:")
mi_neurona = Neurona(n_entradas=3, funcion_activacion="sigmoide")
print(mi_neurona)

# Probamos con algunas entradas
entradas_prueba = [0.5, 0.8, 0.2]
salida = mi_neurona.calcular_salida(entradas_prueba)

print(f"\nEntradas: {entradas_prueba}")
print(f"Suma ponderada: {mi_neurona.ultima_suma:.4f}")
print(f"Salida (después de sigmoide): {salida:.4f}")


# ==============================================================================
# EJEMPLO PRÁCTICO: COMPUERTA LÓGICA AND
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO: Neurona que aprende la compuerta AND")
print("=" * 60)

print("""
La compuerta AND:
- Entrada: 2 valores binarios (0 o 1)
- Salida: 1 solo si AMBAS entradas son 1

Tabla de verdad:
  A | B | A AND B
  0 | 0 |    0
  0 | 1 |    0
  1 | 0 |    0
  1 | 1 |    1

Vamos a crear una neurona con pesos específicos que implementa AND.
""")

# Creamos una neurona con pesos "ajustados manualmente"
neurona_and = Neurona(n_entradas=2, funcion_activacion="escalon")

# Ajustamos los pesos manualmente para que funcione como AND
# La suma debe ser > 0 solo cuando ambas entradas son 1
neurona_and.pesos = [0.5, 0.5]  # Cada entrada aporta 0.5
neurona_and.sesgo = -0.7        # Umbral: necesitamos al menos 0.7 de suma

print(f"Neurona AND configurada:")
print(f"  Pesos: {neurona_and.pesos}")
print(f"  Sesgo: {neurona_and.sesgo}")
print()

# Probamos todas las combinaciones
print("Prueba de la neurona AND:")
print("-" * 30)
casos_and = [[0, 0], [0, 1], [1, 0], [1, 1]]

for caso in casos_and:
    salida = neurona_and.calcular_salida(caso)
    suma = neurona_and.ultima_suma
    print(f"  {caso[0]} AND {caso[1]} = {int(salida)}  (suma: {suma:.2f})")


# ==============================================================================
# LIMITACIONES DE UNA SOLA NEURONA
# ==============================================================================

print("\n" + "=" * 60)
print("LIMITACIÓN: El problema XOR")
print("=" * 60)

print("""
Una sola neurona NO puede resolver todos los problemas.

Ejemplo: La compuerta XOR (OR exclusivo)
  A | B | A XOR B
  0 | 0 |    0
  0 | 1 |    1
  1 | 0 |    1
  1 | 1 |    0

El problema: XOR no es linealmente separable.

Visualmente (1 = activar, 0 = no activar):

    B
    1 |  O───────X
      |  │       │
    0 |  X───────O
      +──────────── A
         0       1

    O = salida 0
    X = salida 1

No podemos dibujar UNA línea recta que separe los X de los O.
Una sola neurona solo puede aprender separaciones lineales.

SOLUCIÓN: Combinar múltiples neuronas → RED NEURONAL
""")

print("=" * 60)
print("PRÓXIMO PASO: 03_red_neuronal_desde_cero.py")
print("Aprenderemos a conectar neuronas para resolver problemas complejos.")
print("=" * 60)
