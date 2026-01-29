"""
================================================================================
GENERADORES E ITERADORES
================================================================================

Los iteradores y generadores permiten procesar secuencias de datos
de forma eficiente en memoria, generando valores bajo demanda.

ITERADOR: Objeto que implementa __iter__() y __next__()
GENERADOR: Función que usa 'yield' para producir valores

VENTAJAS:
- Eficiencia en memoria (no carga todo en RAM)
- Evaluación perezosa (lazy evaluation)
- Procesamiento de datos infinitos o muy grandes
- Pipelines de procesamiento de datos

================================================================================
"""

# ==============================================================================
# PROTOCOLO DE ITERACIÓN
# ==============================================================================

print("=" * 60)
print("PROTOCOLO DE ITERACIÓN")
print("=" * 60)

print("""
Un objeto es iterable si implementa:
- __iter__(): retorna un iterador
- __next__(): retorna el siguiente valor (o StopIteration)
""")

# Iterar sobre una lista (forma implícita)
print("--- Iteración implícita (for) ---")
numeros = [1, 2, 3]
for n in numeros:
    print(f"  {n}")

# Lo mismo de forma explícita
print("\n--- Iteración explícita ---")
iterador = iter(numeros)  # Llama a __iter__
print(f"  {next(iterador)}")  # Llama a __next__
print(f"  {next(iterador)}")
print(f"  {next(iterador)}")
# next(iterador)  # StopIteration

# Ver la diferencia entre iterable e iterador
print("\n--- Iterable vs Iterador ---")
print(f"lista es iterable: {hasattr(numeros, '__iter__')}")
print(f"lista es iterador: {hasattr(numeros, '__next__')}")
iterador = iter(numeros)
print(f"iter(lista) es iterador: {hasattr(iterador, '__next__')}")


# ==============================================================================
# CREAR UN ITERADOR PERSONALIZADO
# ==============================================================================

print("\n" + "=" * 60)
print("CREAR UN ITERADOR PERSONALIZADO")
print("=" * 60)

class Contador:
    """Iterador que cuenta desde inicio hasta fin."""

    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual >= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor


print("Contador(1, 5):")
for n in Contador(1, 5):
    print(f"  {n}")


class RangoInverso:
    """Iterador que cuenta hacia atrás."""

    def __init__(self, inicio, fin=0, paso=-1):
        self.actual = inicio
        self.fin = fin
        self.paso = paso

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual <= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += self.paso
        return valor


print("\nRangoInverso(5):")
for n in RangoInverso(5):
    print(f"  {n}")


# ==============================================================================
# GENERADORES CON YIELD
# ==============================================================================

print("\n" + "=" * 60)
print("GENERADORES CON YIELD")
print("=" * 60)

print("""
Un generador es una función que usa 'yield' en lugar de 'return'.
Cada vez que se llama a next(), ejecuta hasta el siguiente yield.
""")

def generador_simple():
    """Generador más simple."""
    print("  Antes del primer yield")
    yield 1
    print("  Antes del segundo yield")
    yield 2
    print("  Antes del tercer yield")
    yield 3
    print("  Función terminada")

print("Ejecutando generador paso a paso:")
gen = generador_simple()
print(f"next() = {next(gen)}")
print(f"next() = {next(gen)}")
print(f"next() = {next(gen)}")
# next(gen)  # StopIteration


# Generador que reemplaza al iterador Contador
def contador(inicio, fin):
    """Generador que cuenta de inicio a fin."""
    actual = inicio
    while actual < fin:
        yield actual
        actual += 1

print("\ncontador(1, 5):")
for n in contador(1, 5):
    print(f"  {n}")


# Generador infinito
def numeros_naturales(inicio=1):
    """Genera números naturales infinitamente."""
    n = inicio
    while True:
        yield n
        n += 1

print("\nPrimeros 5 números naturales:")
gen = numeros_naturales()
for _ in range(5):
    print(f"  {next(gen)}")


# ==============================================================================
# EXPRESIONES GENERADORAS
# ==============================================================================

print("\n" + "=" * 60)
print("EXPRESIONES GENERADORAS")
print("=" * 60)

print("""
Son como list comprehensions pero con paréntesis.
Crean un generador en lugar de una lista completa.
""")

import sys

# Comparar memoria
lista = [x**2 for x in range(1000)]
generador = (x**2 for x in range(1000))

print(f"Tamaño lista: {sys.getsizeof(lista)} bytes")
print(f"Tamaño generador: {sys.getsizeof(generador)} bytes")

# Usar expresión generadora
print("\nCuadrados de 1 a 5:")
cuadrados = (x**2 for x in range(1, 6))
for c in cuadrados:
    print(f"  {c}")

# En funciones que aceptan iterables
print(f"\nSuma de cuadrados 1-100: {sum(x**2 for x in range(1, 101))}")
print(f"Máximo: {max(x**2 for x in range(1, 11))}")

# Condicionales en expresiones generadoras
pares_cuadrados = (x**2 for x in range(20) if x % 2 == 0)
print(f"Cuadrados de pares: {list(pares_cuadrados)}")


# ==============================================================================
# YIELD FROM
# ==============================================================================

print("\n" + "=" * 60)
print("YIELD FROM")
print("=" * 60)

print("""
'yield from' delega la generación a otro iterable o generador.
Simplifica la composición de generadores.
""")

# Sin yield from
def aplanar_sin_yield_from(lista_anidada):
    for sublista in lista_anidada:
        for elemento in sublista:
            yield elemento

# Con yield from
def aplanar(lista_anidada):
    for sublista in lista_anidada:
        yield from sublista

anidada = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"Lista anidada: {anidada}")
print(f"Aplanada: {list(aplanar(anidada))}")


# Combinar generadores
def generador_a():
    yield 'A1'
    yield 'A2'

def generador_b():
    yield 'B1'
    yield 'B2'

def generador_combinado():
    yield from generador_a()
    yield from generador_b()

print(f"\nGeneradores combinados: {list(generador_combinado())}")


# yield from para recorrer árboles
def recorrer_arbol(nodo):
    """Recorre un árbol (diccionario anidado) en profundidad."""
    if isinstance(nodo, dict):
        for clave, valor in nodo.items():
            yield clave
            yield from recorrer_arbol(valor)
    elif isinstance(nodo, list):
        for elemento in nodo:
            yield from recorrer_arbol(elemento)
    else:
        yield nodo

arbol = {
    'raiz': {
        'izquierda': {
            'hoja1': 1,
            'hoja2': 2
        },
        'derecha': {
            'hoja3': 3
        }
    }
}

print(f"\nRecorrido del árbol: {list(recorrer_arbol(arbol))}")


# ==============================================================================
# MÉTODOS DE GENERADORES
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS DE GENERADORES")
print("=" * 60)

print("""
Los generadores tienen métodos adicionales:
- send(): envía un valor al generador
- throw(): lanza una excepción en el generador
- close(): cierra el generador
""")

def generador_con_send():
    """Generador que recibe valores con send()."""
    print("  Generador iniciado")
    while True:
        valor = yield
        if valor is None:
            break
        print(f"  Recibido: {valor}")
    print("  Generador terminado")

gen = generador_con_send()
next(gen)  # Iniciar el generador (avanza hasta primer yield)
gen.send("Hola")
gen.send("Mundo")
gen.send(None)  # Termina el generador


# Generador bidireccional más útil
def acumulador():
    """Acumula valores enviados."""
    total = 0
    while True:
        valor = yield total
        if valor is None:
            break
        total += valor

print("\nAcumulador:")
acc = acumulador()
print(f"  Inicial: {next(acc)}")
print(f"  +10: {acc.send(10)}")
print(f"  +5: {acc.send(5)}")
print(f"  +3: {acc.send(3)}")


# ==============================================================================
# ITERTOOLS - HERRAMIENTAS PARA ITERADORES
# ==============================================================================

print("\n" + "=" * 60)
print("ITERTOOLS - HERRAMIENTAS PARA ITERADORES")
print("=" * 60)

import itertools

# --- Iteradores infinitos ---
print("--- Iteradores infinitos ---")

# count: contador infinito
from itertools import count, cycle, repeat, islice

contador = count(start=10, step=2)
print(f"count(10, 2): {list(islice(contador, 5))}")

# cycle: ciclo infinito
colores = cycle(['rojo', 'verde', 'azul'])
print(f"cycle(colores): {[next(colores) for _ in range(7)]}")

# repeat: repetir valor
print(f"repeat('X', 4): {list(repeat('X', 4))}")


# --- Iteradores que terminan ---
print("\n--- Iteradores que terminan ---")

from itertools import chain, compress, dropwhile, takewhile, filterfalse

# chain: concatenar iterables
print(f"chain([1,2], [3,4]): {list(chain([1, 2], [3, 4]))}")

# compress: filtrar con máscara
datos = ['a', 'b', 'c', 'd']
mascara = [1, 0, 1, 0]
print(f"compress({datos}, {mascara}): {list(compress(datos, mascara))}")

# takewhile / dropwhile
numeros = [1, 3, 5, 8, 2, 4, 6]
print(f"takewhile(<5, {numeros}): {list(takewhile(lambda x: x < 5, numeros))}")
print(f"dropwhile(<5, {numeros}): {list(dropwhile(lambda x: x < 5, numeros))}")


# --- Combinatorias ---
print("\n--- Combinatorias ---")

from itertools import permutations, combinations, combinations_with_replacement, product

letras = 'ABC'
print(f"permutations('ABC', 2): {list(permutations(letras, 2))}")
print(f"combinations('ABC', 2): {list(combinations(letras, 2))}")
print(f"product('AB', '12'): {list(product('AB', '12'))}")


# --- Agrupación ---
print("\n--- Agrupación ---")

from itertools import groupby

# Los datos deben estar ordenados por la clave
datos = [
    ('Ana', 'A'), ('Luis', 'B'), ('María', 'A'),
    ('Carlos', 'A'), ('Elena', 'B')
]
datos_ordenados = sorted(datos, key=lambda x: x[1])

print("groupby por grupo:")
for grupo, elementos in groupby(datos_ordenados, key=lambda x: x[1]):
    print(f"  Grupo {grupo}: {[e[0] for e in elementos]}")


# --- Acumulación ---
print("\n--- Acumulación ---")

from itertools import accumulate
import operator

numeros = [1, 2, 3, 4, 5]
print(f"accumulate({numeros}): {list(accumulate(numeros))}")
print(f"accumulate(*, {numeros}): {list(accumulate(numeros, operator.mul))}")


# ==============================================================================
# GENERADORES PARA PROCESAMIENTO DE DATOS
# ==============================================================================

print("\n" + "=" * 60)
print("PIPELINES DE PROCESAMIENTO")
print("=" * 60)

print("""
Los generadores son ideales para crear pipelines de procesamiento
donde cada etapa procesa datos de forma lazy (perezosa).
""")

# Simulamos un archivo de log
logs = [
    "2024-01-15 10:00:00 INFO Usuario conectado",
    "2024-01-15 10:00:05 ERROR Base de datos no responde",
    "2024-01-15 10:00:10 INFO Reintentando conexión",
    "2024-01-15 10:00:15 ERROR Timeout de conexión",
    "2024-01-15 10:00:20 INFO Conexión restaurada",
    "2024-01-15 10:00:25 WARNING Memoria alta",
]

def leer_logs(lineas):
    """Simula lectura de archivo línea por línea."""
    for linea in lineas:
        yield linea

def parsear_log(lineas):
    """Parsea cada línea de log."""
    for linea in lineas:
        partes = linea.split(' ', 3)
        yield {
            'fecha': partes[0],
            'hora': partes[1],
            'nivel': partes[2],
            'mensaje': partes[3]
        }

def filtrar_nivel(logs_parseados, nivel):
    """Filtra logs por nivel."""
    for log in logs_parseados:
        if log['nivel'] == nivel:
            yield log

def formatear_salida(logs_filtrados):
    """Formatea la salida."""
    for log in logs_filtrados:
        yield f"[{log['hora']}] {log['mensaje']}"


# Pipeline completo
print("Pipeline de procesamiento de logs (solo ERROR):")
pipeline = formatear_salida(
    filtrar_nivel(
        parsear_log(
            leer_logs(logs)
        ),
        'ERROR'
    )
)

for linea in pipeline:
    print(f"  {linea}")


# Pipeline más legible con funciones intermedias
def crear_pipeline(datos, nivel='ERROR'):
    """Crea un pipeline de procesamiento."""
    datos = leer_logs(datos)
    datos = parsear_log(datos)
    datos = filtrar_nivel(datos, nivel)
    datos = formatear_salida(datos)
    return datos

print("\nPipeline (solo WARNING):")
for linea in crear_pipeline(logs, 'WARNING'):
    print(f"  {linea}")


# ==============================================================================
# GENERADORES PARA DATOS GRANDES
# ==============================================================================

print("\n" + "=" * 60)
print("PROCESAMIENTO DE DATOS GRANDES")
print("=" * 60)

def leer_archivo_grande(nombre_archivo, chunk_size=1024):
    """
    Generador que lee un archivo grande en chunks.
    (Simulado para el ejemplo)
    """
    # En la vida real:
    # with open(nombre_archivo, 'r') as f:
    #     while True:
    #         chunk = f.read(chunk_size)
    #         if not chunk:
    #             break
    #         yield chunk

    # Simulación
    datos_simulados = "ABCDEFGHIJ" * 10
    for i in range(0, len(datos_simulados), chunk_size):
        yield datos_simulados[i:i + chunk_size]


def procesar_chunks(chunks):
    """Procesa cada chunk."""
    for chunk in chunks:
        # Procesar (aquí solo contamos caracteres)
        yield len(chunk)


print("Procesamiento por chunks:")
chunks = leer_archivo_grande("archivo.txt", chunk_size=20)
for i, tamaño in enumerate(procesar_chunks(chunks), 1):
    print(f"  Chunk {i}: {tamaño} caracteres")


# Generador para números primos (infinito pero eficiente)
def primos():
    """Genera números primos infinitamente."""
    yield 2
    candidato = 3
    primos_encontrados = [2]

    while True:
        es_primo = True
        for p in primos_encontrados:
            if p * p > candidato:
                break
            if candidato % p == 0:
                es_primo = False
                break
        if es_primo:
            primos_encontrados.append(candidato)
            yield candidato
        candidato += 2

print("\nPrimeros 15 primos:")
gen_primos = primos()
print(f"  {[next(gen_primos) for _ in range(15)]}")


# ==============================================================================
# CORRUTINAS CON GENERADORES
# ==============================================================================

print("\n" + "=" * 60)
print("CORRUTINAS CON GENERADORES")
print("=" * 60)

print("""
Las corrutinas permiten suspender y reanudar la ejecución,
útiles para programación asíncrona y máquinas de estado.
""")

def corrutina_promedio():
    """Corrutina que calcula promedio en streaming."""
    total = 0
    contador = 0
    promedio = None

    while True:
        valor = yield promedio
        if valor is None:
            break
        total += valor
        contador += 1
        promedio = total / contador


# Usar la corrutina
print("Corrutina de promedio en streaming:")
promedio = corrutina_promedio()
next(promedio)  # Iniciar

for valor in [10, 20, 30, 40, 50]:
    resultado = promedio.send(valor)
    print(f"  Añadido {valor}, promedio actual: {resultado}")


# Máquina de estados con generador
def semaforo():
    """Máquina de estados de un semáforo."""
    while True:
        print("  🔴 ROJO - Detenerse")
        yield "rojo"
        print("  🟢 VERDE - Avanzar")
        yield "verde"
        print("  🟡 AMARILLO - Precaución")
        yield "amarillo"

print("\nSimulación de semáforo:")
sem = semaforo()
for _ in range(5):
    next(sem)


# ==============================================================================
# EJEMPLO COMPLETO: PROCESADOR DE CSV
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO COMPLETO: PROCESADOR DE CSV")
print("=" * 60)

def generar_csv_simulado():
    """Genera líneas de CSV simulado."""
    yield "nombre,edad,salario"
    yield "Ana,25,50000"
    yield "Luis,30,55000"
    yield "María,28,52000"
    yield "Carlos,35,60000"
    yield "Elena,27,48000"

def parsear_csv(lineas):
    """Parsea CSV a diccionarios."""
    iterador = iter(lineas)
    encabezados = next(iterador).split(',')

    for linea in iterador:
        valores = linea.split(',')
        yield dict(zip(encabezados, valores))

def convertir_tipos(registros):
    """Convierte tipos de datos."""
    for reg in registros:
        yield {
            'nombre': reg['nombre'],
            'edad': int(reg['edad']),
            'salario': float(reg['salario'])
        }

def filtrar_mayores(registros, edad_minima):
    """Filtra por edad mínima."""
    for reg in registros:
        if reg['edad'] >= edad_minima:
            yield reg

def calcular_estadisticas(registros):
    """Calcula estadísticas sobre los registros."""
    total_salario = 0
    total_edad = 0
    count = 0

    for reg in registros:
        total_salario += reg['salario']
        total_edad += reg['edad']
        count += 1
        yield reg

    # Esto se ejecuta después de procesar todos
    print(f"\n  Estadísticas finales:")
    print(f"    Total registros: {count}")
    print(f"    Salario promedio: ${total_salario / count:,.2f}")
    print(f"    Edad promedio: {total_edad / count:.1f}")


# Ejecutar pipeline
print("Procesando CSV (mayores de 27 años):")
pipeline = calcular_estadisticas(
    filtrar_mayores(
        convertir_tipos(
            parsear_csv(
                generar_csv_simulado()
            )
        ),
        edad_minima=27
    )
)

for persona in pipeline:
    print(f"  {persona['nombre']}: {persona['edad']} años, ${persona['salario']:,.2f}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea un generador 'fibonacci()' que genere la secuencia
   de Fibonacci infinitamente

2. Implementa un iterador 'Rango' que funcione como range()
   pero para números decimales (con paso decimal)

3. Crea un generador 'leer_en_batches(iterable, n)' que
   agrupe elementos en lotes de tamaño n

4. Implementa un generador 'ventana_deslizante(iterable, n)'
   que retorne tuplas de n elementos consecutivos

5. Crea un pipeline de procesamiento de texto que:
   - Lea líneas
   - Filtre líneas vacías
   - Convierta a minúsculas
   - Cuente palabras por línea

6. Implementa un generador 'intercalar(iter1, iter2)' que
   alterne elementos de dos iteradores

7. Crea un generador 'aplanar_profundo(estructura)' que
   aplane estructuras anidadas de cualquier profundidad

8. Implementa una corrutina que actúe como calculadora:
   - Recibe operaciones como tuplas ('suma', 5)
   - Mantiene un acumulador
   - Retorna el resultado actual
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 20_recursividad.py")
print("=" * 60)
