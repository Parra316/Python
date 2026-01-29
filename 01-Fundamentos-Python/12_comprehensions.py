"""
================================================================================
COMPREHENSIONS
================================================================================

Las comprehensions son una forma concisa y pythónica de crear
colecciones a partir de iterables.

TIPOS:
1. List comprehension: [expresión for item in iterable]
2. Dict comprehension: {clave: valor for item in iterable}
3. Set comprehension: {expresión for item in iterable}
4. Generator expression: (expresión for item in iterable)

VENTAJAS:
- Código más legible y conciso
- Generalmente más rápido que bucles equivalentes
- Estilo pythónico

================================================================================
"""

# ==============================================================================
# LIST COMPREHENSION
# ==============================================================================

print("=" * 60)
print("LIST COMPREHENSION")
print("=" * 60)

# Forma tradicional
print("--- Forma tradicional vs comprehension ---")
cuadrados_tradicional = []
for x in range(5):
    cuadrados_tradicional.append(x ** 2)
print(f"Tradicional: {cuadrados_tradicional}")

# List comprehension
cuadrados = [x ** 2 for x in range(5)]
print(f"Comprehension: {cuadrados}")

# Sintaxis básica
print("\n--- Sintaxis: [expresión for item in iterable] ---")
numeros = [1, 2, 3, 4, 5]
dobles = [n * 2 for n in numeros]
print(f"Dobles de {numeros}: {dobles}")

# Con strings
palabras = ["hola", "mundo", "python"]
mayusculas = [p.upper() for p in palabras]
print(f"Mayúsculas: {mayusculas}")

longitudes = [len(p) for p in palabras]
print(f"Longitudes: {longitudes}")


# ==============================================================================
# COMPREHENSION CON CONDICIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("COMPREHENSION CON CONDICIÓN")
print("=" * 60)

# if al final: filtrar
print("--- Con if (filtrar) ---")
numeros = range(10)

pares = [x for x in numeros if x % 2 == 0]
print(f"Pares de 0-9: {pares}")

mayores_que_5 = [x for x in numeros if x > 5]
print(f"Mayores que 5: {mayores_que_5}")

# Múltiples condiciones
pares_mayores = [x for x in numeros if x % 2 == 0 if x > 4]
print(f"Pares mayores que 4: {pares_mayores}")

# if-else en la expresión: transformar
print("\n--- Con if-else (transformar) ---")
# Sintaxis: [valor_si_true if condición else valor_si_false for item in iterable]
par_impar = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(f"Par/Impar: {par_impar}")

# Reemplazar negativos con cero
numeros = [-3, -1, 0, 2, 5, -4, 8]
positivos = [x if x > 0 else 0 for x in numeros]
print(f"Negativos a cero: {numeros} → {positivos}")


# ==============================================================================
# COMPREHENSION ANIDADA
# ==============================================================================

print("\n" + "=" * 60)
print("COMPREHENSION ANIDADA")
print("=" * 60)

# Aplanar lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [num for fila in matriz for num in fila]
print(f"Aplanar {matriz}:")
print(f"  → {plana}")

# Crear matriz
print("\n--- Crear matriz ---")
matriz_3x3 = [[j for j in range(3)] for i in range(3)]
print(f"Matriz 3x3: {matriz_3x3}")

# Tabla de multiplicar
print("\n--- Tabla de multiplicar ---")
tabla = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for fila in tabla:
    print(f"  {fila}")

# Producto cartesiano
colores = ["rojo", "verde"]
tamaños = ["S", "M", "L"]
combinaciones = [(c, t) for c in colores for t in tamaños]
print(f"\nCombinaciones: {combinaciones}")


# ==============================================================================
# DICT COMPREHENSION
# ==============================================================================

print("\n" + "=" * 60)
print("DICT COMPREHENSION")
print("=" * 60)

# Sintaxis: {clave: valor for item in iterable}
print("--- Básico ---")
cuadrados = {x: x**2 for x in range(6)}
print(f"Cuadrados: {cuadrados}")

# Desde dos listas
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
personas = {n: e for n, e in zip(nombres, edades)}
print(f"Personas: {personas}")

# Con condición
print("\n--- Con condición ---")
numeros = range(10)
pares_cuadrado = {x: x**2 for x in numeros if x % 2 == 0}
print(f"Cuadrados de pares: {pares_cuadrado}")

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(f"Invertido: {original} → {invertido}")

# Filtrar diccionario
precios = {"manzana": 1.5, "naranja": 2.0, "plátano": 0.8, "uva": 3.5}
caros = {k: v for k, v in precios.items() if v > 1.5}
print(f"Productos caros: {caros}")


# ==============================================================================
# SET COMPREHENSION
# ==============================================================================

print("\n" + "=" * 60)
print("SET COMPREHENSION")
print("=" * 60)

# Sintaxis: {expresión for item in iterable}
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unicos = {x for x in numeros}
print(f"Únicos de {numeros}: {unicos}")

# Con transformación
palabras = ["Hola", "MUNDO", "hola", "Python", "PYTHON"]
unicas_lower = {p.lower() for p in palabras}
print(f"Palabras únicas: {unicas_lower}")

# Longitudes únicas
longitudes = {len(p) for p in palabras}
print(f"Longitudes únicas: {longitudes}")


# ==============================================================================
# GENERATOR EXPRESSIONS
# ==============================================================================

print("\n" + "=" * 60)
print("GENERATOR EXPRESSIONS")
print("=" * 60)

print("""
Los generators son como list comprehensions pero:
- Usan paréntesis () en lugar de corchetes []
- No crean toda la lista en memoria
- Generan valores bajo demanda (lazy evaluation)
- Ideales para grandes cantidades de datos
""")

# Comparación de memoria
import sys

lista = [x**2 for x in range(1000)]
generador = (x**2 for x in range(1000))

print(f"Tamaño lista: {sys.getsizeof(lista)} bytes")
print(f"Tamaño generador: {sys.getsizeof(generador)} bytes")

# Iterar sobre generador
gen = (x**2 for x in range(5))
print(f"\nIterando sobre generador:")
for valor in gen:
    print(f"  {valor}")

# Solo se puede iterar una vez
print(f"Segunda iteración (vacía):")
for valor in gen:
    print(f"  {valor}")  # No imprime nada

# Uso en funciones que aceptan iterables
numeros = (x for x in range(1, 6))
print(f"\nsum() con generador: {sum(numeros)}")

# Equivalente pero más eficiente
suma = sum(x**2 for x in range(1000000))  # No necesita paréntesis extra
print(f"Suma de cuadrados (1M números): {suma}")


# ==============================================================================
# CUÁNDO USAR CADA UNO
# ==============================================================================

print("\n" + "=" * 60)
print("CUÁNDO USAR CADA UNO")
print("=" * 60)

print("""
COMPREHENSION es preferible cuando:
- La lógica es simple (1-2 líneas)
- Mejora la legibilidad
- Necesitas crear una colección

BUCLE TRADICIONAL es preferible cuando:
- La lógica es compleja
- Necesitas efectos secundarios (print, modificar variables)
- Tienes múltiples operaciones por iteración

GENERATOR es preferible cuando:
- Trabajas con grandes cantidades de datos
- Solo necesitas iterar una vez
- Quieres ahorrar memoria
""")

# Ejemplo: cuándo NO usar comprehension
print("--- Cuándo NO usar comprehension ---")

# MALO: demasiado complejo
# resultado = [x if x > 0 else -x if x < -10 else 0 for x in numeros if x != 5]

# MEJOR: usar bucle tradicional
numeros = [-15, -5, 0, 5, 10, 15]
resultado = []
for x in numeros:
    if x == 5:
        continue
    if x > 0:
        resultado.append(x)
    elif x < -10:
        resultado.append(-x)
    else:
        resultado.append(0)
print(f"Resultado: {resultado}")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Procesar lista de diccionarios
print("--- Procesar datos ---")
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 92},
    {"nombre": "María", "nota": 78},
    {"nombre": "Carlos", "nota": 95},
    {"nombre": "Elena", "nota": 88}
]

# Nombres de aprobados (nota >= 80)
aprobados = [e["nombre"] for e in estudiantes if e["nota"] >= 80]
print(f"Aprobados: {aprobados}")

# Diccionario nombre: calificación
calificaciones = {
    e["nombre"]: "A" if e["nota"] >= 90 else "B" if e["nota"] >= 80 else "C"
    for e in estudiantes
}
print(f"Calificaciones: {calificaciones}")

# 2. Matriz transpuesta
print("\n--- Transponer matriz ---")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(f"Original: {matriz}")
print(f"Transpuesta: {transpuesta}")

# 3. Frecuencia de caracteres
print("\n--- Frecuencia de caracteres ---")
texto = "abracadabra"
frecuencia = {c: texto.count(c) for c in set(texto)}
print(f"Frecuencia en '{texto}': {frecuencia}")

# 4. Validar y limpiar datos
print("\n--- Limpiar datos ---")
datos_sucios = ["  Ana  ", "LUIS", "", "  ", "María", "123"]
datos_limpios = [d.strip().title() for d in datos_sucios if d.strip() and d.strip().isalpha()]
print(f"Datos sucios: {datos_sucios}")
print(f"Datos limpios: {datos_limpios}")

# 5. Números primos con comprehension
print("\n--- Números primos ---")
def es_primo(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primos = [n for n in range(50) if es_primo(n)]
print(f"Primos hasta 50: {primos}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Usa list comprehension para obtener las primeras letras
   de cada palabra en una oración

2. Crea un diccionario con los cuadrados de los números
   del 1 al 10, pero solo de los impares

3. Dada una lista de strings, crea una nueva lista con
   solo los palíndromos (se leen igual al derecho y al revés)

4. Usa comprehension para crear una matriz identidad 4x4

5. Dada una lista de números, crea un diccionario que agrupe
   los números por su resto al dividir entre 3

6. Usa generator expression para calcular la suma de los
   primeros 1 millón de números cuadrados perfectos
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 13_manejo_errores.py")
print("=" * 60)
