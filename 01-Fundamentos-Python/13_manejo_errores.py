"""
================================================================================
MANEJO DE ERRORES Y EXCEPCIONES
================================================================================

Los errores son inevitables en programación.
Python proporciona mecanismos para manejarlos elegantemente.

TIPOS DE ERRORES:
1. Errores de sintaxis: código mal escrito (detectados antes de ejecutar)
2. Excepciones: errores durante la ejecución

MANEJO DE EXCEPCIONES:
- try: código que puede fallar
- except: qué hacer si falla
- else: qué hacer si NO falla
- finally: siempre se ejecuta

================================================================================
"""

# ==============================================================================
# TIPOS COMUNES DE EXCEPCIONES
# ==============================================================================

print("=" * 60)
print("TIPOS COMUNES DE EXCEPCIONES")
print("=" * 60)

print("""
EXCEPCIONES FRECUENTES:

SyntaxError       - Error de sintaxis (código mal escrito)
NameError         - Variable no definida
TypeError         - Operación con tipo incorrecto
ValueError        - Valor inapropiado
IndexError        - Índice fuera de rango
KeyError          - Clave no existe en diccionario
ZeroDivisionError - División por cero
FileNotFoundError - Archivo no encontrado
AttributeError    - Atributo no existe
ImportError       - No se puede importar módulo
""")

# Ejemplos (comentados para no detener el script)
"""
# NameError
print(variable_no_definida)

# TypeError
"texto" + 5

# ValueError
int("no es numero")

# IndexError
lista = [1, 2, 3]
lista[10]

# KeyError
diccionario = {"a": 1}
diccionario["z"]

# ZeroDivisionError
10 / 0
"""


# ==============================================================================
# TRY - EXCEPT BÁSICO
# ==============================================================================

print("\n" + "=" * 60)
print("TRY - EXCEPT BÁSICO")
print("=" * 60)

# Sin manejo de errores
print("--- Sin manejo de errores ---")
# resultado = 10 / 0  # Esto detendría el programa

# Con try-except
print("\n--- Con try-except ---")
try:
    resultado = 10 / 0
except:
    print("¡Ocurrió un error!")

print("El programa continúa...")

# Capturar excepción específica
print("\n--- Excepción específica ---")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

# Capturar el objeto excepción
print("\n--- Capturar objeto excepción ---")
try:
    numero = int("abc")
except ValueError as e:
    print(f"Error de valor: {e}")


# ==============================================================================
# MÚLTIPLES EXCEPCIONES
# ==============================================================================

print("\n" + "=" * 60)
print("MÚLTIPLES EXCEPCIONES")
print("=" * 60)

def dividir_elemento(lista, indice, divisor):
    """Función que puede generar varios tipos de errores."""
    try:
        valor = lista[indice]
        resultado = valor / divisor
        return resultado
    except IndexError:
        print(f"Error: Índice {indice} fuera de rango")
    except ZeroDivisionError:
        print("Error: División por cero")
    except TypeError:
        print("Error: Tipo de dato incorrecto")
    return None

numeros = [10, 20, 30]

print("Pruebas de múltiples excepciones:")
print(f"  dividir_elemento([10,20,30], 1, 2) = {dividir_elemento(numeros, 1, 2)}")
dividir_elemento(numeros, 10, 2)   # IndexError
dividir_elemento(numeros, 0, 0)    # ZeroDivisionError
dividir_elemento(numeros, 0, "a")  # TypeError

# Capturar múltiples en una línea
print("\n--- Múltiples en una línea ---")
try:
    # resultado = 10 / 0
    resultado = int("abc")
except (ZeroDivisionError, ValueError) as e:
    print(f"Error numérico: {e}")


# ==============================================================================
# ELSE Y FINALLY
# ==============================================================================

print("\n" + "=" * 60)
print("ELSE Y FINALLY")
print("=" * 60)

print("""
try:
    # código que puede fallar
except ExcepcionTipo:
    # si hay error de ese tipo
else:
    # si NO hay ningún error
finally:
    # SIEMPRE se ejecuta (haya error o no)
""")

def dividir_con_log(a, b):
    """Ejemplo completo de try-except-else-finally."""
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("  [ERROR] División por cero")
        return None
    except TypeError:
        print("  [ERROR] Tipos inválidos")
        return None
    else:
        print(f"  [OK] División exitosa: {a}/{b}")
        return resultado
    finally:
        print("  [LOG] Operación de división completada")

print("Caso exitoso:")
dividir_con_log(10, 2)

print("\nCaso con error:")
dividir_con_log(10, 0)


# ==============================================================================
# LEVANTAR EXCEPCIONES (RAISE)
# ==============================================================================

print("\n" + "=" * 60)
print("LEVANTAR EXCEPCIONES (RAISE)")
print("=" * 60)

def validar_edad(edad):
    """Valida que la edad sea válida."""
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("La edad parece irreal")
    return True

print("Validar edades:")
try:
    validar_edad(25)
    print("  25: válida")
except (TypeError, ValueError) as e:
    print(f"  25: {e}")

try:
    validar_edad(-5)
except ValueError as e:
    print(f"  -5: {e}")

try:
    validar_edad("veinte")
except TypeError as e:
    print(f"  'veinte': {e}")

# Re-lanzar excepción
print("\n--- Re-lanzar excepción ---")
def procesar_dato(dato):
    try:
        return int(dato)
    except ValueError:
        print(f"  Advertencia: '{dato}' no es un número, propagando error...")
        raise  # Re-lanza la misma excepción

try:
    procesar_dato("abc")
except ValueError:
    print("  Error capturado en el nivel superior")


# ==============================================================================
# EXCEPCIONES PERSONALIZADAS
# ==============================================================================

print("\n" + "=" * 60)
print("EXCEPCIONES PERSONALIZADAS")
print("=" * 60)

class SaldoInsuficienteError(Exception):
    """Excepción para cuando no hay suficiente saldo."""

    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.faltante = cantidad - saldo
        mensaje = f"Saldo insuficiente. Tienes ${saldo}, necesitas ${cantidad}"
        super().__init__(mensaje)


class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        return self.saldo


print("Uso de excepción personalizada:")
cuenta = CuentaBancaria(100)

try:
    cuenta.retirar(50)
    print(f"  Retiro de $50 exitoso. Saldo: ${cuenta.saldo}")
    cuenta.retirar(80)
except SaldoInsuficienteError as e:
    print(f"  Error: {e}")
    print(f"  Te faltan: ${e.faltante}")


# ==============================================================================
# CONTEXT MANAGERS (WITH)
# ==============================================================================

print("\n" + "=" * 60)
print("CONTEXT MANAGERS (WITH)")
print("=" * 60)

print("""
'with' garantiza que los recursos se liberen correctamente,
incluso si ocurre una excepción.

Equivalente a try-finally pero más limpio.
""")

# Ejemplo con archivos
print("--- Con archivos ---")
# Sin with (forma antigua):
# archivo = open('archivo.txt', 'r')
# try:
#     contenido = archivo.read()
# finally:
#     archivo.close()

# Con with (forma moderna):
# with open('archivo.txt', 'r') as archivo:
#     contenido = archivo.read()
# # archivo se cierra automáticamente

# Crear context manager propio
class Temporizador:
    """Context manager que mide tiempo de ejecución."""

    def __enter__(self):
        import time
        self.inicio = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.fin = time.time()
        self.duracion = self.fin - self.inicio
        print(f"  Tiempo: {self.duracion:.4f} segundos")
        return False  # No suprimir excepciones

print("\nUso de context manager propio:")
with Temporizador():
    # Simular trabajo
    total = sum(range(1000000))
    print(f"  Suma calculada: {total}")


# ==============================================================================
# BUENAS PRÁCTICAS
# ==============================================================================

print("\n" + "=" * 60)
print("BUENAS PRÁCTICAS")
print("=" * 60)

print("""
1. NO usar except sin especificar tipo:
   ✗ except:           # Captura TODO, incluso Ctrl+C
   ✓ except Exception: # Captura errores comunes

2. Capturar excepciones específicas:
   ✗ except Exception as e:
   ✓ except (ValueError, TypeError) as e:

3. No silenciar excepciones sin razón:
   ✗ except: pass
   ✓ except ValueError: log_error(); return default

4. Usar finally para limpieza:
   - Cerrar archivos
   - Liberar recursos
   - Restaurar estado

5. Crear excepciones descriptivas:
   - Nombres claros que indiquen el problema
   - Incluir información útil en el mensaje

6. Documentar excepciones en docstrings:
   def funcion():
       '''
       Raises:
           ValueError: Si el valor es negativo
       '''
""")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Entrada de usuario robusta
print("--- Entrada robusta ---")
def obtener_numero(prompt, intentos=3):
    """Pide un número al usuario con reintentos."""
    for intento in range(intentos):
        try:
            # Simulamos entrada
            entradas = ["abc", "3.14", "42"]
            entrada = entradas[intento]
            print(f"  Intento {intento + 1}: '{entrada}'")
            return int(entrada)
        except ValueError:
            print(f"    No es un número válido")
    raise ValueError(f"No se pudo obtener número en {intentos} intentos")

try:
    numero = obtener_numero("Ingresa un número: ")
    print(f"  Número obtenido: {numero}")
except ValueError as e:
    print(f"  Error final: {e}")

# 2. API con manejo de errores
print("\n--- Simulación de API ---")
import random

def llamar_api_simulada():
    """Simula una llamada a API que puede fallar."""
    resultado = random.choice(["exito", "error", "timeout"])
    if resultado == "error":
        raise ConnectionError("Error de conexión")
    if resultado == "timeout":
        raise TimeoutError("Tiempo de espera agotado")
    return {"status": "ok", "data": [1, 2, 3]}

def obtener_datos_con_reintentos(max_intentos=3):
    """Intenta obtener datos con reintentos."""
    for intento in range(max_intentos):
        try:
            datos = llamar_api_simulada()
            return datos
        except (ConnectionError, TimeoutError) as e:
            print(f"  Intento {intento + 1} falló: {e}")
            if intento == max_intentos - 1:
                raise
    return None

print("Intentando obtener datos:")
random.seed(42)  # Para reproducibilidad
try:
    datos = obtener_datos_con_reintentos()
    print(f"  Datos obtenidos: {datos}")
except Exception as e:
    print(f"  Error después de todos los intentos: {e}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Escribe una función que divida dos números y maneje
   todos los posibles errores (división por cero, tipos)

2. Crea una función que lea un archivo y maneje el caso
   de que no exista, retornando una lista vacía

3. Implementa una función de validación de email que
   lance excepciones descriptivas para cada tipo de error

4. Crea una excepción personalizada PasswordDevilError
   que se lance cuando una contraseña no cumple requisitos

5. Escribe una función que convierta una lista de strings
   a enteros, ignorando los que no se pueden convertir
   pero registrando cuántos fallaron

6. Implementa un context manager que cambie temporalmente
   el directorio de trabajo y lo restaure al salir
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 14_archivos.py")
print("=" * 60)
