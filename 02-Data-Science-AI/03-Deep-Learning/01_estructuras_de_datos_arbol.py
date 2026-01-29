"""
================================================================================
ESTRUCTURAS DE DATOS: ÁRBOLES
================================================================================

¿POR QUÉ EMPEZAMOS CON ÁRBOLES?
-------------------------------
Antes de entender redes neuronales, necesitamos comprender estructuras de datos
fundamentales. Los árboles son esenciales porque:

1. Las redes neuronales organizan datos en capas (como niveles de un árbol)
2. Los algoritmos de decisión (Random Forest, XGBoost) usan árboles directamente
3. El backpropagation recorre la red como se recorre un árbol
4. Entender recursión en árboles ayuda a entender propagación en redes

================================================================================
¿QUÉ ES UN ÁRBOL?
================================================================================

Un árbol es una estructura de datos jerárquica compuesta por NODOS conectados.

Terminología básica:
- NODO: Cada elemento del árbol que contiene datos
- RAÍZ: El nodo superior (punto de entrada)
- HIJOS: Nodos que descienden de otro nodo
- PADRE: Nodo del cual descienden otros
- HOJAS: Nodos sin hijos (nodos finales)
- NIVEL/PROFUNDIDAD: Distancia desde la raíz

Representación visual de un árbol:

            [RAÍZ]           <- Nivel 0
           /      \
        [A]        [B]       <- Nivel 1
       /   \         \
     [C]   [D]       [E]     <- Nivel 2 (C, D, E son HOJAS)

================================================================================
"""

# ==============================================================================
# IMPLEMENTACIÓN BÁSICA: NODO
# ==============================================================================

class Nodo:
    """
    Clase que representa un nodo en un árbol.

    Un nodo tiene:
    - Un valor/contenido (los datos que almacena)
    - Una lista de hijos (referencias a otros nodos)

    Esta es la unidad fundamental de un árbol.
    """

    def __init__(self, valor):
        """
        Constructor del nodo.

        Args:
            valor: El dato que almacenará este nodo (puede ser cualquier tipo)
        """
        self.valor = valor      # El dato que guarda el nodo
        self.hijos = []         # Lista vacía de hijos (inicialmente no tiene)

    def agregar_hijo(self, nodo_hijo):
        """
        Añade un nodo hijo a este nodo.

        Args:
            nodo_hijo: Otro objeto Nodo que será hijo de este
        """
        self.hijos.append(nodo_hijo)

    def es_hoja(self):
        """
        Verifica si este nodo es una hoja (no tiene hijos).

        Returns:
            bool: True si no tiene hijos, False si tiene al menos uno
        """
        return len(self.hijos) == 0

    def __str__(self):
        """Representación en texto del nodo."""
        return f"Nodo({self.valor})"


# ==============================================================================
# IMPLEMENTACIÓN BÁSICA: ÁRBOL
# ==============================================================================

class Arbol:
    """
    Clase que representa un árbol completo.

    Un árbol se define por su nodo raíz. Desde la raíz podemos
    acceder a todos los demás nodos siguiendo las conexiones padre-hijo.
    """

    def __init__(self, valor_raiz):
        """
        Constructor del árbol.

        Args:
            valor_raiz: El valor que tendrá el nodo raíz
        """
        self.raiz = Nodo(valor_raiz)

    def obtener_raiz(self):
        """Retorna el nodo raíz del árbol."""
        return self.raiz


# ==============================================================================
# EJEMPLO PRÁCTICO 1: ÁRBOL SIMPLE
# ==============================================================================

print("=" * 60)
print("EJEMPLO 1: Creación de un árbol simple")
print("=" * 60)

# Creamos un árbol con raíz "CEO"
empresa = Arbol("CEO")

# Creamos nodos para los directores
director_tech = Nodo("Director de Tecnología")
director_ventas = Nodo("Director de Ventas")
director_rrhh = Nodo("Director de RRHH")

# Los agregamos como hijos del CEO (raíz)
empresa.raiz.agregar_hijo(director_tech)
empresa.raiz.agregar_hijo(director_ventas)
empresa.raiz.agregar_hijo(director_rrhh)

# Agregamos empleados bajo el Director de Tecnología
programador1 = Nodo("Programador Senior")
programador2 = Nodo("Programador Junior")
director_tech.agregar_hijo(programador1)
director_tech.agregar_hijo(programador2)

# Agregamos empleados bajo el Director de Ventas
vendedor = Nodo("Vendedor")
director_ventas.agregar_hijo(vendedor)

print(f"Raíz del árbol: {empresa.raiz}")
print(f"Hijos de la raíz: {[str(h) for h in empresa.raiz.hijos]}")
print(f"¿El CEO es hoja? {empresa.raiz.es_hoja()}")
print(f"¿El vendedor es hoja? {vendedor.es_hoja()}")


# ==============================================================================
# RECORRIDO DE ÁRBOLES (Fundamental para entender backpropagation)
# ==============================================================================

print("\n" + "=" * 60)
print("RECORRIDOS DE ÁRBOLES")
print("=" * 60)

def recorrido_profundidad(nodo, nivel=0):
    """
    Recorre el árbol en profundidad (DFS - Depth First Search).

    Este tipo de recorrido es similar a cómo el backpropagation
    propaga el error desde las capas de salida hacia las de entrada.

    Args:
        nodo: El nodo actual a visitar
        nivel: La profundidad actual (para visualización)
    """
    # Indentación visual según el nivel
    indentacion = "  " * nivel
    print(f"{indentacion}├── {nodo.valor}")

    # Recursivamente visitamos cada hijo
    for hijo in nodo.hijos:
        recorrido_profundidad(hijo, nivel + 1)


print("\nEstructura jerárquica de la empresa:")
recorrido_profundidad(empresa.raiz)


def recorrido_amplitud(nodo_raiz):
    """
    Recorre el árbol en amplitud (BFS - Breadth First Search).

    Visita todos los nodos de un nivel antes de pasar al siguiente.
    Similar a cómo los datos fluyen capa por capa en una red neuronal.

    Args:
        nodo_raiz: El nodo desde donde empezar el recorrido
    """
    # Usamos una cola (lista) para ir guardando los nodos a visitar
    cola = [nodo_raiz]
    nivel_actual = 0

    while cola:
        # Guardamos cuántos nodos hay en este nivel
        nodos_en_nivel = len(cola)
        print(f"\nNivel {nivel_actual}:")

        # Procesamos todos los nodos del nivel actual
        for _ in range(nodos_en_nivel):
            nodo_actual = cola.pop(0)  # Sacamos el primer elemento
            print(f"  - {nodo_actual.valor}")

            # Agregamos sus hijos a la cola para el siguiente nivel
            for hijo in nodo_actual.hijos:
                cola.append(hijo)

        nivel_actual += 1


print("\n" + "-" * 40)
print("Recorrido por niveles (amplitud):")
recorrido_amplitud(empresa.raiz)


# ==============================================================================
# ÁRBOL BINARIO (Base para muchos algoritmos de ML)
# ==============================================================================

print("\n" + "=" * 60)
print("ÁRBOL BINARIO")
print("=" * 60)

class NodoBinario:
    """
    Nodo para árbol binario (máximo 2 hijos: izquierdo y derecho).

    Los árboles binarios son la base de:
    - Árboles de decisión (Decision Trees)
    - Random Forest (conjunto de árboles)
    - Gradient Boosting (XGBoost, LightGBM)
    """

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None   # Hijo izquierdo
        self.derecho = None     # Hijo derecho

    def insertar_izquierdo(self, valor):
        """Crea un hijo izquierdo con el valor dado."""
        self.izquierdo = NodoBinario(valor)
        return self.izquierdo

    def insertar_derecho(self, valor):
        """Crea un hijo derecho con el valor dado."""
        self.derecho = NodoBinario(valor)
        return self.derecho


# Ejemplo: Árbol de decisión simple para clasificar si hacer ejercicio
print("""
Árbol de decisión: ¿Debo hacer ejercicio hoy?

                    [¿Está lloviendo?]
                    /                 \\
                  Sí                   No
                  /                     \\
        [Quedarse en casa]    [¿Tengo energía?]
                              /              \\
                            No               Sí
                            /                 \\
                    [Descansar]          [¡Ejercicio!]
""")

# Implementamos este árbol de decisión
raiz_decision = NodoBinario("¿Está lloviendo?")
raiz_decision.insertar_izquierdo("Quedarse en casa")
nodo_energia = raiz_decision.insertar_derecho("¿Tengo energía?")
nodo_energia.insertar_izquierdo("Descansar")
nodo_energia.insertar_derecho("¡Ejercicio!")


def tomar_decision(nodo, respuestas):
    """
    Recorre el árbol de decisión según las respuestas dadas.

    Args:
        nodo: Nodo actual del árbol
        respuestas: Lista de respuestas (True para derecha, False para izquierda)

    Returns:
        str: La decisión final
    """
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo.valor  # Es una hoja, retornamos la decisión

    if not respuestas:
        return nodo.valor

    respuesta = respuestas.pop(0)
    if respuesta:  # True = ir a la derecha
        return tomar_decision(nodo.derecho, respuestas)
    else:  # False = ir a la izquierda
        return tomar_decision(nodo.izquierdo, respuestas)


# Probamos el árbol de decisión
print("Escenario 1: Está lloviendo (False = izquierda)")
print(f"Decisión: {tomar_decision(raiz_decision, [False])}")

# Recreamos el árbol para otra prueba
raiz_decision = NodoBinario("¿Está lloviendo?")
raiz_decision.insertar_izquierdo("Quedarse en casa")
nodo_energia = raiz_decision.insertar_derecho("¿Tengo energía?")
nodo_energia.insertar_izquierdo("Descansar")
nodo_energia.insertar_derecho("¡Ejercicio!")

print("\nEscenario 2: No llueve y tengo energía (True, True)")
print(f"Decisión: {tomar_decision(raiz_decision, [True, True])}")


# ==============================================================================
# CONEXIÓN CON REDES NEURONALES
# ==============================================================================

print("\n" + "=" * 60)
print("CONEXIÓN CON REDES NEURONALES")
print("=" * 60)

print("""
¿Por qué los árboles son relevantes para Deep Learning?

1. ESTRUCTURA EN CAPAS:
   - Un árbol tiene niveles (profundidad)
   - Una red neuronal tiene capas (layers)
   - Los datos fluyen de un nivel/capa al siguiente

2. PROPAGACIÓN:
   - En árboles: recorremos de raíz a hojas (o viceversa)
   - En redes: forward propagation (entrada → salida)
                backpropagation (salida → entrada)

3. DECISIONES:
   - Árboles de decisión: cada nodo toma una decisión binaria
   - Neuronas: cada una "decide" cuánto activarse

4. ALGORITMOS BASADOS EN ÁRBOLES:
   - Random Forest: muchos árboles votando
   - XGBoost: árboles que aprenden de errores anteriores
   - Estos compiten con redes neuronales en datos tabulares

PRÓXIMO PASO: Aprenderemos sobre la neurona, que es como un
"nodo inteligente" que puede aprender de los datos.
""")

print("\n" + "=" * 60)
print("Archivo completado. Continúa con: 02_que_es_una_neurona.py")
print("=" * 60)
