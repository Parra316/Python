"""
================================================================================
OPERADORES EN PYTHON
================================================================================

Los operadores son símbolos que realizan operaciones sobre valores.

TIPOS DE OPERADORES:
1. Aritméticos: +, -, *, /, //, %, **
2. De comparación: ==, !=, <, >, <=, >=
3. Lógicos: and, or, not
4. De asignación: =, +=, -=, *=, etc.
5. De identidad: is, is not
6. De pertenencia: in, not in
7. Bit a bit: &, |, ^, ~, <<, >>

================================================================================
"""

# ==============================================================================
# OPERADORES ARITMÉTICOS
# ==============================================================================

print("=" * 60)
print("OPERADORES ARITMÉTICOS")
print("=" * 60)

a = 17
b = 5

print(f"a = {a}, b = {b}\n")

print(f"Suma:          a + b  = {a + b}")
print(f"Resta:         a - b  = {a - b}")
print(f"Multiplicación: a * b  = {a * b}")
print(f"División:       a / b  = {a / b}")      # Siempre retorna float
print(f"División entera: a // b = {a // b}")    # Trunca la parte decimal
print(f"Módulo (resto): a % b  = {a % b}")      # Resto de la división
print(f"Potencia:       a ** b = {a ** b}")     # a elevado a b

# Casos especiales
print("\n--- Casos especiales ---")
print(f"División negativa: -17 // 5 = {-17 // 5}")  # Redondea hacia abajo
print(f"Módulo negativo: -17 % 5 = {-17 % 5}")
print(f"Raíz cuadrada: 16 ** 0.5 = {16 ** 0.5}")
print(f"Raíz cúbica: 27 ** (1/3) = {27 ** (1/3):.2f}")


# ==============================================================================
# PRECEDENCIA DE OPERADORES
# ==============================================================================

print("\n" + "=" * 60)
print("PRECEDENCIA DE OPERADORES")
print("=" * 60)

print("""
Orden de precedencia (de mayor a menor):
1. ()       Paréntesis
2. **       Potencia
3. +x, -x   Positivo, negativo unario
4. *, /, //, %  Multiplicación, división
5. +, -     Suma, resta
6. Comparaciones
7. not
8. and
9. or
""")

# Ejemplos
print("Ejemplos:")
print(f"  2 + 3 * 4 = {2 + 3 * 4}")          # 14, no 20
print(f"  (2 + 3) * 4 = {(2 + 3) * 4}")      # 20
print(f"  2 ** 3 ** 2 = {2 ** 3 ** 2}")      # 512 (derecha a izquierda)
print(f"  (2 ** 3) ** 2 = {(2 ** 3) ** 2}")  # 64
print(f"  10 - 5 - 2 = {10 - 5 - 2}")        # 3 (izquierda a derecha)


# ==============================================================================
# OPERADORES DE COMPARACIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("OPERADORES DE COMPARACIÓN")
print("=" * 60)

x = 10
y = 5

print(f"x = {x}, y = {y}\n")

print(f"Igual:           x == y  → {x == y}")
print(f"Diferente:       x != y  → {x != y}")
print(f"Mayor que:       x > y   → {x > y}")
print(f"Menor que:       x < y   → {x < y}")
print(f"Mayor o igual:   x >= y  → {x >= y}")
print(f"Menor o igual:   x <= y  → {x <= y}")

# Comparaciones encadenadas (muy pythónico)
print("\n--- Comparaciones encadenadas ---")
edad = 25
print(f"edad = {edad}")
print(f"18 <= edad <= 65: {18 <= edad <= 65}")  # ¡Muy elegante!
print(f"0 < 5 < 10: {0 < 5 < 10}")

# Comparación de strings (orden lexicográfico)
print("\n--- Comparación de strings ---")
print(f"'apple' < 'banana': {'apple' < 'banana'}")
print(f"'ABC' < 'abc': {'ABC' < 'abc'}")  # Mayúsculas primero


# ==============================================================================
# OPERADORES LÓGICOS
# ==============================================================================

print("\n" + "=" * 60)
print("OPERADORES LÓGICOS")
print("=" * 60)

print("""
Tabla de verdad:

and (Y):           or (O):            not (NO):
A     B    A and B | A     B    A or B | A     not A
True  True  True   | True  True  True  | True  False
True  False False  | True  False True  | False True
False True  False  | False True  True  |
False False False  | False False False |
""")

a = True
b = False

print(f"a = {a}, b = {b}\n")
print(f"a and b = {a and b}")
print(f"a or b = {a or b}")
print(f"not a = {not a}")
print(f"not b = {not b}")

# Ejemplo práctico
print("\n--- Ejemplo práctico ---")
edad = 25
tiene_licencia = True
tiene_auto = False

puede_conducir = edad >= 18 and tiene_licencia
print(f"¿Puede conducir? {puede_conducir}")

puede_viajar = tiene_licencia or tiene_auto
print(f"¿Puede viajar en auto? {puede_viajar}")

# Short-circuit evaluation (evaluación de cortocircuito)
print("\n--- Evaluación de cortocircuito ---")
print("""
Python no evalúa el segundo operando si no es necesario:
- False and X → False (sin evaluar X)
- True or X → True (sin evaluar X)
""")


# ==============================================================================
# OPERADORES DE ASIGNACIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("OPERADORES DE ASIGNACIÓN")
print("=" * 60)

x = 10
print(f"x inicial = {x}")

x += 5   # x = x + 5
print(f"x += 5  → x = {x}")

x -= 3   # x = x - 3
print(f"x -= 3  → x = {x}")

x *= 2   # x = x * 2
print(f"x *= 2  → x = {x}")

x /= 4   # x = x / 4
print(f"x /= 4  → x = {x}")

x //= 2  # x = x // 2
print(f"x //= 2 → x = {x}")

x **= 3  # x = x ** 3
print(f"x **= 3 → x = {x}")

x %= 5   # x = x % 5
print(f"x %= 5  → x = {x}")

# Operador morsa (Python 3.8+)
print("\n--- Operador morsa := (Python 3.8+) ---")
print("Permite asignar y usar en la misma expresión")

# Sin operador morsa:
# n = len("Hola")
# if n > 3:
#     print(f"Largo: {n}")

# Con operador morsa:
if (n := len("Hola")) > 3:
    print(f"Largo: {n}")


# ==============================================================================
# OPERADORES DE IDENTIDAD
# ==============================================================================

print("\n" + "=" * 60)
print("OPERADORES DE IDENTIDAD")
print("=" * 60)

print("""
'is' compara si dos variables apuntan al MISMO objeto en memoria.
'==' compara si dos valores son IGUALES.
""")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")

print(f"\na == b: {a == b}")  # True, mismo contenido
print(f"a is b: {a is b}")    # False, diferentes objetos
print(f"a is c: {a is c}")    # True, mismo objeto

# Con None siempre usar 'is'
valor = None
print(f"\nvalor is None: {valor is None}")  # Forma correcta
print(f"valor == None: {valor == None}")    # Funciona pero no recomendado

# Curiosidad con enteros pequeños
print("\n--- Curiosidad: Integer caching ---")
x = 5
y = 5
print(f"x = 5, y = 5")
print(f"x is y: {x is y}")  # True, Python cachea enteros pequeños (-5 a 256)

x = 1000
y = 1000
print(f"\nx = 1000, y = 1000")
print(f"x is y: {x is y}")  # Puede ser False


# ==============================================================================
# OPERADORES DE PERTENENCIA
# ==============================================================================

print("\n" + "=" * 60)
print("OPERADORES DE PERTENENCIA")
print("=" * 60)

# En listas
lista = [1, 2, 3, 4, 5]
print(f"lista = {lista}")
print(f"3 in lista: {3 in lista}")
print(f"6 in lista: {6 in lista}")
print(f"6 not in lista: {6 not in lista}")

# En strings
texto = "Hola mundo"
print(f"\ntexto = '{texto}'")
print(f"'mundo' in texto: {'mundo' in texto}")
print(f"'Python' in texto: {'Python' in texto}")

# En diccionarios (busca en las claves)
datos = {"nombre": "Juan", "edad": 30}
print(f"\ndatos = {datos}")
print(f"'nombre' in datos: {'nombre' in datos}")
print(f"'Juan' in datos: {'Juan' in datos}")  # False, es un valor no una clave
print(f"'Juan' in datos.values(): {'Juan' in datos.values()}")


# ==============================================================================
# OPERADORES BIT A BIT (BITWISE)
# ==============================================================================

print("\n" + "=" * 60)
print("OPERADORES BIT A BIT")
print("=" * 60)

print("""
Operan sobre la representación binaria de los números.
Útiles para: flags, máscaras, optimizaciones, criptografía.
""")

a = 12  # 1100 en binario
b = 7   # 0111 en binario

print(f"a = {a} ({bin(a)})")
print(f"b = {b} ({bin(b)})")

print(f"\na & b  (AND): {a & b} ({bin(a & b)})")    # 0100 = 4
print(f"a | b  (OR):  {a | b} ({bin(a | b)})")      # 1111 = 15
print(f"a ^ b  (XOR): {a ^ b} ({bin(a ^ b)})")      # 1011 = 11
print(f"~a     (NOT): {~a}")                        # -13 (complemento a 2)
print(f"a << 2 (shift izq): {a << 2} ({bin(a << 2)})")  # Multiplicar por 4
print(f"a >> 2 (shift der): {a >> 2} ({bin(a >> 2)})")  # Dividir por 4

# Uso práctico: Verificar si un número es par
print("\n--- Truco: Verificar par/impar ---")
for n in range(5):
    es_par = (n & 1) == 0
    print(f"  {n} es {'par' if es_par else 'impar'}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. ¿Cuál es el resultado de?
   - 15 // 4
   - 15 % 4
   - 2 ** 3 ** 2
   - not (True and False)

2. Sin ejecutar, ¿qué imprime?
   x = 5
   y = 10
   print(x < y and y < 20)
   print(x > y or y == 10)

3. Escribe una expresión que sea True si:
   - Un número está entre 1 y 100 (inclusive)
   - Una persona puede votar (edad >= 18)
   - Un año es bisiesto (divisible por 4, excepto si
     es divisible por 100, excepto si es divisible por 400)

4. ¿Cuál es la diferencia entre '==' e 'is'?
   ¿Cuándo usar cada uno?
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 04_strings.py")
print("=" * 60)
