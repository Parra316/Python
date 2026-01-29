"""
================================================================================
AUTOMATIZACIÓN DE TAREAS CON PYTHON
================================================================================

Python es excelente para automatizar tareas repetitivas:
- Organizar y renombrar archivos
- Procesar documentos en masa
- Generar reportes
- Enviar emails automáticos
- Interactuar con APIs

Este archivo cubre la automatización de tareas con archivos.

================================================================================
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

# ==============================================================================
# PATHLIB: MANEJO MODERNO DE RUTAS
# ==============================================================================

print("=" * 60)
print("PATHLIB: Manejo moderno de rutas")
print("=" * 60)

print("""
pathlib es la forma moderna de manejar rutas en Python 3.
Ventajas sobre os.path:
- API orientada a objetos
- Multiplataforma automáticamente
- Más legible y conciso
""")

# Crear objeto Path
ruta = Path('/tmp/ejemplo')
print(f"Ruta: {ruta}")
print(f"Nombre: {ruta.name}")
print(f"Padre: {ruta.parent}")
print(f"Sufijo: {ruta.suffix}")
print(f"Existe: {ruta.exists()}")

# Operaciones comunes
print("\n--- Operaciones con Path ---")
print(f"Ruta actual: {Path.cwd()}")
print(f"Home: {Path.home()}")

# Unir rutas con /
nueva_ruta = Path.home() / 'Documentos' / 'archivo.txt'
print(f"Ruta unida: {nueva_ruta}")

# Glob: buscar archivos
print(f"\nArchivos .py en /tmp:")
for archivo in Path('/tmp').glob('*.py'):
    print(f"  {archivo.name}")


# ==============================================================================
# CREAR Y ORGANIZAR DIRECTORIOS
# ==============================================================================

print("\n" + "=" * 60)
print("CREAR Y ORGANIZAR DIRECTORIOS")
print("=" * 60)


def crear_estructura_proyecto(nombre_proyecto, base_dir='/tmp'):
    """
    Crea una estructura de directorios para un proyecto Python.
    """
    base = Path(base_dir) / nombre_proyecto

    # Estructura de directorios
    directorios = [
        base / 'src',
        base / 'tests',
        base / 'docs',
        base / 'data' / 'raw',
        base / 'data' / 'processed',
        base / 'notebooks',
        base / 'config'
    ]

    # Crear directorios
    for directorio in directorios:
        directorio.mkdir(parents=True, exist_ok=True)
        print(f"  Creado: {directorio}")

    # Crear archivos iniciales
    archivos = {
        base / 'README.md': f"# {nombre_proyecto}\n\nDescripción del proyecto.",
        base / 'requirements.txt': "pandas\nnumpy\nrequests\n",
        base / 'src' / '__init__.py': "",
        base / 'tests' / '__init__.py': "",
        base / '.gitignore': "*.pyc\n__pycache__/\n.env\ndata/\n"
    }

    for archivo, contenido in archivos.items():
        archivo.write_text(contenido)
        print(f"  Archivo: {archivo.name}")

    return base


# Crear proyecto de ejemplo
print("\nCreando estructura de proyecto:")
proyecto = crear_estructura_proyecto('mi_proyecto')


# ==============================================================================
# ORGANIZAR ARCHIVOS POR TIPO
# ==============================================================================

print("\n" + "=" * 60)
print("ORGANIZAR ARCHIVOS POR TIPO")
print("=" * 60)


def organizar_archivos_por_extension(directorio_origen, directorio_destino=None):
    """
    Organiza archivos en carpetas según su extensión.

    Por ejemplo:
    - archivo.pdf → PDFs/archivo.pdf
    - foto.jpg → Imagenes/foto.jpg
    """
    origen = Path(directorio_origen)
    destino = Path(directorio_destino) if directorio_destino else origen / 'Organizado'

    # Mapeo de extensiones a carpetas
    categorias = {
        'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
        'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac'],
        'Codigo': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
        'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz']
    }

    # Invertir mapeo para búsqueda rápida
    extension_a_categoria = {}
    for categoria, extensiones in categorias.items():
        for ext in extensiones:
            extension_a_categoria[ext.lower()] = categoria

    # Procesar archivos
    archivos_movidos = 0
    for archivo in origen.iterdir():
        if archivo.is_file():
            extension = archivo.suffix.lower()
            categoria = extension_a_categoria.get(extension, 'Otros')

            # Crear carpeta de categoría
            carpeta_destino = destino / categoria
            carpeta_destino.mkdir(parents=True, exist_ok=True)

            # Mover archivo
            nuevo_path = carpeta_destino / archivo.name
            # shutil.move(str(archivo), str(nuevo_path))  # Descomentar para mover
            print(f"  {archivo.name} → {categoria}/")
            archivos_movidos += 1

    return archivos_movidos


print("\nEjemplo de organización (simulado):")
print("Archivos serían organizados así:")
# organizar_archivos_por_extension('/ruta/a/organizar')


# ==============================================================================
# RENOMBRAR ARCHIVOS EN MASA
# ==============================================================================

print("\n" + "=" * 60)
print("RENOMBRAR ARCHIVOS EN MASA")
print("=" * 60)


def renombrar_con_patron(directorio, patron_buscar, patron_reemplazar):
    """
    Renombra archivos que coinciden con un patrón.
    """
    directorio = Path(directorio)
    archivos_renombrados = []

    for archivo in directorio.iterdir():
        if archivo.is_file() and patron_buscar in archivo.name:
            nuevo_nombre = archivo.name.replace(patron_buscar, patron_reemplazar)
            nuevo_path = archivo.parent / nuevo_nombre
            # archivo.rename(nuevo_path)  # Descomentar para renombrar
            archivos_renombrados.append((archivo.name, nuevo_nombre))

    return archivos_renombrados


def renombrar_con_fecha(directorio, prefijo=''):
    """
    Renombra archivos añadiendo la fecha de modificación.
    """
    directorio = Path(directorio)

    for archivo in directorio.iterdir():
        if archivo.is_file():
            # Obtener fecha de modificación
            timestamp = archivo.stat().st_mtime
            fecha = datetime.fromtimestamp(timestamp).strftime('%Y%m%d')

            # Nuevo nombre
            nuevo_nombre = f"{prefijo}{fecha}_{archivo.name}"
            print(f"  {archivo.name} → {nuevo_nombre}")


def renombrar_secuencial(directorio, prefijo='archivo', extension=None):
    """
    Renombra archivos secuencialmente: prefijo_001, prefijo_002, etc.
    """
    directorio = Path(directorio)
    archivos = sorted(directorio.iterdir())

    for i, archivo in enumerate(archivos, 1):
        if archivo.is_file():
            ext = extension or archivo.suffix
            nuevo_nombre = f"{prefijo}_{i:03d}{ext}"
            print(f"  {archivo.name} → {nuevo_nombre}")


print("Ejemplos de renombrado:")
print("\n1. Reemplazar patrón:")
print("   'foto_vieja_001.jpg' → 'foto_nueva_001.jpg'")

print("\n2. Añadir fecha:")
print("   'documento.pdf' → '20240115_documento.pdf'")

print("\n3. Secuencial:")
print("   archivos varios → archivo_001.jpg, archivo_002.jpg, ...")


# ==============================================================================
# BUSCAR ARCHIVOS
# ==============================================================================

print("\n" + "=" * 60)
print("BUSCAR ARCHIVOS")
print("=" * 60)


def buscar_archivos(directorio, patron='*', recursivo=True):
    """
    Busca archivos que coincidan con un patrón.
    """
    directorio = Path(directorio)
    metodo = directorio.rglob if recursivo else directorio.glob
    return list(metodo(patron))


def buscar_archivos_grandes(directorio, tamano_minimo_mb=100):
    """
    Encuentra archivos más grandes que el tamaño especificado.
    """
    directorio = Path(directorio)
    tamano_bytes = tamano_minimo_mb * 1024 * 1024
    archivos_grandes = []

    for archivo in directorio.rglob('*'):
        if archivo.is_file():
            try:
                tamano = archivo.stat().st_size
                if tamano > tamano_bytes:
                    archivos_grandes.append({
                        'archivo': archivo,
                        'tamano_mb': tamano / (1024 * 1024)
                    })
            except (PermissionError, OSError):
                continue

    return sorted(archivos_grandes, key=lambda x: x['tamano_mb'], reverse=True)


def buscar_duplicados(directorio):
    """
    Encuentra archivos duplicados basándose en nombre y tamaño.
    Para mayor precisión, usar hash (md5/sha256).
    """
    from collections import defaultdict
    directorio = Path(directorio)
    archivos_por_tamano = defaultdict(list)

    for archivo in directorio.rglob('*'):
        if archivo.is_file():
            try:
                tamano = archivo.stat().st_size
                archivos_por_tamano[(archivo.name, tamano)].append(archivo)
            except (PermissionError, OSError):
                continue

    # Filtrar solo los que tienen duplicados
    duplicados = {k: v for k, v in archivos_por_tamano.items() if len(v) > 1}
    return duplicados


print("Funciones de búsqueda disponibles:")
print("  buscar_archivos(dir, patron='*.py', recursivo=True)")
print("  buscar_archivos_grandes(dir, tamano_minimo_mb=100)")
print("  buscar_duplicados(dir)")


# ==============================================================================
# PROCESAMIENTO DE ARCHIVOS DE TEXTO
# ==============================================================================

print("\n" + "=" * 60)
print("PROCESAMIENTO DE ARCHIVOS DE TEXTO")
print("=" * 60)


def procesar_logs(directorio, patron_fecha=r'\d{4}-\d{2}-\d{2}'):
    """
    Ejemplo: Procesar archivos de log para extraer errores.
    """
    import re
    directorio = Path(directorio)
    errores = []

    for log_file in directorio.glob('*.log'):
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            for linea in f:
                if 'ERROR' in linea or 'Exception' in linea:
                    errores.append({
                        'archivo': log_file.name,
                        'linea': linea.strip()
                    })

    return errores


def combinar_archivos(directorio, patron, archivo_salida):
    """
    Combina múltiples archivos de texto en uno solo.
    """
    directorio = Path(directorio)
    with open(archivo_salida, 'w', encoding='utf-8') as salida:
        for archivo in sorted(directorio.glob(patron)):
            salida.write(f"\n--- {archivo.name} ---\n")
            with open(archivo, 'r', encoding='utf-8') as f:
                salida.write(f.read())

    print(f"Archivos combinados en: {archivo_salida}")


def reemplazar_en_archivos(directorio, buscar, reemplazar, extension='*.txt'):
    """
    Busca y reemplaza texto en múltiples archivos.
    """
    directorio = Path(directorio)
    archivos_modificados = 0

    for archivo in directorio.rglob(extension):
        try:
            contenido = archivo.read_text(encoding='utf-8')
            if buscar in contenido:
                nuevo_contenido = contenido.replace(buscar, reemplazar)
                # archivo.write_text(nuevo_contenido)  # Descomentar para aplicar
                archivos_modificados += 1
                print(f"  Modificado: {archivo}")
        except (PermissionError, UnicodeDecodeError):
            continue

    return archivos_modificados


print("Funciones de procesamiento:")
print("  procesar_logs(dir) - Extraer errores de logs")
print("  combinar_archivos(dir, '*.csv', 'todo.csv') - Unir archivos")
print("  reemplazar_en_archivos(dir, 'viejo', 'nuevo') - Buscar/reemplazar")


# ==============================================================================
# BACKUP AUTOMÁTICO
# ==============================================================================

print("\n" + "=" * 60)
print("BACKUP AUTOMÁTICO")
print("=" * 60)


def crear_backup(directorio_origen, directorio_backup='/tmp/backups'):
    """
    Crea un backup comprimido con fecha.
    """
    origen = Path(directorio_origen)
    backup_dir = Path(directorio_backup)
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Nombre del backup con fecha
    fecha = datetime.now().strftime('%Y%m%d_%H%M%S')
    nombre_backup = f"{origen.name}_backup_{fecha}"

    # Crear archivo comprimido
    archivo_backup = backup_dir / nombre_backup
    shutil.make_archive(
        str(archivo_backup),
        'zip',
        str(origen.parent),
        origen.name
    )

    print(f"Backup creado: {archivo_backup}.zip")
    return f"{archivo_backup}.zip"


print("Ejemplo de uso:")
print("  crear_backup('/ruta/proyecto', '/backups')")
print("  → /backups/proyecto_backup_20240115_143022.zip")


print("\n" + "=" * 60)
print("PRÓXIMO: 02_emails_automaticos.py")
print("=" * 60)
