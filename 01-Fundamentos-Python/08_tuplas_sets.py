"""
================================================================================
TUPLAS Y SETS (CONJUNTOS)
================================================================================

TUPLAS:
- Colecciones ordenadas e INMUTABLES
- Se usan para datos que no deben cambiar
- Más eficientes en memoria que las listas
- Pueden usarse como claves de diccionario

SETS (CONJUNTOS):
- Colecciones NO ordenadas de elementos únicos
- NO permiten duplicados
- Muy eficientes para operaciones de membresía
- Soportan operaciones matemáticas de conjuntos

================================================================================
"""

# ==============================================================================
# TUPLAS
# ==============================================================================

print("=" * 60)
print("TUPLAS")
print("=" * 60)

# Crear tuplas
tupla_vacia = ()
tupla_vacia2 = tuple()
numeros = (1, 2, 3, 4, 5)
mixta = (1, "dos", 3.0, True)

print(f"Tupla vacía: {tupla_vacia}")
print(f"Números: {numeros}")
print(f"Mixta: {mixta}")

# Tupla de un elemento (necesita coma)
un_elemento = (42,)  # ¡La coma es importante!
no_es_tupla = (42)   # Esto es solo un entero con paréntesis
print(f"\n(42,) es tupla: {type(un_elemento)}")
print(f"(42) es int: {type(no_es_tupla)}")

# Crear sin paréntesis (tuple packing)
coords = 10, 20, 30
print(f"\nTuple packing: {coords}, tipo: {type(coords)}")

# Desde otros iterables
from_list = tuple([1, 2, 3])
from_string = tuple("ABC")
print(f"Desde lista: {from_list}")
print(f"Desde string: {from_string}")


# ==============================================================================
# ACCEDER A ELEMENTOS DE TUPLA
# ==============================================================================

print("\n" + "=" * 60)
print("ACCEDER A ELEMENTOS")
print("=" * 60)

colores = ("rojo", "verde", "azul", "amarillo")
print(f"Tupla: {colores}")

# Indexación
print(f"colores[0] = '{colores[0]}'")
print(f"colores[-1] = '{colores[-1]}'")

# Slicing
print(f"colores[1:3] = {colores[1:3]}")
print(f"colores[::-1] = {colores[::-1]}")

# Desempaquetado
r, g, b, y = colores
print(f"\nDesempaquetado: r={r}, g={g}, b={b}, y={y}")

# Con asterisco
primero, *resto = colores
print(f"primero={primero}, resto={resto}")


# ==============================================================================
# INMUTABILIDAD DE TUPLAS
# ==============================================================================

print("\n" + "=" * 60)
print("INMUTABILIDAD")
print("=" * 60)

print("""
Las tuplas NO se pueden modificar después de crearlas.
Esto las hace:
- Seguras (no se modifican accidentalmente)
- Hashables (pueden ser claves de diccionario)
- Más eficientes en memoria
""")

tupla = (1, 2, 3)
print(f"Tupla: {tupla}")
print("tupla[0] = 10  # ¡Error! TypeError")

# PERO: si contiene elementos mutables, esos SÍ pueden cambiar
tupla_con_lista = (1, 2, [3, 4])
print(f"\nTupla con lista: {tupla_con_lista}")
tupla_con_lista[2].append(5)
print(f"Después de modificar lista interna: {tupla_con_lista}")


# ==============================================================================
# MÉTODOS DE TUPLAS
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS DE TUPLAS")
print("=" * 60)

numeros = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla: {numeros}")

# Solo dos métodos (inmutabilidad)
print(f".count(2): {numeros.count(2)}")  # Contar ocurrencias
print(f".index(4): {numeros.index(4)}")  # Índice de primera ocurrencia


# ==============================================================================
# TUPLAS NOMBRADAS
# ==============================================================================

print("\n" + "=" * 60)
print("NAMED TUPLES")
print("=" * 60)

from collections import namedtuple

# Definir un tipo de tupla nombrada
Punto = namedtuple('Punto', ['x', 'y'])
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Crear instancias
p1 = Punto(10, 20)
persona = Persona("Ana", 25, "Madrid")

print(f"Punto: {p1}")
print(f"  Acceso por nombre: x={p1.x}, y={p1.y}")
print(f"  Acceso por índice: {p1[0]}, {p1[1]}")

print(f"\nPersona: {persona}")
print(f"  {persona.nombre} tiene {persona.edad} años")


# ==============================================================================
# SETS (CONJUNTOS)
# ==============================================================================

print("\n" + "=" * 60)
print("SETS (CONJUNTOS)")
print("=" * 60)

# Crear sets
set_vacio = set()  # ¡NO usar {} que crea diccionario vacío!
numeros = {1, 2, 3, 4, 5}
letras = set("abracadabra")

print(f"Set vacío: {set_vacio}")
print(f"Números: {numeros}")
print(f"Letras (sin duplicados): {letras}")

# Los sets NO tienen orden garantizado
print("\n--- NO tienen orden ---")
for _ in range(3):
    print(f"  {set('hello')}")

# Eliminar duplicados de lista
print("\n--- Eliminar duplicados ---")
lista_dup = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
sin_dup = list(set(lista_dup))
print(f"  {lista_dup} → {sin_dup}")


# ==============================================================================
# MÉTODOS DE SETS
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS DE SETS")
print("=" * 60)

# --- Añadir elementos ---
print("--- Añadir elementos ---")
frutas = {"manzana", "naranja"}
print(f"Original: {frutas}")

frutas.add("plátano")
print(f".add('plátano'): {frutas}")

frutas.update(["uva", "kiwi"])  # Añadir múltiples
print(f".update(['uva', 'kiwi']): {frutas}")

# --- Eliminar elementos ---
print("\n--- Eliminar elementos ---")
frutas.remove("naranja")  # Error si no existe
print(f".remove('naranja'): {frutas}")

frutas.discard("mango")  # No da error si no existe
print(f".discard('mango'): {frutas}")

elemento = frutas.pop()  # Elimina y retorna elemento arbitrario
print(f".pop(): eliminó '{elemento}'")

# --- Pertenencia ---
print("\n--- Pertenencia (muy rápido) ---")
numeros = set(range(1000000))
print(f"500000 in set: {500000 in numeros}")  # O(1)


# ==============================================================================
# OPERACIONES DE CONJUNTOS
# ==============================================================================

print("\n" + "=" * 60)
print("OPERACIONES DE CONJUNTOS")
print("=" * 60)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")

# Unión: elementos en A o B
print(f"\nUnión (A | B): {A | B}")
print(f"Unión (A.union(B)): {A.union(B)}")

# Intersección: elementos en A y B
print(f"\nIntersección (A & B): {A & B}")
print(f"Intersección (A.intersection(B)): {A.intersection(B)}")

# Diferencia: elementos en A pero no en B
print(f"\nDiferencia (A - B): {A - B}")
print(f"Diferencia (A.difference(B)): {A.difference(B)}")

# Diferencia simétrica: elementos en A o B, pero no en ambos
print(f"\nDiferencia simétrica (A ^ B): {A ^ B}")
print(f"Diferencia simétrica: {A.symmetric_difference(B)}")

# Subconjunto y superconjunto
C = {1, 2, 3}
print(f"\nC = {C}")
print(f"C es subconjunto de A (C <= A): {C <= A}")
print(f"A es superconjunto de C (A >= C): {A >= C}")
print(f"C.issubset(A): {C.issubset(A)}")

# Conjuntos disjuntos (sin elementos en común)
D = {10, 11, 12}
print(f"\nD = {D}")
print(f"A y D son disjuntos: {A.isdisjoint(D)}")


# ==============================================================================
# FROZENSET (SET INMUTABLE)
# ==============================================================================

print("\n" + "=" * 60)
print("FROZENSET")
print("=" * 60)

print("""
frozenset es un set inmutable.
Puede usarse como clave de diccionario o elemento de otro set.
""")

frozen = frozenset([1, 2, 3])
print(f"Frozenset: {frozen}")
# frozen.add(4)  # Error: frozenset es inmutable

# Usar como clave de diccionario
datos = {
    frozenset([1, 2]): "grupo A",
    frozenset([3, 4]): "grupo B"
}
print(f"Diccionario con frozenset: {datos}")


# ==============================================================================
# CUÁNDO USAR CADA UNO
# ==============================================================================

print("\n" + "=" * 60)
print("CUÁNDO USAR CADA ESTRUCTURA")
print("=" * 60)

print("""
┌─────────┬──────────┬────────────┬───────────────────────────┐
│ Tipo    │ Ordenado │ Mutable    │ Usar cuando...            │
├─────────┼──────────┼────────────┼───────────────────────────┤
│ Lista   │ Sí       │ Sí         │ Colección que cambia      │
│ Tupla   │ Sí       │ No         │ Datos que no deben cambiar│
│ Set     │ No       │ Sí         │ Elementos únicos, búsqueda│
│ Frozenset│ No      │ No         │ Set como clave de dict    │
└─────────┴──────────┴────────────┴───────────────────────────┘

RENDIMIENTO:
- Búsqueda en lista: O(n)
- Búsqueda en set: O(1)
- Tupla: más eficiente en memoria que lista
""")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Retornar múltiples valores (tupla)
print("--- Retornar múltiples valores ---")
def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, promedio = estadisticas([1, 2, 3, 4, 5])
print(f"  Min: {minimo}, Max: {maximo}, Promedio: {promedio}")

# 2. Encontrar elementos comunes
print("\n--- Elementos comunes ---")
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comunes = list(set(lista1) & set(lista2))
print(f"  Comunes entre {lista1} y {lista2}: {comunes}")

# 3. Contar elementos únicos
print("\n--- Contar únicos ---")
texto = "abracadabra"
unicos = len(set(texto))
print(f"  Caracteres únicos en '{texto}': {unicos}")

# 4. Verificar anagramas
print("\n--- Verificar anagramas ---")
def son_anagramas(palabra1, palabra2):
    return set(palabra1.lower()) == set(palabra2.lower()) and \
           sorted(palabra1.lower()) == sorted(palabra2.lower())

pares = [("listen", "silent"), ("hello", "world")]
for p1, p2 in pares:
    resultado = "Sí" if son_anagramas(p1, p2) else "No"
    print(f"  '{p1}' y '{p2}': {resultado} son anagramas")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea una función que reciba dos listas y retorne:
   - Elementos solo en la primera
   - Elementos solo en la segunda
   - Elementos en ambas

2. Escribe una función que verifique si una palabra
   tiene todas las vocales (usando sets)

3. Dada una lista de números, usa sets para encontrar
   el primer número que se repite

4. Crea una función que reciba una oración y retorne
   un set con las palabras únicas (sin importar mayúsculas)

5. Implementa una función que verifique si dos strings
   usan exactamente los mismos caracteres (son anagramas)

6. Usa tuplas nombradas para representar productos
   con nombre, precio y cantidad, y calcula el total
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 09_diccionarios.py")
print("=" * 60)
