"""
================================================================================
BUCLES (LOOPS)
================================================================================

Los bucles permiten repetir un bloque de código múltiples veces.

TIPOS DE BUCLES EN PYTHON:
1. for - Itera sobre una secuencia
2. while - Repite mientras una condición sea True

PALABRAS CLAVE:
- break: Sale del bucle inmediatamente
- continue: Salta a la siguiente iteración
- else: Se ejecuta si el bucle termina normalmente (sin break)

================================================================================
"""

# ==============================================================================
# BUCLE FOR
# ==============================================================================

print("=" * 60)
print("BUCLE FOR")
print("=" * 60)

print("""
Sintaxis:
    for variable in iterable:
        # código a repetir

El 'iterable' puede ser: lista, string, range, diccionario, etc.
""")

# Iterar sobre lista
print("--- Iterar sobre lista ---")
frutas = ["manzana", "naranja", "plátano"]
for fruta in frutas:
    print(f"  Me gusta la {fruta}")

# Iterar sobre string
print("\n--- Iterar sobre string ---")
for letra in "Python":
    print(f"  {letra}")

# Iterar sobre range
print("\n--- Iterar con range() ---")
print("range(5): ", end="")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")

print("\nrange(2, 8): ", end="")
for i in range(2, 8):  # 2, 3, 4, 5, 6, 7
    print(i, end=" ")

print("\nrange(0, 10, 2): ", end="")
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i, end=" ")

print("\nrange(10, 0, -1): ", end="")
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i, end=" ")
print()


# ==============================================================================
# ENUMERATE Y ZIP
# ==============================================================================

print("\n" + "=" * 60)
print("ENUMERATE Y ZIP")
print("=" * 60)

# enumerate - obtener índice y valor
print("--- enumerate() ---")
nombres = ["Ana", "Luis", "María"]
for indice, nombre in enumerate(nombres):
    print(f"  {indice}: {nombre}")

# Empezar desde otro número
print("\n  Empezando desde 1:")
for num, nombre in enumerate(nombres, start=1):
    print(f"  {num}. {nombre}")

# zip - combinar múltiples listas
print("\n--- zip() ---")
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Sevilla"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre} tiene {edad} años y vive en {ciudad}")


# ==============================================================================
# BUCLE WHILE
# ==============================================================================

print("\n" + "=" * 60)
print("BUCLE WHILE")
print("=" * 60)

print("""
Sintaxis:
    while condición:
        # código a repetir

Se repite MIENTRAS la condición sea True.
¡Cuidado con bucles infinitos!
""")

# Ejemplo básico
print("--- Contador ---")
contador = 0
while contador < 5:
    print(f"  Contador: {contador}")
    contador += 1

# Con entrada de usuario (simulada)
print("\n--- Simulación de menú ---")
opciones = ["1", "2", "3", "salir"]
for opcion in opciones:
    print(f"  Opción: {opcion}")
    if opcion == "salir":
        print("  ¡Adiós!")
        break


# ==============================================================================
# BREAK Y CONTINUE
# ==============================================================================

print("\n" + "=" * 60)
print("BREAK Y CONTINUE")
print("=" * 60)

# break - salir del bucle
print("--- break ---")
print("Buscando el número 5:")
for i in range(10):
    if i == 5:
        print(f"  ¡Encontrado! Saliendo del bucle")
        break
    print(f"  {i}...")

# continue - saltar a la siguiente iteración
print("\n--- continue ---")
print("Números impares del 0 al 9:")
for i in range(10):
    if i % 2 == 0:  # Si es par, saltar
        continue
    print(f"  {i}")


# ==============================================================================
# ELSE EN BUCLES
# ==============================================================================

print("\n" + "=" * 60)
print("ELSE EN BUCLES")
print("=" * 60)

print("""
El 'else' en un bucle se ejecuta SOLO si el bucle
termina normalmente (sin break).
""")

# else con for
print("--- Buscar en lista (no encontrado) ---")
numeros = [1, 3, 5, 7, 9]
buscar = 4

for n in numeros:
    if n == buscar:
        print(f"  ¡{buscar} encontrado!")
        break
else:
    print(f"  {buscar} no está en la lista")

# else con for (encontrado)
print("\n--- Buscar en lista (encontrado) ---")
buscar = 5
for n in numeros:
    if n == buscar:
        print(f"  ¡{buscar} encontrado!")
        break
else:
    print(f"  {buscar} no está en la lista")

# Uso práctico: verificar número primo
print("\n--- Verificar número primo ---")
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Tiene divisor, no es primo
    else:
        return True  # No encontró divisores

for num in [7, 10, 13, 15, 17]:
    print(f"  {num}: {'primo' if es_primo(num) else 'no primo'}")


# ==============================================================================
# BUCLES ANIDADOS
# ==============================================================================

print("\n" + "=" * 60)
print("BUCLES ANIDADOS")
print("=" * 60)

# Tabla de multiplicar
print("--- Tabla de multiplicar (parcial) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i*j}")
    print()

# Matriz
print("--- Recorrer matriz ---")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(f"{elemento:3}", end="")
    print()

# Con índices
print("\n--- Con índices ---")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"  [{i}][{j}] = {matriz[i][j]}")


# ==============================================================================
# PATRONES COMUNES
# ==============================================================================

print("\n" + "=" * 60)
print("PATRONES COMUNES")
print("=" * 60)

# Sumar elementos
print("--- Sumar elementos ---")
numeros = [1, 2, 3, 4, 5]
suma = 0
for n in numeros:
    suma += n
print(f"  Suma de {numeros}: {suma}")
print(f"  Con sum(): {sum(numeros)}")  # Forma pythónica

# Encontrar máximo
print("\n--- Encontrar máximo ---")
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
maximo = numeros[0]
for n in numeros:
    if n > maximo:
        maximo = n
print(f"  Máximo de {numeros}: {maximo}")
print(f"  Con max(): {max(numeros)}")  # Forma pythónica

# Filtrar elementos
print("\n--- Filtrar pares ---")
numeros = range(10)
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(f"  Pares: {pares}")

# Contar elementos
print("\n--- Contar vocales ---")
texto = "Hola Mundo"
contador = 0
for letra in texto.lower():
    if letra in "aeiou":
        contador += 1
print(f"  '{texto}' tiene {contador} vocales")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. FizzBuzz
print("--- FizzBuzz (1-15) ---")
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("  FizzBuzz")
    elif i % 3 == 0:
        print("  Fizz")
    elif i % 5 == 0:
        print("  Buzz")
    else:
        print(f"  {i}")

# 2. Factorial
print("\n--- Factorial ---")
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

for n in [5, 7, 10]:
    print(f"  {n}! = {factorial(n)}")

# 3. Fibonacci
print("\n--- Fibonacci (primeros 10) ---")
a, b = 0, 1
fibonacci = []
for _ in range(10):
    fibonacci.append(a)
    a, b = b, a + b
print(f"  {fibonacci}")

# 4. Validar entrada
print("\n--- Validar entrada (simulación) ---")
intentos_maximos = 3
passwords_prueba = ["abc", "123", "admin123"]

for intento, password in enumerate(passwords_prueba, 1):
    print(f"  Intento {intento}: '{password}'")
    if password == "admin123":
        print("  ¡Acceso concedido!")
        break
    if intento >= intentos_maximos:
        print("  Demasiados intentos fallidos")
        break
else:
    print("  Nunca se llegó aquí porque hubo break")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Escribe un programa que imprima los números del 1 al 100
   que sean divisibles por 3 pero no por 5

2. Crea un programa que encuentre todos los números primos
   entre 1 y 50

3. Escribe un programa que calcule la suma de los dígitos
   de un número (ej: 12345 → 1+2+3+4+5 = 15)

4. Crea un programa que imprima el siguiente patrón:
   *
   **
   ***
   ****
   *****

5. Escribe un programa que encuentre el segundo número
   más grande en una lista (sin usar sort ni max)

6. Crea un juego de adivinanza donde el usuario tiene
   que adivinar un número entre 1 y 100 en máximo 7 intentos
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 07_listas.py")
print("=" * 60)
