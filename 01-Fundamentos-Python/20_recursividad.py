"""
================================================================================
RECURSIVIDAD
================================================================================

La recursividad es una técnica donde una función se llama a sí misma
para resolver un problema dividiéndolo en subproblemas más pequeños.

ELEMENTOS CLAVE:
1. Caso base: condición que detiene la recursión
2. Caso recursivo: la función se llama a sí misma con datos más pequeños
3. Progreso hacia el caso base: cada llamada debe acercarse al caso base

CUÁNDO USAR RECURSIÓN:
- Problemas que se dividen naturalmente en subproblemas similares
- Estructuras de datos recursivas (árboles, grafos)
- Algoritmos de divide y vencerás
- Backtracking

================================================================================
"""

# ==============================================================================
# RECURSIÓN BÁSICA: FACTORIAL
# ==============================================================================

print("=" * 60)
print("RECURSIÓN BÁSICA: FACTORIAL")
print("=" * 60)

print("""
Factorial: n! = n × (n-1) × (n-2) × ... × 1
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- Caso base: 0! = 1! = 1
- Caso recursivo: n! = n × (n-1)!
""")

def factorial_iterativo(n):
    """Factorial con bucle."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def factorial(n):
    """Factorial recursivo."""
    # Caso base
    if n <= 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)

# Versión con visualización
def factorial_verbose(n, nivel=0):
    """Factorial que muestra las llamadas."""
    indent = "  " * nivel
    print(f"{indent}factorial({n})")

    if n <= 1:
        print(f"{indent}→ retorna 1 (caso base)")
        return 1

    resultado = n * factorial_verbose(n - 1, nivel + 1)
    print(f"{indent}→ retorna {n} × ... = {resultado}")
    return resultado


print("Comparación iterativo vs recursivo:")
for n in [0, 1, 5, 10]:
    print(f"  {n}! = {factorial(n)}")

print("\nVisualizando factorial(4):")
factorial_verbose(4)


# ==============================================================================
# FIBONACCI RECURSIVO
# ==============================================================================

print("\n" + "=" * 60)
print("FIBONACCI RECURSIVO")
print("=" * 60)

print("""
Secuencia de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
- F(0) = 0, F(1) = 1 (casos base)
- F(n) = F(n-1) + F(n-2) (caso recursivo)
""")

def fibonacci_simple(n):
    """Fibonacci recursivo simple (ineficiente)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_simple(n - 1) + fibonacci_simple(n - 2)

# Versión con memoización (eficiente)
def fibonacci_memo(n, memo=None):
    """Fibonacci con memoización."""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Usando decorador lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """Fibonacci con caché automático."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Secuencia de Fibonacci:")
print(f"  {[fibonacci(i) for i in range(15)]}")

# Comparar rendimiento
import time

print("\nComparación de rendimiento (n=30):")

inicio = time.perf_counter()
fibonacci_simple(30)
tiempo_simple = time.perf_counter() - inicio
print(f"  Simple: {tiempo_simple:.4f} segundos")

inicio = time.perf_counter()
fibonacci_memo(30)
tiempo_memo = time.perf_counter() - inicio
print(f"  Memoizado: {tiempo_memo:.6f} segundos")

print(f"  Speedup: {tiempo_simple / tiempo_memo:.0f}x más rápido")


# ==============================================================================
# SUMA RECURSIVA
# ==============================================================================

print("\n" + "=" * 60)
print("SUMA RECURSIVA DE LISTA")
print("=" * 60)

def suma_lista(lista):
    """Suma elementos de una lista recursivamente."""
    # Caso base: lista vacía
    if not lista:
        return 0
    # Caso recursivo: primer elemento + suma del resto
    return lista[0] + suma_lista(lista[1:])

def suma_lista_verbose(lista, nivel=0):
    """Suma con visualización."""
    indent = "  " * nivel
    print(f"{indent}suma({lista})")

    if not lista:
        print(f"{indent}→ 0 (vacía)")
        return 0

    resto = suma_lista_verbose(lista[1:], nivel + 1)
    resultado = lista[0] + resto
    print(f"{indent}→ {lista[0]} + {resto} = {resultado}")
    return resultado


numeros = [1, 2, 3, 4, 5]
print(f"Suma de {numeros}:")
print(f"  Resultado: {suma_lista(numeros)}")

print("\nVisualización:")
suma_lista_verbose([1, 2, 3])


# ==============================================================================
# RECURSIÓN CON STRINGS
# ==============================================================================

print("\n" + "=" * 60)
print("RECURSIÓN CON STRINGS")
print("=" * 60)

def invertir_string(s):
    """Invierte un string recursivamente."""
    # Caso base
    if len(s) <= 1:
        return s
    # Caso recursivo
    return invertir_string(s[1:]) + s[0]

def es_palindromo(s):
    """Verifica si es palíndromo recursivamente."""
    # Limpiar string
    s = s.lower().replace(" ", "")

    # Caso base
    if len(s) <= 1:
        return True
    # Caso recursivo
    if s[0] != s[-1]:
        return False
    return es_palindromo(s[1:-1])

def contar_caracter(s, char):
    """Cuenta ocurrencias de un carácter."""
    if not s:
        return 0
    return (1 if s[0] == char else 0) + contar_caracter(s[1:], char)


print("Invertir string:")
texto = "Python"
print(f"  '{texto}' → '{invertir_string(texto)}'")

print("\nPalíndromos:")
palabras = ["radar", "hola", "anita lava la tina", "python"]
for p in palabras:
    print(f"  '{p}': {'✓' if es_palindromo(p) else '✗'}")

print(f"\nContar 'a' en 'abracadabra': {contar_caracter('abracadabra', 'a')}")


# ==============================================================================
# POTENCIA RECURSIVA
# ==============================================================================

print("\n" + "=" * 60)
print("POTENCIA RECURSIVA")
print("=" * 60)

def potencia(base, exponente):
    """Calcula base^exponente recursivamente."""
    # Caso base
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potencia(base, -exponente)
    # Caso recursivo
    return base * potencia(base, exponente - 1)

# Versión optimizada (exponenciación rápida)
def potencia_rapida(base, exponente):
    """Potencia con exponenciación binaria - O(log n)."""
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potencia_rapida(base, -exponente)

    if exponente % 2 == 0:
        # base^n = (base^(n/2))^2
        mitad = potencia_rapida(base, exponente // 2)
        return mitad * mitad
    else:
        # base^n = base × base^(n-1)
        return base * potencia_rapida(base, exponente - 1)


print("Potencias:")
casos = [(2, 10), (3, 4), (5, 0), (2, -3)]
for base, exp in casos:
    print(f"  {base}^{exp} = {potencia(base, exp)}")

print(f"\n  2^100 (potencia rápida) = {potencia_rapida(2, 100)}")


# ==============================================================================
# MÁXIMO COMÚN DIVISOR (EUCLIDES)
# ==============================================================================

print("\n" + "=" * 60)
print("ALGORITMO DE EUCLIDES (MCD)")
print("=" * 60)

print("""
MCD(a, b):
- Si b = 0, retorna a (caso base)
- Si no, retorna MCD(b, a mod b)
""")

def mcd(a, b):
    """Máximo Común Divisor usando algoritmo de Euclides."""
    if b == 0:
        return a
    return mcd(b, a % b)

def mcd_verbose(a, b, nivel=0):
    """MCD con visualización."""
    indent = "  " * nivel
    print(f"{indent}mcd({a}, {b})")

    if b == 0:
        print(f"{indent}→ {a} (caso base)")
        return a

    return mcd_verbose(b, a % b, nivel + 1)


print("MCD(48, 18):")
mcd_verbose(48, 18)

print(f"\nOtros ejemplos:")
pares = [(100, 25), (17, 13), (144, 60)]
for a, b in pares:
    print(f"  MCD({a}, {b}) = {mcd(a, b)}")


# ==============================================================================
# BÚSQUEDA BINARIA RECURSIVA
# ==============================================================================

print("\n" + "=" * 60)
print("BÚSQUEDA BINARIA RECURSIVA")
print("=" * 60)

def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    """Búsqueda binaria recursiva en lista ordenada."""
    if fin is None:
        fin = len(lista) - 1

    # Caso base: no encontrado
    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2

    # Caso base: encontrado
    if lista[medio] == objetivo:
        return medio

    # Caso recursivo
    if objetivo < lista[medio]:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)


numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Lista: {numeros}")

for objetivo in [7, 1, 19, 8]:
    indice = busqueda_binaria(numeros, objetivo)
    if indice != -1:
        print(f"  {objetivo} encontrado en índice {indice}")
    else:
        print(f"  {objetivo} no encontrado")


# ==============================================================================
# TORRES DE HANOI
# ==============================================================================

print("\n" + "=" * 60)
print("TORRES DE HANOI")
print("=" * 60)

print("""
Problema clásico de recursión:
- n discos en torre A
- Mover todos a torre C
- Solo mover un disco a la vez
- Disco grande no puede ir sobre disco pequeño
""")

def hanoi(n, origen, destino, auxiliar, movimientos=None):
    """Resuelve Torres de Hanoi."""
    if movimientos is None:
        movimientos = []

    if n == 1:
        movimientos.append(f"Mover disco 1 de {origen} a {destino}")
        return movimientos

    # Mover n-1 discos de origen a auxiliar
    hanoi(n - 1, origen, auxiliar, destino, movimientos)

    # Mover disco n de origen a destino
    movimientos.append(f"Mover disco {n} de {origen} a {destino}")

    # Mover n-1 discos de auxiliar a destino
    hanoi(n - 1, auxiliar, destino, origen, movimientos)

    return movimientos


print("Torres de Hanoi con 3 discos:")
movimientos = hanoi(3, 'A', 'C', 'B')
for i, mov in enumerate(movimientos, 1):
    print(f"  {i}. {mov}")

print(f"\nTotal movimientos para n discos: 2^n - 1")
for n in [1, 2, 3, 4, 5]:
    print(f"  n={n}: {2**n - 1} movimientos")


# ==============================================================================
# RECORRIDO DE ESTRUCTURAS RECURSIVAS
# ==============================================================================

print("\n" + "=" * 60)
print("RECORRIDO DE ESTRUCTURAS RECURSIVAS")
print("=" * 60)

# Árbol binario
class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


def inorden(nodo):
    """Recorrido inorden: izquierda, raíz, derecha."""
    if nodo is None:
        return []
    return inorden(nodo.izquierda) + [nodo.valor] + inorden(nodo.derecha)

def preorden(nodo):
    """Recorrido preorden: raíz, izquierda, derecha."""
    if nodo is None:
        return []
    return [nodo.valor] + preorden(nodo.izquierda) + preorden(nodo.derecha)

def postorden(nodo):
    """Recorrido postorden: izquierda, derecha, raíz."""
    if nodo is None:
        return []
    return postorden(nodo.izquierda) + postorden(nodo.derecha) + [nodo.valor]

def altura(nodo):
    """Calcula la altura del árbol."""
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izquierda), altura(nodo.derecha))

def buscar_arbol(nodo, valor):
    """Busca un valor en el árbol binario de búsqueda."""
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    if valor < nodo.valor:
        return buscar_arbol(nodo.izquierda, valor)
    return buscar_arbol(nodo.derecha, valor)


# Crear árbol:
#        5
#       / \
#      3   7
#     / \ / \
#    1  4 6  9

arbol = Nodo(5,
    Nodo(3, Nodo(1), Nodo(4)),
    Nodo(7, Nodo(6), Nodo(9))
)

print("Árbol binario de búsqueda:")
print(f"  Inorden:   {inorden(arbol)}")
print(f"  Preorden:  {preorden(arbol)}")
print(f"  Postorden: {postorden(arbol)}")
print(f"  Altura:    {altura(arbol)}")
print(f"  ¿Contiene 6?: {buscar_arbol(arbol, 6)}")
print(f"  ¿Contiene 8?: {buscar_arbol(arbol, 8)}")


# ==============================================================================
# BACKTRACKING: PERMUTACIONES
# ==============================================================================

print("\n" + "=" * 60)
print("BACKTRACKING: PERMUTACIONES")
print("=" * 60)

def permutaciones(elementos):
    """Genera todas las permutaciones de una lista."""
    # Caso base
    if len(elementos) <= 1:
        return [elementos]

    resultado = []
    for i, elem in enumerate(elementos):
        # Elementos restantes (sin el actual)
        resto = elementos[:i] + elementos[i+1:]
        # Recursión: permutaciones del resto
        for perm in permutaciones(resto):
            resultado.append([elem] + perm)

    return resultado


print("Permutaciones de [1, 2, 3]:")
for p in permutaciones([1, 2, 3]):
    print(f"  {p}")


# ==============================================================================
# BACKTRACKING: N-REINAS
# ==============================================================================

print("\n" + "=" * 60)
print("BACKTRACKING: N-REINAS")
print("=" * 60)

print("""
Colocar N reinas en un tablero NxN sin que se ataquen.
""")

def es_seguro(tablero, fila, columna):
    """Verifica si es seguro colocar reina en (fila, columna)."""
    # Verificar columna
    for i in range(fila):
        if tablero[i] == columna:
            return False

    # Verificar diagonal izquierda
    for i, j in zip(range(fila-1, -1, -1), range(columna-1, -1, -1)):
        if tablero[i] == j:
            return False

    # Verificar diagonal derecha
    for i, j in zip(range(fila-1, -1, -1), range(columna+1, len(tablero))):
        if tablero[i] == j:
            return False

    return True

def resolver_n_reinas(n, fila=0, tablero=None, soluciones=None):
    """Encuentra todas las soluciones al problema de N-reinas."""
    if tablero is None:
        tablero = [-1] * n
    if soluciones is None:
        soluciones = []

    # Caso base: todas las reinas colocadas
    if fila == n:
        soluciones.append(tablero.copy())
        return soluciones

    # Intentar cada columna
    for columna in range(n):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            resolver_n_reinas(n, fila + 1, tablero, soluciones)
            tablero[fila] = -1  # Backtrack

    return soluciones

def imprimir_tablero(solucion):
    """Imprime un tablero con reinas."""
    n = len(solucion)
    for fila in range(n):
        linea = ""
        for col in range(n):
            if solucion[fila] == col:
                linea += "♛ "
            else:
                linea += "· "
        print(f"    {linea}")


n = 4
soluciones = resolver_n_reinas(n)
print(f"Soluciones para {n}-reinas: {len(soluciones)}")

print("\nPrimera solución:")
imprimir_tablero(soluciones[0])

print(f"\nNúmero de soluciones para diferentes N:")
for n in range(1, 9):
    sols = resolver_n_reinas(n)
    print(f"  {n}-reinas: {len(sols)} soluciones")


# ==============================================================================
# RECURSIÓN VS ITERACIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("RECURSIÓN VS ITERACIÓN")
print("=" * 60)

print("""
RECURSIÓN:
+ Código más elegante y legible para problemas recursivos
+ Natural para estructuras de datos recursivas
- Overhead de llamadas a funciones
- Riesgo de stack overflow

ITERACIÓN:
+ Generalmente más eficiente
+ No tiene límite de stack
- Puede ser menos intuitiva para problemas recursivos

REGLA GENERAL:
- Usa recursión cuando el problema es naturalmente recursivo
- Usa iteración cuando el rendimiento es crítico
- Considera memoización para optimizar recursión
""")

import sys
print(f"\nLímite de recursión en Python: {sys.getrecursionlimit()}")
# sys.setrecursionlimit(10000)  # Se puede aumentar si es necesario


# ==============================================================================
# RECURSIÓN DE COLA (TAIL RECURSION)
# ==============================================================================

print("\n" + "=" * 60)
print("RECURSIÓN DE COLA")
print("=" * 60)

print("""
La recursión de cola es cuando la llamada recursiva es la última
operación. Algunos lenguajes la optimizan, pero Python no.
""")

# Factorial normal (no de cola)
def factorial_normal(n):
    if n <= 1:
        return 1
    return n * factorial_normal(n - 1)  # Multiplicación DESPUÉS de la llamada

# Factorial con recursión de cola
def factorial_cola(n, acumulador=1):
    if n <= 1:
        return acumulador
    return factorial_cola(n - 1, n * acumulador)  # Llamada es última operación


print("Factorial normal vs cola:")
print(f"  factorial_normal(5) = {factorial_normal(5)}")
print(f"  factorial_cola(5) = {factorial_cola(5)}")


# Convertir recursión de cola a iteración
def factorial_iterativo_desde_cola(n):
    """Conversión manual de recursión de cola a iteración."""
    acumulador = 1
    while n > 1:
        acumulador *= n
        n -= 1
    return acumulador

print(f"  factorial_iterativo_desde_cola(5) = {factorial_iterativo_desde_cola(5)}")


# ==============================================================================
# EJEMPLO COMPLETO: EXPLORADOR DE DIRECTORIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO COMPLETO: EXPLORADOR DE DIRECTORIOS")
print("=" * 60)

# Simulamos estructura de directorios
sistema_archivos = {
    'tipo': 'directorio',
    'nombre': 'raiz',
    'contenido': [
        {
            'tipo': 'directorio',
            'nombre': 'documentos',
            'contenido': [
                {'tipo': 'archivo', 'nombre': 'informe.pdf', 'tamaño': 1024},
                {'tipo': 'archivo', 'nombre': 'notas.txt', 'tamaño': 256},
                {
                    'tipo': 'directorio',
                    'nombre': 'proyectos',
                    'contenido': [
                        {'tipo': 'archivo', 'nombre': 'codigo.py', 'tamaño': 512}
                    ]
                }
            ]
        },
        {
            'tipo': 'directorio',
            'nombre': 'imagenes',
            'contenido': [
                {'tipo': 'archivo', 'nombre': 'foto1.jpg', 'tamaño': 2048},
                {'tipo': 'archivo', 'nombre': 'foto2.png', 'tamaño': 1536}
            ]
        },
        {'tipo': 'archivo', 'nombre': 'readme.md', 'tamaño': 128}
    ]
}

def listar_recursivo(nodo, nivel=0):
    """Lista todos los archivos y directorios recursivamente."""
    indent = "  " * nivel
    prefijo = "📁" if nodo['tipo'] == 'directorio' else "📄"
    print(f"{indent}{prefijo} {nodo['nombre']}")

    if nodo['tipo'] == 'directorio':
        for item in nodo.get('contenido', []):
            listar_recursivo(item, nivel + 1)

def calcular_tamaño(nodo):
    """Calcula el tamaño total recursivamente."""
    if nodo['tipo'] == 'archivo':
        return nodo['tamaño']

    total = 0
    for item in nodo.get('contenido', []):
        total += calcular_tamaño(item)
    return total

def buscar_archivos(nodo, extension, ruta=""):
    """Busca archivos por extensión."""
    resultados = []
    ruta_actual = f"{ruta}/{nodo['nombre']}"

    if nodo['tipo'] == 'archivo':
        if nodo['nombre'].endswith(extension):
            resultados.append(ruta_actual)
    else:
        for item in nodo.get('contenido', []):
            resultados.extend(buscar_archivos(item, extension, ruta_actual))

    return resultados

def contar_elementos(nodo):
    """Cuenta archivos y directorios."""
    if nodo['tipo'] == 'archivo':
        return {'archivos': 1, 'directorios': 0}

    conteo = {'archivos': 0, 'directorios': 1}
    for item in nodo.get('contenido', []):
        sub_conteo = contar_elementos(item)
        conteo['archivos'] += sub_conteo['archivos']
        conteo['directorios'] += sub_conteo['directorios']

    return conteo


print("Estructura de directorios:")
listar_recursivo(sistema_archivos)

print(f"\nTamaño total: {calcular_tamaño(sistema_archivos)} bytes")

print(f"\nArchivos .py: {buscar_archivos(sistema_archivos, '.py')}")
print(f"Archivos .txt: {buscar_archivos(sistema_archivos, '.txt')}")

conteo = contar_elementos(sistema_archivos)
print(f"\nTotal: {conteo['archivos']} archivos, {conteo['directorios']} directorios")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Implementa una función recursiva que calcule la suma de
   los dígitos de un número (ej: 123 → 1+2+3 = 6)

2. Escribe una función recursiva que determine si una lista
   está ordenada de menor a mayor

3. Implementa el algoritmo de ordenamiento Merge Sort
   recursivamente

4. Crea una función que genere todas las combinaciones
   de k elementos de una lista

5. Implementa una función que resuelva el problema del
   subconjunto suma (dado un conjunto de números, determinar
   si existe un subconjunto que sume un valor objetivo)

6. Escribe un generador de laberintos y un solucionador
   recursivo usando backtracking

7. Implementa un evaluador de expresiones matemáticas
   con paréntesis de forma recursiva

8. Crea una función que imprima el triángulo de Pascal
   usando recursión
""")

print("\n" + "=" * 60)
print("¡FELICIDADES! Has completado los Fundamentos de Python")
print("=" * 60)

print("""
Has aprendido:
01. Introducción a Python
02. Variables y tipos de datos
03. Operadores
04. Strings
05. Estructuras de control
06. Bucles
07. Listas
08. Tuplas y Sets
09. Diccionarios
10. Funciones básicas
11. Funciones avanzadas
12. Comprehensions
13. Manejo de errores
14. Archivos
15. Módulos y paquetes
16. POO básico
17. POO avanzado
18. Decoradores
19. Generadores e iteradores
20. Recursividad

Continúa con las carpetas avanzadas:
- 02-Data-Science-AI/
- 03-Automatizacion-Scripting/
- 04-Ciberseguridad/
- 05-Finanzas-Cuantitativas/
""")
