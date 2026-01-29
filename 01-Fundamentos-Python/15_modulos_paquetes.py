"""
================================================================================
MÓDULOS Y PAQUETES
================================================================================

MÓDULO: Un archivo .py que contiene código Python reutilizable.
PAQUETE: Un directorio con módulos y un archivo __init__.py.

VENTAJAS:
- Organización del código
- Reutilización
- Namespaces separados
- Mantenibilidad

================================================================================
"""

# ==============================================================================
# IMPORTAR MÓDULOS
# ==============================================================================

print("=" * 60)
print("IMPORTAR MÓDULOS")
print("=" * 60)

# import módulo
import math
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")

# import módulo as alias
import math as m
print(f"m.cos(0) = {m.cos(0)}")

# from módulo import función
from math import sqrt, pi
print(f"sqrt(25) = {sqrt(25)}")
print(f"pi = {pi}")

# from módulo import función as alias
from math import factorial as fact
print(f"fact(5) = {fact(5)}")

# from módulo import * (NO RECOMENDADO)
# from math import *  # Importa todo, contamina el namespace


# ==============================================================================
# MÓDULOS DE LA BIBLIOTECA ESTÁNDAR
# ==============================================================================

print("\n" + "=" * 60)
print("MÓDULOS DE LA BIBLIOTECA ESTÁNDAR")
print("=" * 60)

# --- os: Sistema operativo ---
print("--- os ---")
import os
print(f"Directorio actual: {os.getcwd()}")
print(f"Variables de entorno HOME: {os.environ.get('HOME', 'N/A')}")
print(f"Separador de path: '{os.sep}'")

# --- sys: Sistema Python ---
print("\n--- sys ---")
import sys
print(f"Versión de Python: {sys.version_info.major}.{sys.version_info.minor}")
print(f"Plataforma: {sys.platform}")
print(f"Path de búsqueda de módulos: {sys.path[:3]}...")

# --- datetime: Fechas y horas ---
print("\n--- datetime ---")
from datetime import datetime, timedelta
ahora = datetime.now()
print(f"Ahora: {ahora}")
print(f"Formateado: {ahora.strftime('%d/%m/%Y %H:%M')}")
mañana = ahora + timedelta(days=1)
print(f"Mañana: {mañana.date()}")

# --- random: Números aleatorios ---
print("\n--- random ---")
import random
print(f"Número aleatorio 1-10: {random.randint(1, 10)}")
lista = [1, 2, 3, 4, 5]
print(f"Elección aleatoria de {lista}: {random.choice(lista)}")
random.shuffle(lista)
print(f"Lista mezclada: {lista}")

# --- collections: Estructuras de datos ---
print("\n--- collections ---")
from collections import Counter, defaultdict, namedtuple

# Counter
texto = "abracadabra"
conteo = Counter(texto)
print(f"Counter('{texto}'): {conteo.most_common(3)}")

# defaultdict
grupos = defaultdict(list)
datos = [("fruta", "manzana"), ("vegetal", "zanahoria"), ("fruta", "naranja")]
for categoria, item in datos:
    grupos[categoria].append(item)
print(f"defaultdict: {dict(grupos)}")

# --- itertools: Iteradores ---
print("\n--- itertools ---")
from itertools import combinations, permutations, cycle, islice

letras = "ABC"
print(f"Combinaciones de 2 de '{letras}': {list(combinations(letras, 2))}")
print(f"Permutaciones de 2 de '{letras}': {list(permutations(letras, 2))}")

# --- functools: Herramientas funcionales ---
print("\n--- functools ---")
from functools import reduce, lru_cache

# reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda a, b: a + b, numeros)
print(f"reduce(suma, {numeros}) = {suma}")

# lru_cache - memoización
@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"fibonacci(30) = {fibonacci(30)}")


# ==============================================================================
# CREAR TU PROPIO MÓDULO
# ==============================================================================

print("\n" + "=" * 60)
print("CREAR TU PROPIO MÓDULO")
print("=" * 60)

print("""
Para crear un módulo, simplemente crea un archivo .py:

mi_modulo.py:
    '''Mi módulo personalizado.'''

    PI = 3.14159

    def saludar(nombre):
        '''Saluda a alguien.'''
        return f"Hola, {nombre}!"

    def sumar(a, b):
        '''Suma dos números.'''
        return a + b

    class Calculadora:
        '''Calculadora simple.'''
        def multiplicar(self, a, b):
            return a * b

Luego lo importas:
    import mi_modulo
    print(mi_modulo.saludar("Ana"))
    print(mi_modulo.PI)
""")

# Crear módulo de ejemplo en /tmp
import os
modulo_path = "/tmp/mi_modulo_ejemplo.py"
codigo_modulo = '''"""Módulo de ejemplo."""

VERSION = "1.0.0"

def saludar(nombre):
    """Saluda a alguien."""
    return f"¡Hola, {nombre}!"

def duplicar(n):
    """Duplica un número."""
    return n * 2

class Persona:
    """Representa una persona."""
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        return f"Soy {self.nombre}"
'''

with open(modulo_path, 'w') as f:
    f.write(codigo_modulo)

# Importar el módulo creado
import sys
sys.path.insert(0, '/tmp')

import mi_modulo_ejemplo as mme
print(f"Versión: {mme.VERSION}")
print(f"Saludar: {mme.saludar('Python')}")
print(f"Duplicar: {mme.duplicar(21)}")
persona = mme.Persona("Ana")
print(f"Persona: {persona.presentarse()}")


# ==============================================================================
# __name__ Y __main__
# ==============================================================================

print("\n" + "=" * 60)
print("__name__ Y __main__")
print("=" * 60)

print("""
Cada módulo tiene una variable especial __name__:
- Si se ejecuta directamente: __name__ == "__main__"
- Si se importa: __name__ == nombre_del_modulo

Esto permite que un módulo funcione como script o como librería:

    # mi_modulo.py
    def funcion():
        return "Hola"

    if __name__ == "__main__":
        # Este código solo se ejecuta si se corre directamente
        print("Ejecutando como script")
        print(funcion())
    else:
        # Cuando se importa, esto no se ejecuta
        pass

Uso:
    $ python mi_modulo.py      # Ejecuta el bloque __main__
    >>> import mi_modulo       # NO ejecuta el bloque __main__
""")

print(f"__name__ de este archivo: {__name__}")


# ==============================================================================
# PAQUETES
# ==============================================================================

print("\n" + "=" * 60)
print("PAQUETES")
print("=" * 60)

print("""
Un paquete es un directorio con módulos:

mi_paquete/
├── __init__.py      # Marca el directorio como paquete
├── modulo1.py
├── modulo2.py
└── subpaquete/
    ├── __init__.py
    └── modulo3.py

Importar:
    import mi_paquete.modulo1
    from mi_paquete import modulo2
    from mi_paquete.subpaquete import modulo3

__init__.py puede:
    - Estar vacío
    - Inicializar el paquete
    - Definir __all__ para controlar qué se exporta
    - Importar submódulos para acceso más fácil
""")

# Crear estructura de paquete de ejemplo
import os
paquete_dir = "/tmp/mi_paquete"
os.makedirs(f"{paquete_dir}/subpaquete", exist_ok=True)

# __init__.py principal
init_content = '''"""Mi paquete de ejemplo."""
from .utilidades import saludar
from .matematicas import sumar

__version__ = "1.0.0"
__all__ = ["saludar", "sumar", "utilidades", "matematicas"]
'''

# Módulos
utilidades_content = '''"""Módulo de utilidades."""
def saludar(nombre):
    return f"Hola desde utilidades, {nombre}!"
'''

matematicas_content = '''"""Módulo de matemáticas."""
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
'''

# Escribir archivos
with open(f"{paquete_dir}/__init__.py", 'w') as f:
    f.write(init_content)
with open(f"{paquete_dir}/utilidades.py", 'w') as f:
    f.write(utilidades_content)
with open(f"{paquete_dir}/matematicas.py", 'w') as f:
    f.write(matematicas_content)
with open(f"{paquete_dir}/subpaquete/__init__.py", 'w') as f:
    f.write("")

print("Paquete de ejemplo creado en /tmp/mi_paquete")


# ==============================================================================
# INSTALACIÓN DE PAQUETES EXTERNOS (PIP)
# ==============================================================================

print("\n" + "=" * 60)
print("INSTALACIÓN DE PAQUETES (PIP)")
print("=" * 60)

print("""
pip es el gestor de paquetes de Python.

COMANDOS BÁSICOS:
    pip install nombre_paquete       # Instalar
    pip install nombre==1.2.3        # Versión específica
    pip install -r requirements.txt  # Desde archivo
    pip uninstall nombre_paquete     # Desinstalar
    pip list                         # Listar instalados
    pip show nombre_paquete          # Info de paquete
    pip freeze > requirements.txt    # Exportar dependencias

ENTORNOS VIRTUALES (recomendado):
    python -m venv mi_entorno        # Crear entorno
    source mi_entorno/bin/activate   # Activar (Linux/Mac)
    mi_entorno\\Scripts\\activate     # Activar (Windows)
    deactivate                       # Desactivar

PAQUETES POPULARES:
    - requests: HTTP requests
    - numpy: Computación numérica
    - pandas: Análisis de datos
    - flask/django: Web frameworks
    - pytest: Testing
""")


# ==============================================================================
# IMPORTACIONES RELATIVAS Y ABSOLUTAS
# ==============================================================================

print("\n" + "=" * 60)
print("IMPORTACIONES RELATIVAS Y ABSOLUTAS")
print("=" * 60)

print("""
ABSOLUTAS (recomendadas generalmente):
    from mi_paquete.modulo import funcion
    import mi_paquete.subpaquete.modulo

RELATIVAS (dentro de un paquete):
    from . import modulo           # Del mismo directorio
    from .modulo import funcion    # Función de módulo hermano
    from .. import otro_modulo     # Del directorio padre
    from ..subpaquete import x     # De paquete hermano

Las importaciones relativas solo funcionan dentro de paquetes.
""")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Verificar si un módulo está instalado
print("--- Verificar módulos ---")
def modulo_instalado(nombre):
    try:
        __import__(nombre)
        return True
    except ImportError:
        return False

modulos = ["os", "sys", "numpy", "pandas", "requests", "modulo_ficticio"]
for mod in modulos:
    estado = "✓" if modulo_instalado(mod) else "✗"
    print(f"  {mod}: {estado}")

# 2. Información de módulo
print("\n--- Info de módulo ---")
import math
print(f"Nombre: {math.__name__}")
print(f"Archivo: {math.__file__ if hasattr(math, '__file__') else 'built-in'}")
print(f"Funciones disponibles: {[x for x in dir(math) if not x.startswith('_')][:10]}...")

# 3. Cargar módulo dinámicamente
print("\n--- Importación dinámica ---")
nombre_modulo = "json"
modulo = __import__(nombre_modulo)
datos = modulo.dumps({"clave": "valor"})
print(f"Cargado '{nombre_modulo}' dinámicamente: {datos}")

# Otra forma más moderna
from importlib import import_module
modulo2 = import_module("collections")
print(f"Counter disponible: {hasattr(modulo2, 'Counter')}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea un módulo 'utilidades.py' con funciones:
   - es_par(n): verifica si n es par
   - invertir_string(s): invierte un string
   - contar_vocales(s): cuenta vocales

2. Crea un paquete 'geometria' con módulos:
   - circulo.py: area, perimetro
   - rectangulo.py: area, perimetro
   - triangulo.py: area, perimetro

3. Escribe un script que liste todos los módulos
   importados y su ubicación

4. Crea un módulo que funcione como script y como librería:
   - Como librería: exporta funciones
   - Como script: ejecuta demo de las funciones

5. Implementa un sistema de plugins simple donde
   el programa cargue módulos de un directorio dinámicamente

6. Crea un requirements.txt y un script que verifique
   si todas las dependencias están instaladas
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 16_poo_basico.py")
print("=" * 60)
