"""
================================================================================
DECORADORES
================================================================================

Los decoradores son funciones que modifican el comportamiento de otras funciones
o clases sin cambiar su código fuente.

USOS COMUNES:
- Logging y debugging
- Medición de tiempo
- Validación de argumentos
- Caché/Memoización
- Control de acceso
- Registro de funciones

SINTAXIS:
    @decorador
    def funcion():
        pass

    # Equivale a:
    funcion = decorador(funcion)

================================================================================
"""

# ==============================================================================
# FUNCIONES COMO OBJETOS DE PRIMERA CLASE
# ==============================================================================

print("=" * 60)
print("FUNCIONES COMO OBJETOS DE PRIMERA CLASE")
print("=" * 60)

print("""
En Python, las funciones son objetos que pueden:
- Asignarse a variables
- Pasarse como argumentos
- Retornarse desde otras funciones
""")

def saludar(nombre):
    return f"¡Hola, {nombre}!"

# Asignar a variable
mi_funcion = saludar
print(f"Función asignada: {mi_funcion('Ana')}")

# Pasar como argumento
def ejecutar_funcion(func, valor):
    return func(valor)

resultado = ejecutar_funcion(saludar, "Luis")
print(f"Función como argumento: {resultado}")

# Retornar función
def crear_saludador(saludo):
    def saludador(nombre):
        return f"{saludo}, {nombre}!"
    return saludador

saludo_formal = crear_saludador("Buenos días")
saludo_informal = crear_saludador("Hey")

print(f"Saludo formal: {saludo_formal('María')}")
print(f"Saludo informal: {saludo_informal('Carlos')}")


# ==============================================================================
# DECORADOR BÁSICO
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADOR BÁSICO")
print("=" * 60)

def mi_decorador(func):
    """Decorador simple que añade mensaje antes y después."""
    def wrapper():
        print("  Antes de la función")
        func()
        print("  Después de la función")
    return wrapper

# Sin sintaxis @
def decir_hola():
    print("  ¡Hola!")

print("Sin decorador:")
decir_hola()

print("\nCon decorador (manual):")
decir_hola_decorada = mi_decorador(decir_hola)
decir_hola_decorada()

# Con sintaxis @
@mi_decorador
def decir_adios():
    print("  ¡Adiós!")

print("\nCon sintaxis @:")
decir_adios()


# ==============================================================================
# DECORADOR CON ARGUMENTOS DE FUNCIÓN
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADOR CON ARGUMENTOS DE FUNCIÓN")
print("=" * 60)

print("""
Para que el decorador funcione con funciones que tienen argumentos,
usamos *args y **kwargs en el wrapper.
""")

def log_llamada(func):
    """Registra cada llamada a la función."""
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        todos_args = ', '.join(filter(None, [args_str, kwargs_str]))
        print(f"  Llamando: {func.__name__}({todos_args})")
        resultado = func(*args, **kwargs)
        print(f"  Retornó: {resultado}")
        return resultado
    return wrapper

@log_llamada
def suma(a, b):
    return a + b

@log_llamada
def potencia(base, exponente=2):
    return base ** exponente

print("Probando decorador con argumentos:")
suma(3, 5)
potencia(2, exponente=10)


# ==============================================================================
# PRESERVAR METADATOS CON FUNCTOOLS.WRAPS
# ==============================================================================

print("\n" + "=" * 60)
print("PRESERVAR METADATOS CON FUNCTOOLS.WRAPS")
print("=" * 60)

from functools import wraps

def decorador_sin_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def decorador_con_wraps(func):
    @wraps(func)  # Preserva metadatos de func
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorador_sin_wraps
def funcion_a():
    """Documentación de función A."""
    pass

@decorador_con_wraps
def funcion_b():
    """Documentación de función B."""
    pass

print("Sin @wraps:")
print(f"  Nombre: {funcion_a.__name__}")
print(f"  Docstring: {funcion_a.__doc__}")

print("\nCon @wraps:")
print(f"  Nombre: {funcion_b.__name__}")
print(f"  Docstring: {funcion_b.__doc__}")


# ==============================================================================
# DECORADOR CON ARGUMENTOS
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADOR CON ARGUMENTOS")
print("=" * 60)

print("""
Para crear decoradores que aceptan argumentos,
necesitamos un nivel adicional de anidamiento.
""")

def repetir(veces):
    """Decorador que repite la función n veces."""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resultados = []
            for _ in range(veces):
                resultado = func(*args, **kwargs)
                resultados.append(resultado)
            return resultados
        return wrapper
    return decorador

@repetir(3)
def saludar(nombre):
    print(f"  ¡Hola, {nombre}!")
    return f"Saludo a {nombre}"

print("Función repetida 3 veces:")
resultados = saludar("Ana")
print(f"Resultados: {resultados}")


# Otro ejemplo: límite de reintentos
def reintentar(intentos=3, excepciones=(Exception,)):
    """Reintenta la función si falla."""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ultimo_error = None
            for intento in range(1, intentos + 1):
                try:
                    return func(*args, **kwargs)
                except excepciones as e:
                    ultimo_error = e
                    print(f"  Intento {intento} falló: {e}")
            raise ultimo_error
        return wrapper
    return decorador

import random

@reintentar(intentos=5, excepciones=(ValueError,))
def operacion_inestable():
    """Simula una operación que puede fallar."""
    if random.random() < 0.7:  # 70% de probabilidad de fallo
        raise ValueError("Operación falló")
    return "¡Éxito!"

print("\nOperación con reintentos:")
try:
    resultado = operacion_inestable()
    print(f"  Resultado: {resultado}")
except ValueError:
    print("  Todos los intentos fallaron")


# ==============================================================================
# DECORADORES ÚTILES EN LA PRÁCTICA
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADORES ÚTILES EN LA PRÁCTICA")
print("=" * 60)

# --- Medidor de tiempo ---
import time

def medir_tiempo(func):
    """Mide el tiempo de ejecución."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"  {func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta():
    time.sleep(0.1)
    return sum(range(100000))

print("--- Medidor de tiempo ---")
operacion_lenta()


# --- Caché simple (memoización) ---
def cache(func):
    """Cachea resultados de la función."""
    memoria = {}

    @wraps(func)
    def wrapper(*args):
        if args not in memoria:
            memoria[args] = func(*args)
            print(f"  Calculando {func.__name__}{args}")
        else:
            print(f"  Desde caché {func.__name__}{args}")
        return memoria[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n--- Caché (memoización) ---")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(10) de nuevo = {fibonacci(10)}")


# --- Validador de tipos ---
def validar_tipos(*tipos_args, **tipos_kwargs):
    """Valida los tipos de los argumentos."""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Validar args posicionales
            for valor, tipo in zip(args, tipos_args):
                if not isinstance(valor, tipo):
                    raise TypeError(f"Se esperaba {tipo.__name__}, se recibió {type(valor).__name__}")
            # Validar kwargs
            for nombre, tipo in tipos_kwargs.items():
                if nombre in kwargs and not isinstance(kwargs[nombre], tipo):
                    raise TypeError(f"{nombre} debe ser {tipo.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorador

@validar_tipos(str, int)
def crear_mensaje(texto, repeticiones):
    return texto * repeticiones

print("\n--- Validador de tipos ---")
print(f"crear_mensaje('Hola', 3) = {crear_mensaje('Hola', 3)}")
try:
    crear_mensaje(123, "no es int")
except TypeError as e:
    print(f"Error: {e}")


# --- Singleton ---
def singleton(cls):
    """Convierte una clase en singleton."""
    instancias = {}

    @wraps(cls)
    def obtener_instancia(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    return obtener_instancia

@singleton
class Configuracion:
    def __init__(self):
        self.debug = False
        self.database = "localhost"

print("\n--- Singleton ---")
config1 = Configuracion()
config2 = Configuracion()
print(f"¿Misma instancia?: {config1 is config2}")
config1.debug = True
print(f"config2.debug = {config2.debug}")


# ==============================================================================
# DECORADORES INCORPORADOS EN PYTHON
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADORES INCORPORADOS EN PYTHON")
print("=" * 60)

print("""
Python incluye varios decoradores útiles:
- @staticmethod: método sin acceso a instancia
- @classmethod: método con acceso a la clase
- @property: getter de propiedad
- @abstractmethod: método abstracto
- @functools.lru_cache: caché con límite
- @dataclass: genera métodos automáticamente
""")

from functools import lru_cache

@lru_cache(maxsize=100)
def factorial(n):
    """Factorial con caché LRU."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("@lru_cache:")
print(f"factorial(100) = {factorial(100)}")
print(f"Info del caché: {factorial.cache_info()}")


# ==============================================================================
# DECORADORES DE CLASE
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADORES DE CLASE")
print("=" * 60)

print("""
Los decoradores también pueden aplicarse a clases completas.
""")

def agregar_repr(cls):
    """Agrega __repr__ automático a la clase."""
    def __repr__(self):
        attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    cls.__repr__ = __repr__
    return cls

def agregar_comparacion(cls):
    """Agrega métodos de comparación basados en __dict__."""
    def __eq__(self, otro):
        if not isinstance(otro, cls):
            return False
        return self.__dict__ == otro.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    cls.__eq__ = __eq__
    cls.__hash__ = __hash__
    return cls

@agregar_repr
@agregar_comparacion
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Punto(1, 2)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(f"p1 = {p1}")  # Usa __repr__ agregado
print(f"p1 == p2: {p1 == p2}")  # Usa __eq__ agregado
print(f"p1 == p3: {p1 == p3}")


# Decorador que registra todas las instancias
def registrar_instancias(cls):
    """Mantiene registro de todas las instancias creadas."""
    cls._instancias = []
    init_original = cls.__init__

    def nuevo_init(self, *args, **kwargs):
        init_original(self, *args, **kwargs)
        cls._instancias.append(self)

    cls.__init__ = nuevo_init

    @classmethod
    def obtener_instancias(cls):
        return cls._instancias

    cls.obtener_instancias = obtener_instancias
    return cls

@registrar_instancias
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

u1 = Usuario("Ana")
u2 = Usuario("Luis")
u3 = Usuario("María")

print(f"\nUsuarios creados: {[u.nombre for u in Usuario.obtener_instancias()]}")


# ==============================================================================
# DECORADORES CON CLASES
# ==============================================================================

print("\n" + "=" * 60)
print("DECORADORES IMPLEMENTADOS COMO CLASES")
print("=" * 60)

print("""
Los decoradores pueden implementarse como clases usando __call__.
Útil cuando necesitas mantener estado.
""")

class ContadorLlamadas:
    """Decorador que cuenta las llamadas a una función."""

    def __init__(self, func):
        self.func = func
        self.llamadas = 0
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        self.llamadas += 1
        print(f"  Llamada #{self.llamadas} a {self.func.__name__}")
        return self.func(*args, **kwargs)

    def reset(self):
        self.llamadas = 0


@ContadorLlamadas
def mi_funcion(x):
    return x * 2

print("Decorador como clase:")
mi_funcion(5)
mi_funcion(10)
mi_funcion(15)
print(f"Total llamadas: {mi_funcion.llamadas}")
mi_funcion.reset()
print(f"Después de reset: {mi_funcion.llamadas}")


# Decorador con argumentos como clase
class LimitarLlamadas:
    """Limita el número de llamadas a una función."""

    def __init__(self, max_llamadas):
        self.max_llamadas = max_llamadas
        self.llamadas = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.llamadas >= self.max_llamadas:
                raise RuntimeError(f"Límite de {self.max_llamadas} llamadas alcanzado")
            self.llamadas += 1
            return func(*args, **kwargs)
        return wrapper

@LimitarLlamadas(max_llamadas=3)
def recurso_limitado():
    return "Acceso concedido"

print("\nDecorador con límite:")
for i in range(5):
    try:
        print(f"  Intento {i+1}: {recurso_limitado()}")
    except RuntimeError as e:
        print(f"  Intento {i+1}: Error - {e}")


# ==============================================================================
# APILAR DECORADORES
# ==============================================================================

print("\n" + "=" * 60)
print("APILAR DECORADORES")
print("=" * 60)

print("""
Se pueden aplicar múltiples decoradores a una función.
Se ejecutan de abajo hacia arriba.
""")

def decorador_a(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("  A: antes")
        resultado = func(*args, **kwargs)
        print("  A: después")
        return resultado
    return wrapper

def decorador_b(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("  B: antes")
        resultado = func(*args, **kwargs)
        print("  B: después")
        return resultado
    return wrapper

@decorador_a
@decorador_b
def mi_funcion():
    print("  Función ejecutándose")

print("Ejecutando función con decoradores apilados:")
mi_funcion()

print("""
Orden de ejecución:
1. @decorador_a envuelve todo
2. @decorador_b está dentro de A
3. La función está dentro de B
""")


# ==============================================================================
# EJEMPLO COMPLETO: FRAMEWORK DE API SIMPLE
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO COMPLETO: FRAMEWORK DE API SIMPLE")
print("=" * 60)

class APISimple:
    """Framework simple de API con decoradores."""

    rutas = {}

    @classmethod
    def ruta(cls, path, metodo="GET"):
        """Decorador para registrar rutas."""
        def decorador(func):
            cls.rutas[(metodo, path)] = func
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorador

    @classmethod
    def procesar_peticion(cls, metodo, path, **params):
        """Procesa una petición."""
        handler = cls.rutas.get((metodo, path))
        if handler:
            return handler(**params)
        return {"error": "Ruta no encontrada"}


def requiere_auth(func):
    """Decorador que requiere autenticación."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get('token')
        if token != "secreto":
            return {"error": "No autorizado"}
        return func(*args, **kwargs)
    return wrapper


def validar_json(campos_requeridos):
    """Decorador que valida campos requeridos."""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for campo in campos_requeridos:
                if campo not in kwargs:
                    return {"error": f"Campo requerido: {campo}"}
            return func(*args, **kwargs)
        return wrapper
    return decorador


# Definir endpoints
@APISimple.ruta("/usuarios", "GET")
def listar_usuarios():
    return {"usuarios": ["Ana", "Luis", "María"]}


@APISimple.ruta("/usuarios", "POST")
@requiere_auth
@validar_json(["nombre", "email"])
def crear_usuario(**datos):
    return {"mensaje": f"Usuario {datos['nombre']} creado"}


@APISimple.ruta("/admin", "GET")
@requiere_auth
def panel_admin(**kwargs):
    return {"mensaje": "Bienvenido al panel de admin"}


# Probar API
print("--- Peticiones a la API ---")

print("\nGET /usuarios:")
print(f"  {APISimple.procesar_peticion('GET', '/usuarios')}")

print("\nPOST /usuarios (sin auth):")
print(f"  {APISimple.procesar_peticion('POST', '/usuarios', nombre='Carlos', email='c@e.com')}")

print("\nPOST /usuarios (con auth, sin campos):")
print(f"  {APISimple.procesar_peticion('POST', '/usuarios', token='secreto')}")

print("\nPOST /usuarios (completo):")
print(f"  {APISimple.procesar_peticion('POST', '/usuarios', token='secreto', nombre='Carlos', email='c@e.com')}")

print("\nGET /admin (con auth):")
print(f"  {APISimple.procesar_peticion('GET', '/admin', token='secreto')}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea un decorador @deprecated que muestre un warning
   cuando se usa una función marcada como obsoleta

2. Implementa un decorador @rate_limit(calls, period) que
   limite el número de llamadas en un período de tiempo

3. Crea un decorador @debug que imprima los argumentos,
   el resultado y el tiempo de ejecución

4. Implementa un decorador @once que asegure que la
   función solo se ejecute una vez

5. Crea un decorador @retry_on_exception que reintente
   la función con backoff exponencial

6. Implementa un sistema de plugins usando decoradores
   donde cada plugin se registre automáticamente

7. Crea un decorador que convierta el resultado de
   una función a JSON automáticamente

8. Implementa un decorador @log_to_file que escriba
   las llamadas a un archivo de log
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 19_generadores_iteradores.py")
print("=" * 60)
