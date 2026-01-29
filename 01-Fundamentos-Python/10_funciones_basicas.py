"""
================================================================================
FUNCIONES - CONCEPTOS BÁSICOS
================================================================================

¿QUÉ ES UNA FUNCIÓN?
-------------------
Una función es un bloque de código reutilizable que realiza una tarea específica.

VENTAJAS:
- Reutilización: escribir una vez, usar muchas veces
- Organización: dividir código en partes manejables
- Abstracción: ocultar detalles de implementación
- Mantenimiento: cambios en un solo lugar
- Testing: probar partes del código por separado

ANATOMÍA DE UNA FUNCIÓN:
    def nombre_funcion(parametros):
        '''Docstring: documentación'''
        # cuerpo de la función
        return valor  # opcional

================================================================================
"""

# ==============================================================================
# DEFINIR Y LLAMAR FUNCIONES
# ==============================================================================

print("=" * 60)
print("DEFINIR Y LLAMAR FUNCIONES")
print("=" * 60)

# Función sin parámetros ni retorno
def saludar():
    """Imprime un saludo simple."""
    print("¡Hola, mundo!")

# Llamar la función
saludar()
saludar()  # Podemos llamarla múltiples veces

# Función con parámetro
def saludar_a(nombre):
    """Saluda a una persona específica."""
    print(f"¡Hola, {nombre}!")

saludar_a("Ana")
saludar_a("Luis")

# Función con retorno
def sumar(a, b):
    """Retorna la suma de dos números."""
    resultado = a + b
    return resultado

total = sumar(5, 3)
print(f"\n5 + 3 = {total}")

# El return termina la función
def division_segura(a, b):
    """Divide a entre b, retorna None si b es cero."""
    if b == 0:
        return None  # Sale de la función aquí
    return a / b

print(f"10 / 2 = {division_segura(10, 2)}")
print(f"10 / 0 = {division_segura(10, 0)}")


# ==============================================================================
# PARÁMETROS Y ARGUMENTOS
# ==============================================================================

print("\n" + "=" * 60)
print("PARÁMETROS Y ARGUMENTOS")
print("=" * 60)

print("""
TERMINOLOGÍA:
- Parámetros: variables en la definición de la función
- Argumentos: valores pasados al llamar la función

def funcion(parametro):  # 'parametro' es el parámetro
    ...

funcion(argumento)  # 'argumento' es el argumento
""")

# Múltiples parámetros
def presentar(nombre, edad, ciudad):
    """Presenta a una persona."""
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

# Argumentos posicionales
presentar("Ana", 25, "Madrid")

# Argumentos con nombre (keyword arguments)
presentar(nombre="Luis", ciudad="Barcelona", edad=30)

# Mezcla (posicionales primero)
presentar("María", ciudad="Sevilla", edad=28)


# ==============================================================================
# VALORES POR DEFECTO
# ==============================================================================

print("\n" + "=" * 60)
print("VALORES POR DEFECTO")
print("=" * 60)

def saludar_formal(nombre, saludo="Hola", despedida="Adiós"):
    """Saluda con opciones personalizables."""
    print(f"{saludo}, {nombre}!")
    print(f"{despedida}, {nombre}!")

print("--- Sin valores por defecto ---")
saludar_formal("Ana")

print("\n--- Con valores personalizados ---")
saludar_formal("Luis", saludo="Buenos días")
saludar_formal("María", despedida="Hasta luego")
saludar_formal("Carlos", "Hey", "Chao")

# ¡CUIDADO! No usar mutables como valores por defecto
print("\n--- Peligro con mutables por defecto ---")

# MAL: lista compartida entre llamadas
def agregar_item_mal(item, lista=[]):
    lista.append(item)
    return lista

print(f"Primera llamada: {agregar_item_mal('a')}")
print(f"Segunda llamada: {agregar_item_mal('b')}")  # ¡Mantiene 'a'!

# BIEN: usar None y crear nueva lista
def agregar_item_bien(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print(f"\nPrimera llamada: {agregar_item_bien('a')}")
print(f"Segunda llamada: {agregar_item_bien('b')}")  # Nueva lista


# ==============================================================================
# RETORNO DE VALORES
# ==============================================================================

print("\n" + "=" * 60)
print("RETORNO DE VALORES")
print("=" * 60)

# Sin return explícito retorna None
def sin_return():
    x = 5 + 3

resultado = sin_return()
print(f"Sin return: {resultado}")

# Return vacío también retorna None
def return_vacio():
    return

print(f"Return vacío: {return_vacio()}")

# Retornar múltiples valores (tupla)
def estadisticas(numeros):
    """Calcula estadísticas básicas."""
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)
    return minimo, maximo, promedio  # Retorna tupla

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_val, max_val, prom = estadisticas(datos)
print(f"\nEstadísticas de {datos}:")
print(f"  Mínimo: {min_val}, Máximo: {max_val}, Promedio: {prom}")

# También como tupla
resultado = estadisticas(datos)
print(f"  Como tupla: {resultado}")


# ==============================================================================
# DOCSTRINGS
# ==============================================================================

print("\n" + "=" * 60)
print("DOCSTRINGS - DOCUMENTACIÓN")
print("=" * 60)

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo

    Retorna:
        float: El área calculada (base * altura)

    Ejemplo:
        >>> calcular_area_rectangulo(5, 3)
        15
    """
    return base * altura

# Acceder a la documentación
print("Documentación de la función:")
print(calcular_area_rectangulo.__doc__)

# help() también muestra la documentación
# help(calcular_area_rectangulo)


# ==============================================================================
# ÁMBITO DE VARIABLES (SCOPE)
# ==============================================================================

print("\n" + "=" * 60)
print("ÁMBITO DE VARIABLES (SCOPE)")
print("=" * 60)

print("""
REGLA LEGB:
- Local: dentro de la función actual
- Enclosing: función contenedora (funciones anidadas)
- Global: nivel del módulo
- Built-in: funciones integradas de Python
""")

# Variable global
mensaje_global = "Soy global"

def mostrar_scope():
    # Variable local
    mensaje_local = "Soy local"
    print(f"  Dentro de función - Local: {mensaje_local}")
    print(f"  Dentro de función - Global: {mensaje_global}")

mostrar_scope()
print(f"Fuera de función - Global: {mensaje_global}")
# print(mensaje_local)  # Error: no existe fuera de la función

# Modificar variable global
contador = 0

def incrementar():
    global contador  # Declarar que usamos la global
    contador += 1

print(f"\nContador antes: {contador}")
incrementar()
incrementar()
print(f"Contador después: {contador}")

# Mejor práctica: evitar global, usar parámetros y return
def incrementar_mejor(valor):
    return valor + 1

contador2 = 0
contador2 = incrementar_mejor(contador2)
contador2 = incrementar_mejor(contador2)
print(f"Con return: {contador2}")


# ==============================================================================
# FUNCIONES COMO OBJETOS
# ==============================================================================

print("\n" + "=" * 60)
print("FUNCIONES COMO OBJETOS")
print("=" * 60)

print("""
En Python, las funciones son objetos de primera clase:
- Se pueden asignar a variables
- Se pueden pasar como argumentos
- Se pueden retornar desde otras funciones
""")

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

# Asignar a variable
operacion = cuadrado
print(f"operacion(5) = {operacion(5)}")

operacion = cubo
print(f"operacion(5) = {operacion(5)}")

# Pasar como argumento
def aplicar_operacion(func, valor):
    return func(valor)

print(f"\naplicar_operacion(cuadrado, 4) = {aplicar_operacion(cuadrado, 4)}")
print(f"aplicar_operacion(cubo, 4) = {aplicar_operacion(cubo, 4)}")

# Lista de funciones
operaciones = [cuadrado, cubo, abs]
valor = -3
print(f"\nAplicar todas las operaciones a {valor}:")
for op in operaciones:
    print(f"  {op.__name__}({valor}) = {op(valor)}")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Validar email
def es_email_valido(email):
    """Validación básica de email."""
    if "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    usuario, dominio = partes
    if not usuario or not dominio:
        return False
    if "." not in dominio:
        return False
    return True

print("--- Validar emails ---")
emails = ["user@gmail.com", "invalido@", "test@dominio.org", "@sin.usuario"]
for email in emails:
    valido = "✓" if es_email_valido(email) else "✗"
    print(f"  {email}: {valido}")

# 2. Calcular precio con descuento
def calcular_precio_final(precio, descuento=0, impuesto=0.16):
    """
    Calcula el precio final con descuento e impuesto.

    Parámetros:
        precio: Precio base
        descuento: Porcentaje de descuento (0-100)
        impuesto: Tasa de impuesto (default 16%)

    Retorna:
        Precio final redondeado a 2 decimales
    """
    precio_con_descuento = precio * (1 - descuento / 100)
    precio_final = precio_con_descuento * (1 + impuesto)
    return round(precio_final, 2)

print("\n--- Calcular precio ---")
print(f"  $100, sin descuento: ${calcular_precio_final(100)}")
print(f"  $100, 20% descuento: ${calcular_precio_final(100, descuento=20)}")
print(f"  $100, 10% descuento, 21% IVA: ${calcular_precio_final(100, 10, 0.21)}")

# 3. Formatear nombre
def formatear_nombre(nombre, apellido, formato="completo"):
    """
    Formatea un nombre según el formato especificado.

    Formatos: 'completo', 'formal', 'iniciales'
    """
    nombre = nombre.strip().title()
    apellido = apellido.strip().title()

    if formato == "completo":
        return f"{nombre} {apellido}"
    elif formato == "formal":
        return f"{apellido}, {nombre}"
    elif formato == "iniciales":
        return f"{nombre[0]}. {apellido[0]}."
    else:
        return f"{nombre} {apellido}"

print("\n--- Formatear nombre ---")
print(f"  Completo: {formatear_nombre('juan', 'PÉREZ')}")
print(f"  Formal: {formatear_nombre('juan', 'pérez', 'formal')}")
print(f"  Iniciales: {formatear_nombre('Juan', 'Pérez', 'iniciales')}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Escribe una función que calcule el factorial de un número

2. Crea una función que reciba una lista de números y retorne:
   - El mayor
   - El menor
   - El promedio
   (sin usar las funciones built-in max, min)

3. Escribe una función que verifique si un número es primo

4. Crea una función que convierta temperatura:
   - celsius_a_fahrenheit(celsius)
   - fahrenheit_a_celsius(fahrenheit)

5. Escribe una función que cuente las vocales y consonantes
   de un string, retornando un diccionario

6. Crea una función que reciba una lista de palabras y
   retorne solo las que tienen más de n caracteres
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 11_funciones_avanzadas.py")
print("=" * 60)
