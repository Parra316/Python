"""
================================================================================
STRINGS (CADENAS DE TEXTO)
================================================================================

Los strings son secuencias inmutables de caracteres.
Son uno de los tipos de datos más usados en programación.

CARACTERÍSTICAS:
- Inmutables: no se pueden modificar después de crearse
- Indexables: accedes a caracteres por posición
- Iterables: puedes recorrerlos con bucles
- Muchos métodos útiles integrados

================================================================================
"""

# ==============================================================================
# CREAR STRINGS
# ==============================================================================

print("=" * 60)
print("CREAR STRINGS")
print("=" * 60)

# Comillas simples o dobles
simple = 'Hola con comillas simples'
doble = "Hola con comillas dobles"

# Útil para incluir comillas
frase1 = "Él dijo 'Hola'"
frase2 = 'Ella respondió "Adiós"'

print(simple)
print(doble)
print(frase1)
print(frase2)

# Strings multilínea
multilinea = """Esta es una cadena
que ocupa varias líneas.
Muy útil para texto largo."""
print(f"\nMultilínea:\n{multilinea}")

# String vacío
vacio = ""
print(f"\nString vacío: '{vacio}', longitud: {len(vacio)}")


# ==============================================================================
# CARACTERES ESPECIALES (ESCAPE)
# ==============================================================================

print("\n" + "=" * 60)
print("CARACTERES ESPECIALES")
print("=" * 60)

print("""
Secuencias de escape:
\\n  → Nueva línea
\\t  → Tabulador
\\\\  → Backslash
\\'  → Comilla simple
\\"  → Comilla doble
\\r  → Retorno de carro
""")

# Ejemplos
print("Primera línea\nSegunda línea")
print("Columna1\tColumna2\tColumna3")
print("Ruta: C:\\Users\\nombre\\archivo.txt")

# Raw strings (ignora escapes)
print("\n--- Raw strings (r'...') ---")
print(r"En raw string \n no es nueva línea")
print(r"Útil para: C:\ruta\nueva\archivo")


# ==============================================================================
# INDEXACIÓN Y SLICING
# ==============================================================================

print("\n" + "=" * 60)
print("INDEXACIÓN Y SLICING")
print("=" * 60)

texto = "Python"
print(f"texto = '{texto}'")
print(f"Longitud: {len(texto)}")

# Índices (empiezan en 0)
print("""
Índices positivos:  P  y  t  h  o  n
                    0  1  2  3  4  5

Índices negativos:  P  y  t  h  o  n
                   -6 -5 -4 -3 -2 -1
""")

print(f"texto[0] = '{texto[0]}'")    # Primer carácter
print(f"texto[-1] = '{texto[-1]}'")  # Último carácter
print(f"texto[2] = '{texto[2]}'")    # Tercer carácter

# Slicing: texto[inicio:fin:paso]
print("\n--- Slicing ---")
print(f"texto[0:3] = '{texto[0:3]}'")    # 'Pyt' (del 0 al 2)
print(f"texto[:3] = '{texto[:3]}'")      # 'Pyt' (desde el inicio)
print(f"texto[3:] = '{texto[3:]}'")      # 'hon' (hasta el final)
print(f"texto[::2] = '{texto[::2]}'")    # 'Pto' (cada 2 caracteres)
print(f"texto[::-1] = '{texto[::-1]}'")  # 'nohtyP' (invertido)

# Más ejemplos
palabra = "Programación"
print(f"\npalabra = '{palabra}'")
print(f"Primeras 4 letras: '{palabra[:4]}'")
print(f"Últimas 4 letras: '{palabra[-4:]}'")
print(f"Sin primera y última: '{palabra[1:-1]}'")


# ==============================================================================
# MÉTODOS DE STRINGS
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS DE STRINGS")
print("=" * 60)

# --- Cambiar mayúsculas/minúsculas ---
print("--- Mayúsculas/Minúsculas ---")
texto = "Hola Mundo"
print(f"Original: '{texto}'")
print(f".upper(): '{texto.upper()}'")
print(f".lower(): '{texto.lower()}'")
print(f".capitalize(): '{texto.capitalize()}'")
print(f".title(): '{'hola mundo'.title()}'")
print(f".swapcase(): '{texto.swapcase()}'")

# --- Buscar y reemplazar ---
print("\n--- Buscar y reemplazar ---")
frase = "Python es genial, Python es fácil"
print(f"Frase: '{frase}'")
print(f".find('es'): {frase.find('es')}")  # Índice de primera aparición
print(f".rfind('es'): {frase.rfind('es')}")  # Última aparición
print(f".count('Python'): {frase.count('Python')}")
print(f".replace('Python', 'Java'): '{frase.replace('Python', 'Java')}'")

# --- Verificaciones (retornan bool) ---
print("\n--- Verificaciones ---")
print(f"'Python'.startswith('Py'): {'Python'.startswith('Py')}")
print(f"'Python'.endswith('on'): {'Python'.endswith('on')}")
print(f"'Python' in frase: {'Python' in frase}")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'HOLA'.isupper(): {'HOLA'.isupper()}")
print(f"'hola'.islower(): {'hola'.islower()}")

# --- Limpiar espacios ---
print("\n--- Limpiar espacios ---")
con_espacios = "   Hola Mundo   "
print(f"Original: '{con_espacios}'")
print(f".strip(): '{con_espacios.strip()}'")
print(f".lstrip(): '{con_espacios.lstrip()}'")
print(f".rstrip(): '{con_espacios.rstrip()}'")

# --- Split y Join ---
print("\n--- Split y Join ---")
oracion = "Python es un lenguaje de programación"
palabras = oracion.split()  # Divide por espacios
print(f"Oración: '{oracion}'")
print(f".split(): {palabras}")

csv = "manzana,naranja,plátano"
frutas = csv.split(',')  # Divide por comas
print(f"\nCSV: '{csv}'")
print(f".split(','): {frutas}")

# Join: une una lista en un string
print(f"\n'-'.join(frutas): '{'-'.join(frutas)}'")
print(f"' | '.join(frutas): '{' | '.join(frutas)}'")

# --- Alinear texto ---
print("\n--- Alinear texto ---")
texto = "Python"
print(f"'{texto}'.center(20): '{texto.center(20)}'")
print(f"'{texto}'.ljust(20): '{texto.ljust(20)}'")
print(f"'{texto}'.rjust(20): '{texto.rjust(20)}'")
print(f"'{texto}'.zfill(10): '{texto.zfill(10)}'")


# ==============================================================================
# FORMATEO DE STRINGS
# ==============================================================================

print("\n" + "=" * 60)
print("FORMATEO DE STRINGS")
print("=" * 60)

nombre = "María"
edad = 28
altura = 1.65

# 1. f-strings (Python 3.6+) - RECOMENDADO
print("--- f-strings (recomendado) ---")
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}")

# Expresiones dentro de f-strings
print(f"Edad en 10 años: {edad + 10}")
print(f"Nombre en mayúsculas: {nombre.upper()}")

# Formato de números
pi = 3.14159265359
print(f"\nFormato de números:")
print(f"Pi con 2 decimales: {pi:.2f}")
print(f"Pi con 4 decimales: {pi:.4f}")
print(f"Número grande: {1000000:,}")  # Con separador de miles
print(f"Porcentaje: {0.85:.1%}")
print(f"Binario: {255:b}")
print(f"Hexadecimal: {255:x}")

# Alineación en f-strings
print(f"\nAlineación:")
print(f"{'Izquierda':<20}|")
print(f"{'Centro':^20}|")
print(f"{'Derecha':>20}|")

# 2. Método .format()
print("\n--- .format() ---")
print("Nombre: {}, Edad: {}".format(nombre, edad))
print("Nombre: {n}, Edad: {e}".format(n=nombre, e=edad))
print("{0} tiene {1} años, {0} es genial".format(nombre, edad))

# 3. Operador % (estilo antiguo)
print("\n--- Operador % (estilo antiguo) ---")
print("Nombre: %s, Edad: %d" % (nombre, edad))
print("Pi: %.2f" % pi)


# ==============================================================================
# STRINGS SON INMUTABLES
# ==============================================================================

print("\n" + "=" * 60)
print("STRINGS SON INMUTABLES")
print("=" * 60)

print("""
Los strings NO se pueden modificar directamente.
texto[0] = 'X'  # ¡Error!

Para "modificar", creas un nuevo string:
""")

original = "Hola"
# original[0] = 'J'  # TypeError!

# Crear nuevo string
nuevo = 'J' + original[1:]
print(f"Original: '{original}'")
print(f"Nuevo: '{nuevo}'")

# Usando replace
otro = original.replace('H', 'J')
print(f"Con replace: '{otro}'")


# ==============================================================================
# OPERACIONES CON STRINGS
# ==============================================================================

print("\n" + "=" * 60)
print("OPERACIONES CON STRINGS")
print("=" * 60)

# Concatenación
print("--- Concatenación ---")
saludo = "Hola" + " " + "Mundo"
print(f"'Hola' + ' ' + 'Mundo' = '{saludo}'")

# Repetición
print("\n--- Repetición ---")
linea = "-" * 20
print(f"'-' * 20 = '{linea}'")
eco = "eco " * 3
print(f"'eco ' * 3 = '{eco}'")

# Iterar sobre string
print("\n--- Iterar ---")
for i, char in enumerate("Hola"):
    print(f"  Índice {i}: '{char}'")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Validar email (muy básico)
def validar_email_simple(email):
    return "@" in email and "." in email.split("@")[-1]

print("--- Validar email (básico) ---")
emails = ["usuario@gmail.com", "invalido@", "test@dominio.org"]
for email in emails:
    valido = validar_email_simple(email)
    print(f"  '{email}': {'✓' if valido else '✗'}")

# 2. Contar vocales
def contar_vocales(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for char in texto if char in vocales)

print("\n--- Contar vocales ---")
frase = "Hola Mundo"
print(f"  '{frase}' tiene {contar_vocales(frase)} vocales")

# 3. Palíndromo
def es_palindromo(texto):
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]

print("\n--- Verificar palíndromo ---")
palabras = ["radar", "hola", "Anita lava la tina"]
for p in palabras:
    result = es_palindromo(p)
    print(f"  '{p}': {'✓ palíndromo' if result else '✗'}")

# 4. Título de caso
def titulo_caso(texto):
    excepciones = {'de', 'la', 'el', 'en', 'y', 'a'}
    palabras = texto.lower().split()
    resultado = [palabras[0].capitalize()]
    resultado += [p if p in excepciones else p.capitalize() for p in palabras[1:]]
    return ' '.join(resultado)

print("\n--- Título de caso ---")
print(f"  '{titulo_caso('el señor de los anillos')}'")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Dado el string "Python Programming":
   - Extrae "Python"
   - Extrae "Programming"
   - Invierte el string completo
   - Cuenta cuántas 'g' hay

2. Escribe una función que:
   - Reciba una oración
   - Retorne la palabra más larga

3. Escribe una función que:
   - Reciba un string
   - Retorne True si tiene más vocales que consonantes

4. Formatea los siguientes datos como tabla:
   productos = [("Manzana", 2.50), ("Naranja", 1.80), ("Plátano", 0.99)]
   Salida esperada:
   | Producto  | Precio |
   | Manzana   | $2.50  |
   | Naranja   | $1.80  |
   | Plátano   | $0.99  |

5. Crea una función que convierta "hola_mundo" a "holaMundo"
   (snake_case a camelCase)
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 05_estructuras_control.py")
print("=" * 60)
