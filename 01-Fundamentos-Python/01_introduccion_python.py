"""
================================================================================
INTRODUCCIÓN A PYTHON
================================================================================

¿QUÉ ES PYTHON?
---------------
Python es un lenguaje de programación:
- De alto nivel (cercano al lenguaje humano)
- Interpretado (no necesita compilación)
- De propósito general (sirve para todo)
- Con tipado dinámico (no declaras tipos)

CREADOR: Guido van Rossum (1991)
NOMBRE: Viene de "Monty Python" (grupo de comedia)

¿POR QUÉ PYTHON?
---------------
1. Sintaxis simple y legible
2. Gran comunidad y documentación
3. Muchísimas librerías disponibles
4. Usado en: IA, Data Science, Web, Automatización, etc.
5. Demandado en el mercado laboral

FILOSOFÍA DE PYTHON (El Zen de Python):
--------------------------------------
- Bello es mejor que feo
- Explícito es mejor que implícito
- Simple es mejor que complejo
- La legibilidad cuenta
- Debería haber una manera obvia de hacerlo

================================================================================
"""

# ==============================================================================
# TU PRIMER PROGRAMA
# ==============================================================================

print("=" * 60)
print("¡HOLA MUNDO!")
print("=" * 60)

# La función print() muestra texto en la pantalla
print("¡Hola, mundo!")
print("Bienvenido a Python")

# Puedes imprimir múltiples valores separados por coma
print("Python", "es", "genial")

# Por defecto, print añade un salto de línea al final
# Puedes cambiarlo con el parámetro 'end'
print("Esto no tiene salto de línea...", end=" ")
print("¡Continúa aquí!")


# ==============================================================================
# COMENTARIOS
# ==============================================================================

print("\n" + "=" * 60)
print("COMENTARIOS")
print("=" * 60)

# Esto es un comentario de una línea
# Los comentarios son ignorados por Python
# Se usan para explicar el código

"""
Esto es un comentario
de múltiples líneas.
También llamado docstring
cuando está al inicio de una función/clase.
"""

# Los comentarios son MUY importantes para:
# 1. Explicar código complejo
# 2. Documentar funciones
# 3. Dejar notas para ti mismo o otros programadores
# 4. Temporalmente "desactivar" código

print("Los comentarios no se ejecutan")
# print("Esta línea está comentada, no se ejecutará")


# ==============================================================================
# INDENTACIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("INDENTACIÓN (MUY IMPORTANTE)")
print("=" * 60)

print("""
En Python, la INDENTACIÓN (espacios al inicio) es OBLIGATORIA.
Define los bloques de código.

CORRECTO:
    if True:
        print("Indentado con 4 espacios")

INCORRECTO (dará error):
    if True:
    print("Sin indentar")  # ¡Error!

Convención: Usar 4 ESPACIOS (no tabuladores)
""")

# Ejemplo de indentación correcta
if True:
    print("  Este código está dentro del 'if'")
    print("  También este")
print("Este código está fuera del 'if'")


# ==============================================================================
# PYTHON COMO CALCULADORA
# ==============================================================================

print("\n" + "=" * 60)
print("PYTHON COMO CALCULADORA")
print("=" * 60)

# Python puede hacer cálculos directamente
print("Operaciones básicas:")
print(f"  5 + 3 = {5 + 3}")      # Suma
print(f"  10 - 4 = {10 - 4}")    # Resta
print(f"  6 * 7 = {6 * 7}")      # Multiplicación
print(f"  20 / 4 = {20 / 4}")    # División (siempre retorna float)
print(f"  20 // 3 = {20 // 3}")  # División entera
print(f"  20 % 3 = {20 % 3}")    # Módulo (resto)
print(f"  2 ** 10 = {2 ** 10}")  # Potencia

# Orden de operaciones (PEMDAS)
print("\nOrden de operaciones:")
print(f"  2 + 3 * 4 = {2 + 3 * 4}")      # Primero multiplicación
print(f"  (2 + 3) * 4 = {(2 + 3) * 4}")  # Paréntesis primero


# ==============================================================================
# FUNCIÓN input() - ENTRADA DEL USUARIO
# ==============================================================================

print("\n" + "=" * 60)
print("ENTRADA DEL USUARIO")
print("=" * 60)

print("""
La función input() permite recibir datos del usuario:

    nombre = input("¿Cómo te llamas? ")
    print(f"Hola, {nombre}")

IMPORTANTE: input() SIEMPRE retorna un STRING (texto)
Si necesitas un número, debes convertirlo:

    edad = int(input("¿Cuántos años tienes? "))
    precio = float(input("¿Cuál es el precio? "))
""")

# Ejemplo (comentado para que el script no se pause)
# nombre = input("¿Cómo te llamas? ")
# print(f"¡Hola, {nombre}!")


# ==============================================================================
# ERRORES COMUNES AL EMPEZAR
# ==============================================================================

print("\n" + "=" * 60)
print("ERRORES COMUNES")
print("=" * 60)

print("""
1. SyntaxError - Error de sintaxis
   print("Hola"   # Falta cerrar paréntesis

2. IndentationError - Error de indentación
   if True:
   print("mal")   # Falta indentar

3. NameError - Variable no definida
   print(variable_inexistente)

4. TypeError - Tipo incorrecto
   "texto" + 5    # No puedes sumar string y número

5. ZeroDivisionError - División por cero
   10 / 0         # No se puede dividir por cero

¡No te frustres! Los errores son normales y parte del aprendizaje.
Python te dice en qué línea está el error.
""")


# ==============================================================================
# EJECUTAR PYTHON
# ==============================================================================

print("\n" + "=" * 60)
print("FORMAS DE EJECUTAR PYTHON")
print("=" * 60)

print("""
1. MODO INTERACTIVO (REPL):
   $ python3
   >>> print("Hola")
   Hola
   >>> exit()

2. EJECUTAR ARCHIVO:
   $ python3 mi_archivo.py

3. JUPYTER NOTEBOOK:
   Celdas interactivas, ideal para aprendizaje

4. IDE (Entorno de Desarrollo):
   - VS Code (recomendado)
   - PyCharm
   - Sublime Text
""")


# ==============================================================================
# EJERCICIOS PROPUESTOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS PARA PRACTICAR")
print("=" * 60)

print("""
1. Modifica el programa para que imprima tu nombre

2. Usa Python como calculadora:
   - Calcula cuántos segundos hay en un día
   - Calcula el área de un círculo (π * r²)

3. Escribe un programa que:
   - Pida el nombre al usuario
   - Pida la edad
   - Imprima un saludo personalizado

4. Experimenta causando errores a propósito
   para ver los mensajes de error
""")

# Ejemplo ejercicio 2:
print("\nEjemplo - Segundos en un día:")
segundos_minuto = 60
minutos_hora = 60
horas_dia = 24
segundos_dia = segundos_minuto * minutos_hora * horas_dia
print(f"  Hay {segundos_dia:,} segundos en un día")

print("\n" + "=" * 60)
print("SIGUIENTE: 02_variables_tipos_datos.py")
print("=" * 60)
