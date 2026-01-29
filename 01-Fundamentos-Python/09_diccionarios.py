"""
================================================================================
DICCIONARIOS
================================================================================

Los diccionarios son colecciones de pares clave-valor.
Son una de las estructuras más usadas y poderosas de Python.

CARACTERÍSTICAS:
- Pares clave: valor
- Las claves deben ser únicas e inmutables
- Los valores pueden ser de cualquier tipo
- Ordenados (desde Python 3.7+)
- Muy eficientes para búsqueda: O(1)

================================================================================
"""

# ==============================================================================
# CREAR DICCIONARIOS
# ==============================================================================

print("=" * 60)
print("CREAR DICCIONARIOS")
print("=" * 60)

# Diccionario vacío
vacio = {}
vacio2 = dict()

# Con valores
persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid"
}

# Claves de diferentes tipos
mixto = {
    "string": 1,
    42: "numero",
    (1, 2): "tupla"  # Tuplas pueden ser claves
}

print(f"Diccionario vacío: {vacio}")
print(f"Persona: {persona}")
print(f"Mixto: {mixto}")

# Desde lista de tuplas
pares = [("a", 1), ("b", 2), ("c", 3)]
desde_tuplas = dict(pares)
print(f"\nDesde tuplas: {desde_tuplas}")

# Con dict()
usando_dict = dict(nombre="Luis", edad=30)
print(f"Con dict(): {usando_dict}")

# Con fromkeys (mismo valor para todas las claves)
claves = ["a", "b", "c"]
todos_cero = dict.fromkeys(claves, 0)
print(f"fromkeys: {todos_cero}")


# ==============================================================================
# ACCEDER A VALORES
# ==============================================================================

print("\n" + "=" * 60)
print("ACCEDER A VALORES")
print("=" * 60)

persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid",
    "hobbies": ["leer", "viajar"]
}

# Por clave
print(f"persona['nombre']: {persona['nombre']}")
print(f"persona['hobbies']: {persona['hobbies']}")
print(f"persona['hobbies'][0]: {persona['hobbies'][0]}")

# Con get() - más seguro (no da error si no existe)
print(f"\npersona.get('edad'): {persona.get('edad')}")
print(f"persona.get('salario'): {persona.get('salario')}")  # None
print(f"persona.get('salario', 0): {persona.get('salario', 0)}")  # Valor por defecto

# Verificar si existe una clave
print(f"\n'nombre' in persona: {'nombre' in persona}")
print(f"'salario' in persona: {'salario' in persona}")


# ==============================================================================
# MODIFICAR DICCIONARIOS
# ==============================================================================

print("\n" + "=" * 60)
print("MODIFICAR DICCIONARIOS")
print("=" * 60)

persona = {"nombre": "Ana", "edad": 28}
print(f"Original: {persona}")

# Añadir/modificar elemento
persona["ciudad"] = "Madrid"
print(f"Añadir ciudad: {persona}")

persona["edad"] = 29
print(f"Modificar edad: {persona}")

# update() - añadir múltiples
persona.update({"trabajo": "ingeniera", "salario": 45000})
print(f"update(): {persona}")

# También con pares clave=valor
persona.update(email="ana@email.com")
print(f"update(email=...): {persona}")

# setdefault() - añadir solo si no existe
persona.setdefault("ciudad", "Barcelona")  # No cambia, ya existe
persona.setdefault("pais", "España")  # Añade, no existía
print(f"setdefault(): {persona}")


# ==============================================================================
# ELIMINAR ELEMENTOS
# ==============================================================================

print("\n" + "=" * 60)
print("ELIMINAR ELEMENTOS")
print("=" * 60)

datos = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Original: {datos}")

# pop() - eliminar y retornar
valor = datos.pop("a")
print(f"pop('a'): retornó {valor}, dict: {datos}")

# pop() con valor por defecto (no error si no existe)
valor = datos.pop("z", "no existe")
print(f"pop('z', 'no existe'): {valor}")

# popitem() - eliminar último par
clave, valor = datos.popitem()
print(f"popitem(): ({clave}, {valor}), dict: {datos}")

# del
del datos["b"]
print(f"del datos['b']: {datos}")

# clear() - eliminar todo
datos.clear()
print(f"clear(): {datos}")


# ==============================================================================
# ITERAR SOBRE DICCIONARIOS
# ==============================================================================

print("\n" + "=" * 60)
print("ITERAR SOBRE DICCIONARIOS")
print("=" * 60)

persona = {"nombre": "Ana", "edad": 28, "ciudad": "Madrid"}

# Iterar sobre claves (por defecto)
print("--- Claves ---")
for clave in persona:
    print(f"  {clave}")

# Equivalente explícito
print("\n--- .keys() ---")
for clave in persona.keys():
    print(f"  {clave}")

# Iterar sobre valores
print("\n--- .values() ---")
for valor in persona.values():
    print(f"  {valor}")

# Iterar sobre pares clave-valor
print("\n--- .items() ---")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")


# ==============================================================================
# DICCIONARIOS ANIDADOS
# ==============================================================================

print("\n" + "=" * 60)
print("DICCIONARIOS ANIDADOS")
print("=" * 60)

empresa = {
    "nombre": "TechCorp",
    "empleados": {
        "e001": {
            "nombre": "Ana García",
            "departamento": "Ingeniería",
            "salario": 50000
        },
        "e002": {
            "nombre": "Luis López",
            "departamento": "Marketing",
            "salario": 45000
        }
    },
    "ubicaciones": ["Madrid", "Barcelona"]
}

print(f"Empresa: {empresa['nombre']}")
print(f"Empleado e001: {empresa['empleados']['e001']['nombre']}")
print(f"Ubicaciones: {empresa['ubicaciones']}")

# Modificar anidado
empresa["empleados"]["e001"]["salario"] = 55000
print(f"Nuevo salario e001: {empresa['empleados']['e001']['salario']}")


# ==============================================================================
# MÉTODOS ÚTILES
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS ÚTILES")
print("=" * 60)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# copy()
copia = d1.copy()
copia["a"] = 999
print(f"Original: {d1}")
print(f"Copia modificada: {copia}")

# Unir diccionarios (Python 3.9+)
print(f"\nUnir con |: {d1 | d2}")

# Antes de Python 3.9
combinado = {**d1, **d2}
print(f"Unir con **: {combinado}")


# ==============================================================================
# DICT COMPREHENSION
# ==============================================================================

print("\n" + "=" * 60)
print("DICT COMPREHENSION")
print("=" * 60)

# Crear diccionario de cuadrados
cuadrados = {x: x**2 for x in range(6)}
print(f"Cuadrados: {cuadrados}")

# Con condición
pares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Cuadrados de pares: {pares}")

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(f"Invertido: {invertido}")

# Desde dos listas
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
personas = {n: e for n, e in zip(nombres, edades)}
print(f"Desde listas: {personas}")


# ==============================================================================
# DEFAULTDICT Y COUNTER
# ==============================================================================

print("\n" + "=" * 60)
print("DEFAULTDICT Y COUNTER")
print("=" * 60)

from collections import defaultdict, Counter

# defaultdict - valor por defecto automático
print("--- defaultdict ---")
conteo = defaultdict(int)  # Valores por defecto: 0
palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]

for palabra in palabras:
    conteo[palabra] += 1  # No necesita verificar si existe

print(f"Conteo: {dict(conteo)}")

# defaultdict con lista
grupos = defaultdict(list)
personas = [("ventas", "Ana"), ("tech", "Luis"), ("ventas", "María")]

for depto, nombre in personas:
    grupos[depto].append(nombre)

print(f"Grupos: {dict(grupos)}")

# Counter - contar elementos
print("\n--- Counter ---")
texto = "abracadabra"
contador = Counter(texto)
print(f"Counter('{texto}'): {contador}")
print(f"Más comunes: {contador.most_common(3)}")

# Operaciones con Counter
c1 = Counter("aab")
c2 = Counter("abc")
print(f"\n{c1} + {c2} = {c1 + c2}")
print(f"{c1} - {c2} = {c1 - c2}")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Agrupar por clave
print("--- Agrupar estudiantes por nota ---")
estudiantes = [
    {"nombre": "Ana", "nota": "A"},
    {"nombre": "Luis", "nota": "B"},
    {"nombre": "María", "nota": "A"},
    {"nombre": "Carlos", "nota": "B"},
    {"nombre": "Elena", "nota": "A"}
]

por_nota = defaultdict(list)
for est in estudiantes:
    por_nota[est["nota"]].append(est["nombre"])

for nota, nombres in sorted(por_nota.items()):
    print(f"  Nota {nota}: {nombres}")

# 2. Caché simple
print("\n--- Caché de resultados ---")
cache = {}

def fibonacci_con_cache(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci_con_cache(n-1) + fibonacci_con_cache(n-2)
    cache[n] = resultado
    return resultado

print(f"  fibonacci(10) = {fibonacci_con_cache(10)}")
print(f"  Cache: {cache}")

# 3. Contar palabras
print("\n--- Contar palabras en texto ---")
texto = "el sol brilla el cielo está azul y el mar también"
palabras = texto.split()
conteo = Counter(palabras)
print(f"  Palabras más comunes: {conteo.most_common(3)}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea un diccionario que almacene los precios de productos.
   Escribe funciones para:
   - Añadir producto
   - Eliminar producto
   - Buscar precio
   - Aplicar descuento a todos

2. Dado un texto, cuenta la frecuencia de cada palabra
   e imprime las 5 más comunes

3. Crea una función que reciba dos diccionarios y los
   combine. Si hay claves repetidas, sumar los valores

4. Implementa una agenda de contactos con diccionarios:
   - Añadir contacto (nombre, teléfono, email)
   - Buscar por nombre
   - Listar todos
   - Eliminar contacto

5. Dado una lista de estudiantes con sus notas, crea
   un diccionario que agrupe por rango de nota:
   "excelente" (90-100), "bueno" (70-89), "regular" (50-69)

6. Escribe una función que encuentre la primera letra
   que no se repite en un string usando diccionarios
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 10_funciones_basicas.py")
print("=" * 60)
