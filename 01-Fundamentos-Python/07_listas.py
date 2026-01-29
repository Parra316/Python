"""
================================================================================
LISTAS
================================================================================

Las listas son colecciones ordenadas y mutables de elementos.
Son uno de los tipos de datos más usados en Python.

CARACTERÍSTICAS:
- Ordenadas: mantienen el orden de inserción
- Mutables: se pueden modificar después de crearlas
- Permiten duplicados
- Pueden contener diferentes tipos de datos
- Son dinámicas: pueden crecer o reducirse

================================================================================
"""

# ==============================================================================
# CREAR LISTAS
# ==============================================================================

print("=" * 60)
print("CREAR LISTAS")
print("=" * 60)

# Lista vacía
vacia = []
vacia2 = list()

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "naranja", "plátano"]
mixta = [1, "dos", 3.0, True, None]

print(f"Lista vacía: {vacia}")
print(f"Números: {numeros}")
print(f"Frutas: {frutas}")
print(f"Mixta: {mixta}")

# Crear desde otros iterables
from_string = list("Python")
from_range = list(range(5))

print(f"\nDesde string 'Python': {from_string}")
print(f"Desde range(5): {from_range}")

# Lista anidada (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\nMatriz: {matriz}")


# ==============================================================================
# ACCEDER A ELEMENTOS
# ==============================================================================

print("\n" + "=" * 60)
print("ACCEDER A ELEMENTOS")
print("=" * 60)

frutas = ["manzana", "naranja", "plátano", "uva", "kiwi"]
print(f"Lista: {frutas}")

# Por índice
print(f"\nfrutas[0] = '{frutas[0]}'")
print(f"frutas[2] = '{frutas[2]}'")
print(f"frutas[-1] = '{frutas[-1]}'")  # Último
print(f"frutas[-2] = '{frutas[-2]}'")  # Penúltimo

# Slicing
print(f"\nfrutas[1:3] = {frutas[1:3]}")
print(f"frutas[:3] = {frutas[:3]}")
print(f"frutas[2:] = {frutas[2:]}")
print(f"frutas[::2] = {frutas[::2]}")
print(f"frutas[::-1] = {frutas[::-1]}")  # Invertir

# En matriz
print(f"\nmatriz[1][2] = {matriz[1][2]}")  # Fila 1, columna 2


# ==============================================================================
# MODIFICAR LISTAS
# ==============================================================================

print("\n" + "=" * 60)
print("MODIFICAR LISTAS")
print("=" * 60)

numeros = [1, 2, 3, 4, 5]
print(f"Original: {numeros}")

# Modificar un elemento
numeros[0] = 10
print(f"numeros[0] = 10: {numeros}")

# Modificar un rango
numeros[1:3] = [20, 30]
print(f"numeros[1:3] = [20, 30]: {numeros}")

# Insertar elementos con slicing
numeros[2:2] = [25]  # Insertar sin eliminar
print(f"numeros[2:2] = [25]: {numeros}")


# ==============================================================================
# MÉTODOS DE LISTAS
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS DE LISTAS")
print("=" * 60)

# --- Añadir elementos ---
print("--- Añadir elementos ---")
lista = [1, 2, 3]
print(f"Original: {lista}")

lista.append(4)  # Añadir al final
print(f".append(4): {lista}")

lista.insert(0, 0)  # Insertar en posición
print(f".insert(0, 0): {lista}")

lista.extend([5, 6])  # Añadir múltiples
print(f".extend([5, 6]): {lista}")

# Diferencia entre append y extend
print("\n--- append vs extend ---")
a = [1, 2]
a.append([3, 4])  # Añade la lista como elemento
print(f"append([3,4]): {a}")

b = [1, 2]
b.extend([3, 4])  # Añade los elementos de la lista
print(f"extend([3,4]): {b}")

# --- Eliminar elementos ---
print("\n--- Eliminar elementos ---")
lista = [1, 2, 3, 2, 4, 2, 5]
print(f"Original: {lista}")

lista.remove(2)  # Elimina la PRIMERA ocurrencia
print(f".remove(2): {lista}")

elemento = lista.pop()  # Elimina y retorna el último
print(f".pop(): eliminó {elemento}, lista: {lista}")

elemento = lista.pop(0)  # Elimina y retorna el índice 0
print(f".pop(0): eliminó {elemento}, lista: {lista}")

lista.clear()  # Elimina todos
print(f".clear(): {lista}")

# del: eliminar por índice o rango
lista = [0, 1, 2, 3, 4, 5]
del lista[0]
print(f"\ndel lista[0]: {lista}")
del lista[1:3]
print(f"del lista[1:3]: {lista}")

# --- Buscar elementos ---
print("\n--- Buscar elementos ---")
lista = ["a", "b", "c", "b", "d"]
print(f"Lista: {lista}")

print(f"'b' in lista: {'b' in lista}")
print(f"lista.index('b'): {lista.index('b')}")  # Primera ocurrencia
print(f"lista.count('b'): {lista.count('b')}")

# --- Ordenar ---
print("\n--- Ordenar ---")
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numeros}")

numeros.sort()
print(f".sort(): {numeros}")

numeros.sort(reverse=True)
print(f".sort(reverse=True): {numeros}")

# sorted() retorna nueva lista (no modifica original)
original = [3, 1, 4, 1, 5]
ordenada = sorted(original)
print(f"\nsorted({original}): {ordenada}")
print(f"Original sin cambios: {original}")

# --- Invertir ---
print("\n--- Invertir ---")
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(f".reverse(): {lista}")

# --- Copiar ---
print("\n--- Copiar ---")
original = [1, 2, 3]
# ¡Cuidado! Esto NO copia:
referencia = original
referencia[0] = 999
print(f"Referencia (modifica original): {original}")

# Formas de copiar:
original = [1, 2, 3]
copia1 = original.copy()
copia2 = original[:]
copia3 = list(original)
copia1[0] = 111
print(f"Copia (no modifica original): {original}")


# ==============================================================================
# LISTAS Y FUNCIONES ÚTILES
# ==============================================================================

print("\n" + "=" * 60)
print("FUNCIONES ÚTILES")
print("=" * 60)

numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Lista: {numeros}")

print(f"len(): {len(numeros)}")
print(f"sum(): {sum(numeros)}")
print(f"min(): {min(numeros)}")
print(f"max(): {max(numeros)}")
print(f"any([0, 0, 1]): {any([0, 0, 1])}")  # ¿Alguno es True?
print(f"all([1, 1, 1]): {all([1, 1, 1])}")  # ¿Todos son True?


# ==============================================================================
# DESEMPAQUETADO
# ==============================================================================

print("\n" + "=" * 60)
print("DESEMPAQUETADO")
print("=" * 60)

# Desempaquetado básico
coordenadas = [10, 20]
x, y = coordenadas
print(f"{coordenadas} → x={x}, y={y}")

# Con asterisco (resto)
primero, *resto = [1, 2, 3, 4, 5]
print(f"primero={primero}, resto={resto}")

primero, *medio, ultimo = [1, 2, 3, 4, 5]
print(f"primero={primero}, medio={medio}, ultimo={ultimo}")

# Ignorar valores
a, _, c = [1, 2, 3]  # Ignoramos el segundo
print(f"a={a}, c={c}")


# ==============================================================================
# LISTAS POR COMPRENSIÓN (PREVIEW)
# ==============================================================================

print("\n" + "=" * 60)
print("LIST COMPREHENSION (Vista previa)")
print("=" * 60)

# Forma tradicional
cuadrados = []
for x in range(5):
    cuadrados.append(x ** 2)
print(f"Tradicional: {cuadrados}")

# List comprehension
cuadrados = [x ** 2 for x in range(5)]
print(f"Comprehension: {cuadrados}")

# Con condición
pares = [x for x in range(10) if x % 2 == 0]
print(f"Pares: {pares}")

print("\n(Más detalles en 12_comprehensions.py)")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Eliminar duplicados (manteniendo orden)
print("--- Eliminar duplicados ---")
def eliminar_duplicados(lista):
    vistos = []
    for item in lista:
        if item not in vistos:
            vistos.append(item)
    return vistos

original = [1, 2, 2, 3, 1, 4, 2, 5]
sin_dup = eliminar_duplicados(original)
print(f"  {original} → {sin_dup}")

# 2. Aplanar lista anidada
print("\n--- Aplanar lista ---")
def aplanar(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(aplanar(item))
        else:
            resultado.append(item)
    return resultado

anidada = [1, [2, 3], [4, [5, 6]]]
plana = aplanar(anidada)
print(f"  {anidada} → {plana}")

# 3. Rotar lista
print("\n--- Rotar lista ---")
def rotar(lista, n):
    n = n % len(lista)  # Manejar n > len(lista)
    return lista[n:] + lista[:n]

original = [1, 2, 3, 4, 5]
rotada = rotar(original, 2)
print(f"  Rotar {original} por 2: {rotada}")

# 4. Encontrar elemento más frecuente
print("\n--- Elemento más frecuente ---")
def mas_frecuente(lista):
    contador = {}
    for item in lista:
        contador[item] = contador.get(item, 0) + 1
    return max(contador, key=contador.get)

numeros = [1, 2, 2, 3, 3, 3, 4]
print(f"  Más frecuente en {numeros}: {mas_frecuente(numeros)}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Escribe una función que reciba dos listas y retorne
   una lista con los elementos comunes (intersección)

2. Crea una función que reciba una lista de números
   y retorne una lista con solo los números positivos

3. Escribe una función que mueva todos los ceros de
   una lista al final, manteniendo el orden de los demás
   Ej: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

4. Crea una función que reciba una lista de palabras
   y retorne la palabra más larga

5. Escribe una función que divida una lista en grupos
   de n elementos
   Ej: [1,2,3,4,5,6,7], n=3 → [[1,2,3], [4,5,6], [7]]

6. Crea una función que verifique si una lista es
   palíndromo (igual al derecho y al revés)
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 08_tuplas_sets.py")
print("=" * 60)
