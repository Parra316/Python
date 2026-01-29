"""
================================================================================
MANEJO DE ARCHIVOS
================================================================================

Python permite leer y escribir archivos de texto y binarios.
El manejo correcto de archivos es esencial para:
- Guardar datos persistentes
- Leer configuraciones
- Procesar logs
- Importar/exportar datos

MODOS DE APERTURA:
- 'r'  : Lectura (default)
- 'w'  : Escritura (sobrescribe)
- 'a'  : Append (añadir al final)
- 'x'  : Crear (falla si existe)
- 'r+' : Lectura y escritura
- 'b'  : Modo binario (rb, wb)

================================================================================
"""

import os
from pathlib import Path

# Directorio temporal para ejemplos
DIR_TEMP = "/tmp/python_archivos_ejemplo"
os.makedirs(DIR_TEMP, exist_ok=True)

# ==============================================================================
# ABRIR Y CERRAR ARCHIVOS
# ==============================================================================

print("=" * 60)
print("ABRIR Y CERRAR ARCHIVOS")
print("=" * 60)

# Forma antigua (no recomendada)
print("--- Forma antigua ---")
archivo_path = f"{DIR_TEMP}/ejemplo.txt"
archivo = open(archivo_path, 'w')
archivo.write("Hola, mundo!")
archivo.close()
print(f"Archivo creado: {archivo_path}")

# Forma moderna con 'with' (RECOMENDADA)
print("\n--- Con 'with' (recomendado) ---")
with open(archivo_path, 'w') as archivo:
    archivo.write("Hola con with!")
# El archivo se cierra automáticamente
print("Archivo cerrado automáticamente")


# ==============================================================================
# ESCRIBIR ARCHIVOS
# ==============================================================================

print("\n" + "=" * 60)
print("ESCRIBIR ARCHIVOS")
print("=" * 60)

# write() - escribe un string
print("--- write() ---")
with open(f"{DIR_TEMP}/write.txt", 'w') as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")
    f.write("Tercera línea")
print("Archivo escrito con write()")

# writelines() - escribe lista de strings
print("\n--- writelines() ---")
lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
with open(f"{DIR_TEMP}/writelines.txt", 'w') as f:
    f.writelines(lineas)
print("Archivo escrito con writelines()")

# print() con file
print("\n--- print() con file ---")
with open(f"{DIR_TEMP}/print.txt", 'w') as f:
    print("Esto va al archivo", file=f)
    print("También esto", file=f)
    print(f"Y números: {42}", file=f)
print("Archivo escrito con print()")

# Append - añadir al final
print("\n--- Modo append ('a') ---")
with open(f"{DIR_TEMP}/write.txt", 'a') as f:
    f.write("\nLínea añadida al final")
print("Línea añadida al archivo existente")


# ==============================================================================
# LEER ARCHIVOS
# ==============================================================================

print("\n" + "=" * 60)
print("LEER ARCHIVOS")
print("=" * 60)

# Crear archivo de ejemplo
with open(f"{DIR_TEMP}/lectura.txt", 'w') as f:
    f.write("Línea 1: Hola\n")
    f.write("Línea 2: Mundo\n")
    f.write("Línea 3: Python\n")
    f.write("Línea 4: Archivos")

# read() - lee todo el archivo
print("--- read() ---")
with open(f"{DIR_TEMP}/lectura.txt", 'r') as f:
    contenido = f.read()
print(f"Contenido completo:\n{contenido}")

# read(n) - lee n caracteres
print("\n--- read(n) ---")
with open(f"{DIR_TEMP}/lectura.txt", 'r') as f:
    primeros = f.read(20)
print(f"Primeros 20 caracteres: '{primeros}'")

# readline() - lee una línea
print("\n--- readline() ---")
with open(f"{DIR_TEMP}/lectura.txt", 'r') as f:
    linea1 = f.readline()
    linea2 = f.readline()
print(f"Línea 1: {linea1.strip()}")
print(f"Línea 2: {linea2.strip()}")

# readlines() - lista de todas las líneas
print("\n--- readlines() ---")
with open(f"{DIR_TEMP}/lectura.txt", 'r') as f:
    lineas = f.readlines()
print(f"Lista de líneas: {lineas}")

# Iterar directamente (más eficiente en memoria)
print("\n--- Iterar línea por línea ---")
with open(f"{DIR_TEMP}/lectura.txt", 'r') as f:
    for numero, linea in enumerate(f, 1):
        print(f"  {numero}: {linea.strip()}")


# ==============================================================================
# ENCODING
# ==============================================================================

print("\n" + "=" * 60)
print("ENCODING")
print("=" * 60)

print("""
Es importante especificar el encoding para caracteres especiales.
UTF-8 es el estándar recomendado.
""")

# Escribir con caracteres especiales
with open(f"{DIR_TEMP}/unicode.txt", 'w', encoding='utf-8') as f:
    f.write("Español: ñ, á, é, í, ó, ú\n")
    f.write("Japonés: こんにちは\n")
    f.write("Emojis: 🐍 📁 ✨\n")

# Leer
with open(f"{DIR_TEMP}/unicode.txt", 'r', encoding='utf-8') as f:
    print(f.read())


# ==============================================================================
# POSICIÓN EN EL ARCHIVO
# ==============================================================================

print("=" * 60)
print("POSICIÓN EN EL ARCHIVO")
print("=" * 60)

with open(f"{DIR_TEMP}/lectura.txt", 'r') as f:
    print(f"Posición inicial: {f.tell()}")

    f.read(10)
    print(f"Después de leer 10 chars: {f.tell()}")

    f.seek(0)  # Volver al inicio
    print(f"Después de seek(0): {f.tell()}")

    f.seek(0, 2)  # Ir al final (0 desde el final)
    print(f"Al final del archivo: {f.tell()}")


# ==============================================================================
# TRABAJAR CON RUTAS - PATHLIB
# ==============================================================================

print("\n" + "=" * 60)
print("PATHLIB - Manejo moderno de rutas")
print("=" * 60)

# Crear Path
ruta = Path(DIR_TEMP) / "subdir" / "archivo.txt"
print(f"Ruta: {ruta}")
print(f"Nombre: {ruta.name}")
print(f"Extensión: {ruta.suffix}")
print(f"Directorio padre: {ruta.parent}")
print(f"¿Existe?: {ruta.exists()}")

# Crear directorio y archivo
ruta.parent.mkdir(parents=True, exist_ok=True)
ruta.write_text("Contenido usando pathlib")
print(f"\nArchivo creado: {ruta}")

# Leer con pathlib
contenido = ruta.read_text()
print(f"Contenido: {contenido}")

# Listar archivos
print("\n--- Listar archivos ---")
for archivo in Path(DIR_TEMP).glob("**/*.txt"):
    print(f"  {archivo}")

# Información del archivo
if ruta.exists():
    stats = ruta.stat()
    print(f"\nInfo de {ruta.name}:")
    print(f"  Tamaño: {stats.st_size} bytes")


# ==============================================================================
# ARCHIVOS CSV
# ==============================================================================

print("\n" + "=" * 60)
print("ARCHIVOS CSV")
print("=" * 60)

import csv

# Escribir CSV
datos = [
    ["nombre", "edad", "ciudad"],
    ["Ana", 25, "Madrid"],
    ["Luis", 30, "Barcelona"],
    ["María", 28, "Sevilla"]
]

csv_path = f"{DIR_TEMP}/datos.csv"
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(datos)
print(f"CSV escrito: {csv_path}")

# Leer CSV
print("\n--- Leer CSV ---")
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        print(f"  {fila}")

# CSV con diccionarios
print("\n--- CSV con diccionarios ---")
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 30, "ciudad": "Barcelona"}
]

dict_csv_path = f"{DIR_TEMP}/personas.csv"
with open(dict_csv_path, 'w', newline='', encoding='utf-8') as f:
    campos = ["nombre", "edad", "ciudad"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(personas)

# Leer como diccionarios
with open(dict_csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(f"  {dict(fila)}")


# ==============================================================================
# ARCHIVOS JSON
# ==============================================================================

print("\n" + "=" * 60)
print("ARCHIVOS JSON")
print("=" * 60)

import json

datos = {
    "nombre": "Proyecto Python",
    "version": "1.0",
    "autores": ["Ana", "Luis"],
    "configuracion": {
        "debug": True,
        "max_conexiones": 100
    }
}

# Escribir JSON
json_path = f"{DIR_TEMP}/config.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
print(f"JSON escrito: {json_path}")

# Leer JSON
with open(json_path, 'r', encoding='utf-8') as f:
    datos_leidos = json.load(f)
print(f"Datos leídos: {datos_leidos}")

# JSON a string y viceversa
json_string = json.dumps(datos, indent=2)
print(f"\nJSON como string:\n{json_string}")


# ==============================================================================
# ARCHIVOS BINARIOS
# ==============================================================================

print("\n" + "=" * 60)
print("ARCHIVOS BINARIOS")
print("=" * 60)

# Escribir bytes
bytes_data = bytes([0, 1, 2, 3, 255, 254, 253])
bin_path = f"{DIR_TEMP}/datos.bin"
with open(bin_path, 'wb') as f:
    f.write(bytes_data)
print(f"Bytes escritos: {list(bytes_data)}")

# Leer bytes
with open(bin_path, 'rb') as f:
    datos_bin = f.read()
print(f"Bytes leídos: {list(datos_bin)}")


# ==============================================================================
# EJEMPLOS PRÁCTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLOS PRÁCTICOS")
print("=" * 60)

# 1. Procesar log
print("--- Procesar archivo de log ---")
log_content = """2024-01-15 10:00:00 INFO Usuario conectado
2024-01-15 10:00:05 ERROR Base de datos no responde
2024-01-15 10:00:10 INFO Reintentando conexión
2024-01-15 10:00:15 ERROR Timeout de conexión
2024-01-15 10:00:20 INFO Conexión restaurada"""

log_path = f"{DIR_TEMP}/app.log"
Path(log_path).write_text(log_content)

# Contar errores
errores = 0
with open(log_path, 'r') as f:
    for linea in f:
        if 'ERROR' in linea:
            errores += 1
            print(f"  {linea.strip()}")
print(f"Total de errores: {errores}")

# 2. Configuración persistente
print("\n--- Configuración persistente ---")
def cargar_config(path):
    """Carga configuración desde JSON o crea default."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        config_default = {"tema": "claro", "idioma": "es"}
        guardar_config(path, config_default)
        return config_default

def guardar_config(path, config):
    """Guarda configuración en JSON."""
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)

config_path = f"{DIR_TEMP}/user_config.json"
config = cargar_config(config_path)
print(f"Configuración: {config}")

config["tema"] = "oscuro"
guardar_config(config_path, config)
print(f"Configuración actualizada: {cargar_config(config_path)}")


# ==============================================================================
# LIMPIEZA
# ==============================================================================

print("\n" + "=" * 60)
print("LIMPIEZA")
print("=" * 60)

# Limpiar archivos de ejemplo (opcional)
import shutil
# shutil.rmtree(DIR_TEMP)  # Descomentar para limpiar
print(f"Archivos de ejemplo en: {DIR_TEMP}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Escribe un programa que lea un archivo de texto y cuente:
   - Número de líneas
   - Número de palabras
   - Número de caracteres

2. Crea una función que lea un CSV de productos y retorne
   el producto más caro y el más barato

3. Implementa un sistema simple de notas que:
   - Guarde notas en un archivo JSON
   - Permita añadir, listar y eliminar notas

4. Escribe un programa que busque una palabra en todos
   los archivos .txt de un directorio

5. Crea una función que copie un archivo línea por línea,
   añadiendo números de línea

6. Implementa un "tail" simple que muestre las últimas
   N líneas de un archivo
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 15_modulos_paquetes.py")
print("=" * 60)
