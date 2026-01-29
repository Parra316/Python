"""
================================================================================
FUNCIONES AVANZADAS
================================================================================

Temas avanzados de funciones:
- *args y **kwargs
- Funciones lambda
- Funciones de orden superior (map, filter, reduce)
- Closures
- Funciones anidadas

================================================================================
"""

# ==============================================================================
# *ARGS - ARGUMENTOS POSICIONALES VARIABLES
# ==============================================================================

print("=" * 60)
print("*ARGS - Argumentos posicionales variables")
print("=" * 60)

print("""
*args permite recibir cualquier número de argumentos posicionales.
Los argumentos se empaquetan en una tupla.
""")

def sumar_todos(*args):
    """Suma cualquier cantidad de números."""
    print(f"  args recibidos: {args} (tipo: {type(args).__name__})")
    return sum(args)

print(f"sumar_todos(1, 2) = {sumar_todos(1, 2)}")
print(f"sumar_todos(1, 2, 3, 4, 5) = {sumar_todos(1, 2, 3, 4, 5)}")

# Combinar con parámetros normales
def multiplicar(factor, *numeros):
    """Multiplica cada número por el factor."""
    return [n * factor for n in numeros]

print(f"\nmultiplicar(2, 1, 2, 3) = {multiplicar(2, 1, 2, 3)}")

# Desempaquetar lista al llamar
numeros = [1, 2, 3, 4, 5]
print(f"sumar_todos(*{numeros}) = {sumar_todos(*numeros)}")


# ==============================================================================
# **KWARGS - ARGUMENTOS CON NOMBRE VARIABLES
# ==============================================================================

print("\n" + "=" * 60)
print("**KWARGS - Argumentos con nombre variables")
print("=" * 60)

print("""
**kwargs permite recibir cualquier número de argumentos con nombre.
Los argumentos se empaquetan en un diccionario.
""")

def mostrar_info(**kwargs):
    """Muestra información recibida."""
    print(f"  kwargs recibidos: {kwargs}")
    for clave, valor in kwargs.items():
        print(f"    {clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Madrid")

# Combinar con parámetros normales y *args
def funcion_completa(obligatorio, *args, defecto="valor", **kwargs):
    """Demuestra todos los tipos de parámetros."""
    print(f"  obligatorio: {obligatorio}")
    print(f"  args: {args}")
    print(f"  defecto: {defecto}")
    print(f"  kwargs: {kwargs}")

print("\nfuncion_completa('primero', 1, 2, 3, defecto='nuevo', extra='dato'):")
funcion_completa('primero', 1, 2, 3, defecto='nuevo', extra='dato')

# Desempaquetar diccionario al llamar
datos = {"nombre": "Luis", "edad": 30}
print(f"\nmostrar_info(**{datos}):")
mostrar_info(**datos)


# ==============================================================================
# FUNCIONES LAMBDA
# ==============================================================================

print("\n" + "=" * 60)
print("FUNCIONES LAMBDA")
print("=" * 60)

print("""
Lambda son funciones anónimas de una línea.
Sintaxis: lambda argumentos: expresión

Útiles para funciones simples y de un solo uso.
""")

# Función normal vs lambda
def cuadrado(x):
    return x ** 2

cuadrado_lambda = lambda x: x ** 2

print(f"Función normal: cuadrado(5) = {cuadrado(5)}")
print(f"Lambda: cuadrado_lambda(5) = {cuadrado_lambda(5)}")

# Múltiples argumentos
suma = lambda a, b: a + b
print(f"\nsuma(3, 4) = {suma(3, 4)}")

# Con condicional
par_o_impar = lambda n: "par" if n % 2 == 0 else "impar"
print(f"par_o_impar(7) = {par_o_impar(7)}")

# Uso común: como argumento de otras funciones
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOrdenar {numeros}:")
print(f"  sorted() normal: {sorted(numeros)}")
print(f"  sorted() descendente: {sorted(numeros, key=lambda x: -x)}")

# Ordenar objetos por atributo
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "María", "edad": 22}
]
print(f"\nOrdenar por edad:")
for p in sorted(personas, key=lambda x: x["edad"]):
    print(f"  {p['nombre']}: {p['edad']}")


# ==============================================================================
# MAP, FILTER, REDUCE
# ==============================================================================

print("\n" + "=" * 60)
print("MAP, FILTER, REDUCE")
print("=" * 60)

# --- MAP: aplicar función a cada elemento ---
print("--- map() ---")
numeros = [1, 2, 3, 4, 5]

# Elevar al cuadrado
cuadrados = list(map(lambda x: x**2, numeros))
print(f"map(x**2, {numeros}) = {cuadrados}")

# Con función nombrada
def fahrenheit_a_celsius(f):
    return round((f - 32) * 5/9, 1)

temps_f = [32, 68, 100, 212]
temps_c = list(map(fahrenheit_a_celsius, temps_f))
print(f"Fahrenheit {temps_f} → Celsius {temps_c}")

# map con múltiples iterables
a = [1, 2, 3]
b = [10, 20, 30]
sumas = list(map(lambda x, y: x + y, a, b))
print(f"map(suma, {a}, {b}) = {sumas}")

# --- FILTER: filtrar elementos ---
print("\n--- filter() ---")
numeros = range(1, 11)

# Solo pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"filter(pares, 1-10) = {pares}")

# Solo mayores que 5
mayores = list(filter(lambda x: x > 5, numeros))
print(f"filter(>5, 1-10) = {mayores}")

# Filtrar strings vacíos
palabras = ["hola", "", "mundo", "", "python"]
no_vacias = list(filter(None, palabras))  # None filtra valores "falsy"
print(f"filter(None, {palabras}) = {no_vacias}")

# --- REDUCE: reducir a un solo valor ---
print("\n--- reduce() ---")
from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Suma acumulativa
suma = reduce(lambda acc, x: acc + x, numeros)
print(f"reduce(suma, {numeros}) = {suma}")

# Producto
producto = reduce(lambda acc, x: acc * x, numeros)
print(f"reduce(producto, {numeros}) = {producto}")

# Encontrar máximo
maximo = reduce(lambda acc, x: x if x > acc else acc, numeros)
print(f"reduce(max, {numeros}) = {maximo}")

# Con valor inicial
suma_desde_10 = reduce(lambda acc, x: acc + x, numeros, 10)
print(f"reduce(suma, {numeros}, inicial=10) = {suma_desde_10}")


# ==============================================================================
# FUNCIONES ANIDADAS
# ==============================================================================

print("\n" + "=" * 60)
print("FUNCIONES ANIDADAS")
print("=" * 60)

def exterior(x):
    """Función exterior."""

    def interior(y):
        """Función interior - tiene acceso a x."""
        return x + y

    return interior(10)

print(f"exterior(5) = {exterior(5)}")  # 5 + 10 = 15

# Función que retorna otra función
def crear_multiplicador(factor):
    """Crea una función que multiplica por factor."""

    def multiplicar(numero):
        return numero * factor

    return multiplicar  # Retorna la función, no el resultado

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(f"\nduplicar(5) = {duplicar(5)}")
print(f"triplicar(5) = {triplicar(5)}")


# ==============================================================================
# CLOSURES
# ==============================================================================

print("\n" + "=" * 60)
print("CLOSURES")
print("=" * 60)

print("""
Un closure es una función que recuerda el entorno en el que
fue creada, incluso después de que ese entorno haya terminado.
""")

def crear_contador(inicio=0):
    """Crea un contador con estado."""
    cuenta = [inicio]  # Usamos lista para poder modificar

    def incrementar():
        cuenta[0] += 1
        return cuenta[0]

    return incrementar

contador1 = crear_contador()
contador2 = crear_contador(100)

print(f"contador1: {contador1()}, {contador1()}, {contador1()}")
print(f"contador2: {contador2()}, {contador2()}")

# Usando nonlocal (Python 3+)
def crear_contador_v2(inicio=0):
    """Versión con nonlocal."""
    cuenta = inicio

    def incrementar():
        nonlocal cuenta  # Permite modificar variable del scope exterior
        cuenta += 1
        return cuenta

    return incrementar

contador3 = crear_contador_v2(50)
print(f"contador3: {contador3()}, {contador3()}, {contador3()}")


# ==============================================================================
# FUNCIONES COMO DECORADORES (PREVIEW)
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADORES (Vista previa)")
print("=" * 60)

def mi_decorador(func):
    """Un decorador simple que añade logging."""
    def wrapper(*args, **kwargs):
        print(f"  Llamando a {func.__name__}...")
        resultado = func(*args, **kwargs)
        print(f"  {func.__name__} retornó: {resultado}")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre):
    return f"¡Hola, {nombre}!"

print("Llamando función decorada:")
saludar("Ana")

print("\n(Más detalles en 18_decoradores.py)")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Validador configurable
def crear_validador(min_len=1, max_len=100, permitir_numeros=True):
    """Crea una función validadora personalizada."""

    def validar(texto):
        if len(texto) < min_len:
            return False, f"Muy corto (mínimo {min_len})"
        if len(texto) > max_len:
            return False, f"Muy largo (máximo {max_len})"
        if not permitir_numeros and any(c.isdigit() for c in texto):
            return False, "No se permiten números"
        return True, "Válido"

    return validar

print("--- Validador configurable ---")
validar_usuario = crear_validador(min_len=3, max_len=20, permitir_numeros=False)
validar_password = crear_validador(min_len=8)

for texto in ["ab", "usuario", "user123", "contraseña_segura"]:
    valido, msg = validar_usuario(texto)
    print(f"  Usuario '{texto}': {msg}")

# 2. Procesamiento de datos con map/filter
print("\n--- Procesamiento de datos ---")
productos = [
    {"nombre": "Laptop", "precio": 1000, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 0},
    {"nombre": "Teclado", "precio": 75, "stock": 10},
    {"nombre": "Monitor", "precio": 300, "stock": 3},
]

# Filtrar productos en stock
en_stock = list(filter(lambda p: p["stock"] > 0, productos))
print(f"Productos en stock: {[p['nombre'] for p in en_stock]}")

# Aplicar descuento del 10%
con_descuento = list(map(
    lambda p: {**p, "precio_desc": p["precio"] * 0.9},
    productos
))
for p in con_descuento:
    print(f"  {p['nombre']}: ${p['precio']} → ${p['precio_desc']}")

# 3. Composición de funciones
print("\n--- Composición de funciones ---")
def componer(*funciones):
    """Compone múltiples funciones en una sola."""
    def composicion(x):
        resultado = x
        for f in reversed(funciones):
            resultado = f(resultado)
        return resultado
    return composicion

# Crear pipeline de procesamiento de texto
limpiar = lambda s: s.strip()
mayusculas = lambda s: s.upper()
añadir_exclamacion = lambda s: s + "!"

procesar_texto = componer(añadir_exclamacion, mayusculas, limpiar)
print(f"procesar_texto('  hola  ') = '{procesar_texto('  hola  ')}'")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Escribe una función que acepte cualquier número de strings
   y los concatene con un separador configurable

2. Usa map() para convertir una lista de strings a enteros

3. Usa filter() para obtener solo las palabras que empiezan
   con vocal de una lista

4. Usa reduce() para encontrar el string más largo de una lista

5. Crea un closure que genere IDs únicos incrementales
   con un prefijo configurable (ej: "USER-001", "USER-002")

6. Escribe una función que reciba una lista de funciones
   y un valor, y aplique todas las funciones en secuencia
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 12_comprehensions.py")
print("=" * 60)
