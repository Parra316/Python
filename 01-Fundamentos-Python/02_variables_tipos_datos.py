"""
================================================================================
VARIABLES Y TIPOS DE DATOS
================================================================================

¿QUÉ ES UNA VARIABLE?
--------------------
Una variable es un "contenedor" que almacena un valor en memoria.
Es como una caja etiquetada donde guardas información.

    nombre = "Juan"    # La caja "nombre" contiene "Juan"
    edad = 25          # La caja "edad" contiene 25

REGLAS PARA NOMBRES DE VARIABLES:
--------------------------------
✓ Pueden contener letras, números y guion bajo
✓ Deben empezar con letra o guion bajo
✓ Son case-sensitive (edad ≠ Edad ≠ EDAD)
✗ NO pueden empezar con número
✗ NO pueden ser palabras reservadas (if, for, while, etc.)

CONVENCIONES:
- snake_case para variables y funciones: mi_variable
- MAYUSCULAS para constantes: PI = 3.14159
- CamelCase para clases: MiClase

================================================================================
"""

# ==============================================================================
# ASIGNACIÓN DE VARIABLES
# ==============================================================================

print("=" * 60)
print("ASIGNACIÓN DE VARIABLES")
print("=" * 60)

# Asignación simple
nombre = "María"
edad = 30
altura = 1.65
es_estudiante = True

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"¿Es estudiante?: {es_estudiante}")

# Asignación múltiple (mismo valor)
x = y = z = 0
print(f"\nx, y, z = {x}, {y}, {z}")

# Asignación múltiple (diferentes valores)
a, b, c = 1, 2, 3
print(f"a, b, c = {a}, {b}, {c}")

# Intercambiar valores (muy elegante en Python)
a, b = b, a
print(f"Después de intercambiar: a={a}, b={b}")

# Reasignar variables
contador = 10
print(f"\nContador inicial: {contador}")
contador = contador + 1  # Incrementar
print(f"Después de +1: {contador}")
contador += 5  # Forma abreviada
print(f"Después de +=5: {contador}")


# ==============================================================================
# TIPOS DE DATOS BÁSICOS
# ==============================================================================

print("\n" + "=" * 60)
print("TIPOS DE DATOS BÁSICOS")
print("=" * 60)

# ------------------------------
# 1. ENTEROS (int)
# ------------------------------
print("\n--- ENTEROS (int) ---")
entero_positivo = 42
entero_negativo = -17
entero_grande = 1_000_000  # Guion bajo para legibilidad

print(f"Entero positivo: {entero_positivo}")
print(f"Entero negativo: {entero_negativo}")
print(f"Entero grande: {entero_grande}")
print(f"Tipo: {type(entero_positivo)}")

# Python maneja enteros arbitrariamente grandes
numero_enorme = 10 ** 100
print(f"10^100 tiene {len(str(numero_enorme))} dígitos")

# ------------------------------
# 2. FLOTANTES (float)
# ------------------------------
print("\n--- FLOTANTES (float) ---")
decimal = 3.14159
negativo_decimal = -2.5
notacion_cientifica = 1.5e6  # 1.5 × 10^6 = 1,500,000

print(f"Pi aproximado: {decimal}")
print(f"Negativo decimal: {negativo_decimal}")
print(f"Notación científica: {notacion_cientifica}")
print(f"Tipo: {type(decimal)}")

# Cuidado con la precisión de flotantes
print(f"\n0.1 + 0.2 = {0.1 + 0.2}")  # ¡No es exactamente 0.3!
print("(Esto es normal en todos los lenguajes)")

# ------------------------------
# 3. STRINGS (str)
# ------------------------------
print("\n--- STRINGS (str) ---")
cadena_simple = 'Hola con comillas simples'
cadena_doble = "Hola con comillas dobles"
cadena_multilinea = """Esta es una
cadena que ocupa
múltiples líneas"""

print(cadena_simple)
print(cadena_doble)
print(f"Multilínea:\n{cadena_multilinea}")
print(f"Tipo: {type(cadena_simple)}")

# Caracteres especiales
print("\nCaracteres especiales:")
print("Tabulador:\tTexto después del tab")
print("Salto de línea: Primera línea\nSegunda línea")
print("Comilla en string: Él dijo \"Hola\"")
print("Backslash: C:\\Users\\nombre")

# ------------------------------
# 4. BOOLEANOS (bool)
# ------------------------------
print("\n--- BOOLEANOS (bool) ---")
verdadero = True
falso = False

print(f"Verdadero: {verdadero}")
print(f"Falso: {falso}")
print(f"Tipo: {type(verdadero)}")

# Valores que se evalúan como False
print("\nValores 'falsy' (se evalúan como False):")
print(f"  bool(0) = {bool(0)}")
print(f"  bool('') = {bool('')}")  # String vacío
print(f"  bool([]) = {bool([])}")  # Lista vacía
print(f"  bool(None) = {bool(None)}")

# Valores que se evalúan como True
print("\nValores 'truthy' (se evalúan como True):")
print(f"  bool(1) = {bool(1)}")
print(f"  bool(-1) = {bool(-1)}")  # Cualquier número no-cero
print(f"  bool('Hola') = {bool('Hola')}")  # String no vacío

# ------------------------------
# 5. NONE (ausencia de valor)
# ------------------------------
print("\n--- NONE (NoneType) ---")
sin_valor = None
print(f"Variable sin valor: {sin_valor}")
print(f"Tipo: {type(sin_valor)}")
print(f"¿Es None?: {sin_valor is None}")


# ==============================================================================
# FUNCIÓN type() - CONOCER EL TIPO
# ==============================================================================

print("\n" + "=" * 60)
print("FUNCIÓN type()")
print("=" * 60)

valores = [42, 3.14, "texto", True, None, [1, 2, 3]]

print("Tipo de cada valor:")
for valor in valores:
    print(f"  {str(valor):15} → {type(valor).__name__}")


# ==============================================================================
# CONVERSIÓN DE TIPOS (CASTING)
# ==============================================================================

print("\n" + "=" * 60)
print("CONVERSIÓN DE TIPOS (CASTING)")
print("=" * 60)

# String a número
texto_numero = "123"
numero = int(texto_numero)
print(f"'{texto_numero}' (str) → {numero} (int)")

texto_decimal = "3.14"
decimal = float(texto_decimal)
print(f"'{texto_decimal}' (str) → {decimal} (float)")

# Número a string
edad = 25
texto_edad = str(edad)
print(f"{edad} (int) → '{texto_edad}' (str)")

# Float a int (trunca, no redondea)
pi = 3.99
pi_entero = int(pi)
print(f"{pi} (float) → {pi_entero} (int) [truncado]")

# Redondear
print(f"round({pi}) = {round(pi)}")  # Redondea al entero más cercano
print(f"round({pi}, 1) = {round(pi, 1)}")  # 1 decimal

# Bool a número
print(f"\nint(True) = {int(True)}")   # 1
print(f"int(False) = {int(False)}")   # 0

# Conversión que falla
print("\n¿Qué pasa si intentamos convertir 'hola' a int?")
print("int('hola')  # ¡Esto daría ValueError!")


# ==============================================================================
# VERIFICAR TIPOS
# ==============================================================================

print("\n" + "=" * 60)
print("VERIFICAR TIPOS")
print("=" * 60)

valor = 42

# Usando type()
print(f"type({valor}) == int: {type(valor) == int}")

# Usando isinstance() (preferido, considera herencia)
print(f"isinstance({valor}, int): {isinstance(valor, int)}")
print(f"isinstance({valor}, (int, float)): {isinstance(valor, (int, float))}")

# Verificar si es numérico
def es_numerico(valor):
    return isinstance(valor, (int, float))

print(f"\nes_numerico(42) = {es_numerico(42)}")
print(f"es_numerico(3.14) = {es_numerico(3.14)}")
print(f"es_numerico('42') = {es_numerico('42')}")


# ==============================================================================
# CONSTANTES
# ==============================================================================

print("\n" + "=" * 60)
print("CONSTANTES")
print("=" * 60)

print("""
Python NO tiene constantes verdaderas.
Por convención, usamos MAYÚSCULAS para indicar
que un valor no debería modificarse.
""")

# Constantes por convención
PI = 3.14159265359
GRAVEDAD = 9.81
VELOCIDAD_LUZ = 299_792_458  # m/s
URL_API = "https://api.ejemplo.com"

print(f"PI = {PI}")
print(f"GRAVEDAD = {GRAVEDAD} m/s²")
print(f"VELOCIDAD_LUZ = {VELOCIDAD_LUZ:,} m/s")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea variables para almacenar:
   - Tu nombre (string)
   - Tu edad (int)
   - Tu altura en metros (float)
   - Si eres estudiante (bool)
   Imprime cada una con su tipo

2. Convierte:
   - El string "100" a entero
   - El flotante 9.8 a entero
   - El número 42 a string
   - El booleano True a int

3. ¿Cuál es el resultado de?
   - 10 / 3
   - 10 // 3
   - int(10 / 3)
   - round(10 / 3, 2)

4. Intercambia el valor de dos variables sin usar
   una variable temporal
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 03_operadores.py")
print("=" * 60)
