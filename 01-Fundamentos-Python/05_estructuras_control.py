"""
================================================================================
ESTRUCTURAS DE CONTROL
================================================================================

Las estructuras de control permiten tomar decisiones en el código.
Ejecutan diferentes bloques según condiciones.

ESTRUCTURAS EN PYTHON:
1. if, elif, else - Condicionales
2. match-case - Pattern matching (Python 3.10+)

================================================================================
"""

# ==============================================================================
# IF - CONDICIONAL BÁSICO
# ==============================================================================

print("=" * 60)
print("IF - CONDICIONAL BÁSICO")
print("=" * 60)

print("""
Sintaxis:
    if condición:
        # código si es True
    elif otra_condición:
        # código si la primera es False y esta es True
    else:
        # código si todas son False

IMPORTANTE: La indentación define el bloque
""")

# Ejemplo básico
edad = 20

if edad >= 18:
    print(f"Con {edad} años, eres mayor de edad")

# If-else
temperatura = 35

if temperatura > 30:
    print(f"Hace calor ({temperatura}°C)")
else:
    print(f"Temperatura agradable ({temperatura}°C)")


# ==============================================================================
# IF-ELIF-ELSE
# ==============================================================================

print("\n" + "=" * 60)
print("IF-ELIF-ELSE")
print("=" * 60)

nota = 85

print(f"Nota: {nota}")

if nota >= 90:
    calificacion = "A - Excelente"
elif nota >= 80:
    calificacion = "B - Muy bien"
elif nota >= 70:
    calificacion = "C - Bien"
elif nota >= 60:
    calificacion = "D - Suficiente"
else:
    calificacion = "F - Reprobado"

print(f"Calificación: {calificacion}")

# Múltiples elif
print("\n--- Clasificación de edad ---")
edad = 25

if edad < 0:
    etapa = "Edad inválida"
elif edad < 2:
    etapa = "Bebé"
elif edad < 12:
    etapa = "Niño"
elif edad < 18:
    etapa = "Adolescente"
elif edad < 65:
    etapa = "Adulto"
else:
    etapa = "Adulto mayor"

print(f"Edad {edad}: {etapa}")


# ==============================================================================
# CONDICIONES COMPUESTAS
# ==============================================================================

print("\n" + "=" * 60)
print("CONDICIONES COMPUESTAS")
print("=" * 60)

edad = 25
tiene_licencia = True
tiene_multas = False

# Usando 'and'
print("--- Usando 'and' ---")
if edad >= 18 and tiene_licencia:
    print("Puede conducir")

# Usando 'or'
print("\n--- Usando 'or' ---")
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Es fin de semana")

# Usando 'not'
print("\n--- Usando 'not' ---")
if not tiene_multas:
    print("Sin multas pendientes")

# Combinaciones
print("\n--- Combinación ---")
if edad >= 18 and tiene_licencia and not tiene_multas:
    print("Puede alquilar un auto")

# Comparaciones encadenadas
print("\n--- Comparaciones encadenadas ---")
valor = 50
if 0 <= valor <= 100:
    print(f"{valor} está entre 0 y 100")


# ==============================================================================
# IF ANIDADOS
# ==============================================================================

print("\n" + "=" * 60)
print("IF ANIDADOS")
print("=" * 60)

usuario = "admin"
password = "1234"
activo = True

print(f"Usuario: {usuario}, Activo: {activo}")

if usuario == "admin":
    if password == "1234":
        if activo:
            print("Acceso concedido")
        else:
            print("Cuenta desactivada")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")

# Mejor práctica: evitar anidación excesiva
print("\n--- Mejor: Reducir anidación ---")
if usuario != "admin":
    print("Usuario no encontrado")
elif password != "1234":
    print("Contraseña incorrecta")
elif not activo:
    print("Cuenta desactivada")
else:
    print("Acceso concedido")


# ==============================================================================
# OPERADOR TERNARIO
# ==============================================================================

print("\n" + "=" * 60)
print("OPERADOR TERNARIO")
print("=" * 60)

print("""
Sintaxis: valor_si_true if condición else valor_si_false

Es un if-else en una sola línea.
Útil para asignaciones simples.
""")

edad = 20

# Forma tradicional
if edad >= 18:
    estado = "adulto"
else:
    estado = "menor"

# Operador ternario (equivalente)
estado = "adulto" if edad >= 18 else "menor"
print(f"Edad {edad}: {estado}")

# Más ejemplos
numero = -5
signo = "positivo" if numero > 0 else "negativo" if numero < 0 else "cero"
print(f"Número {numero} es {signo}")

# En funciones
def valor_absoluto(n):
    return n if n >= 0 else -n

print(f"Valor absoluto de -7: {valor_absoluto(-7)}")


# ==============================================================================
# MATCH-CASE (Python 3.10+)
# ==============================================================================

print("\n" + "=" * 60)
print("MATCH-CASE (Python 3.10+)")
print("=" * 60)

print("""
Pattern matching estructural - Similar al switch de otros lenguajes,
pero mucho más poderoso.

Sintaxis:
    match variable:
        case patrón1:
            # código
        case patrón2:
            # código
        case _:
            # caso por defecto (wildcard)
""")

# Ejemplo básico
def describir_dia(dia):
    match dia:
        case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
            return "Día laboral"
        case "sábado" | "domingo":
            return "Fin de semana"
        case _:
            return "Día inválido"

print("--- Días de la semana ---")
for d in ["lunes", "sábado", "festivo"]:
    print(f"  {d}: {describir_dia(d)}")

# Pattern matching con valores
def describir_codigo_http(codigo):
    match codigo:
        case 200:
            return "OK"
        case 404:
            return "No encontrado"
        case 500:
            return "Error del servidor"
        case code if 200 <= code < 300:
            return f"Éxito ({code})"
        case code if 400 <= code < 500:
            return f"Error cliente ({code})"
        case _:
            return "Código desconocido"

print("\n--- Códigos HTTP ---")
for codigo in [200, 201, 404, 500, 403]:
    print(f"  {codigo}: {describir_codigo_http(codigo)}")

# Pattern matching con estructuras
def procesar_comando(comando):
    match comando.split():
        case ["salir"]:
            return "Saliendo..."
        case ["hola", nombre]:
            return f"¡Hola, {nombre}!"
        case ["sumar", x, y]:
            return f"Resultado: {int(x) + int(y)}"
        case ["repetir", texto, veces]:
            return texto * int(veces)
        case _:
            return "Comando no reconocido"

print("\n--- Procesamiento de comandos ---")
comandos = ["salir", "hola María", "sumar 5 3", "repetir eco 3", "invalid"]
for cmd in comandos:
    print(f"  '{cmd}' → {procesar_comando(cmd)}")


# ==============================================================================
# TRUTHY Y FALSY
# ==============================================================================

print("\n" + "=" * 60)
print("TRUTHY Y FALSY")
print("=" * 60)

print("""
En Python, cualquier valor puede evaluarse como booleano:

FALSY (se evalúan como False):
- False
- None
- 0, 0.0, 0j
- '', [], (), {}, set()
- Objetos con __bool__() que retorna False

TRUTHY (todo lo demás):
- True
- Números no-cero
- Strings, listas, etc. no vacíos
""")

# Ejemplos prácticos
print("--- Uso práctico ---")

lista = [1, 2, 3]
if lista:  # Más pythónico que: if len(lista) > 0
    print(f"Lista tiene elementos: {lista}")

nombre = ""
if not nombre:  # Más pythónico que: if nombre == ""
    print("Nombre está vacío")

resultado = None
if resultado is None:  # Usar 'is' para None
    print("Sin resultado")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Año bisiesto
def es_bisiesto(año):
    """Un año es bisiesto si:
    - Es divisible por 4, EXCEPTO
    - Si es divisible por 100, EXCEPTO
    - Si es divisible por 400
    """
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False

print("--- Años bisiestos ---")
for año in [2000, 2020, 2100, 2024]:
    print(f"  {año}: {'Bisiesto' if es_bisiesto(año) else 'No bisiesto'}")


# 2. Calculadora de descuentos
def calcular_precio(precio, es_miembro, cantidad):
    descuento = 0

    # Descuento por membresía
    if es_miembro:
        descuento += 0.10  # 10%

    # Descuento por cantidad
    if cantidad >= 10:
        descuento += 0.15  # 15%
    elif cantidad >= 5:
        descuento += 0.05  # 5%

    precio_final = precio * cantidad * (1 - descuento)
    return round(precio_final, 2)

print("\n--- Calculadora de descuentos ---")
print(f"  Precio normal (10 unids, no miembro): ${calcular_precio(100, False, 10)}")
print(f"  Precio con descuento (10 unids, miembro): ${calcular_precio(100, True, 10)}")


# 3. Validación de contraseña
def validar_password(password):
    errores = []

    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    if not any(c.isupper() for c in password):
        errores.append("Debe tener al menos una mayúscula")
    if not any(c.islower() for c in password):
        errores.append("Debe tener al menos una minúscula")
    if not any(c.isdigit() for c in password):
        errores.append("Debe tener al menos un número")

    if errores:
        return False, errores
    return True, ["Contraseña válida"]

print("\n--- Validación de contraseña ---")
passwords = ["abc", "abcdefgh", "Abcdefgh1"]
for pwd in passwords:
    valido, mensajes = validar_password(pwd)
    print(f"  '{pwd}': {'✓' if valido else '✗'} {mensajes[0]}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Escribe un programa que determine si un número es:
   - Positivo, negativo o cero
   - Par o impar

2. Crea una función que reciba tres lados de un triángulo
   y determine si es:
   - Equilátero (3 lados iguales)
   - Isósceles (2 lados iguales)
   - Escaleno (3 lados diferentes)

3. Escribe un programa que convierta una nota numérica (0-100)
   a letra (A, B, C, D, F) con los siguientes rangos:
   A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59

4. Crea un programa que determine si una persona puede
   obtener una tarjeta de crédito basándose en:
   - Edad >= 18
   - Ingresos >= 1000
   - Sin deudas pendientes

5. Usando match-case, crea un programa que procese comandos:
   - "ayuda" → muestra lista de comandos
   - "suma X Y" → suma dos números
   - "mayuscula TEXTO" → convierte a mayúsculas
   - "salir" → termina el programa
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 06_bucles.py")
print("=" * 60)
