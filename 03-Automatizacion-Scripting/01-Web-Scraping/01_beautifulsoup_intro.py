"""
================================================================================
WEB SCRAPING CON BEAUTIFULSOUP
================================================================================

¿QUÉ ES WEB SCRAPING?
--------------------
Web scraping es la extracción automática de datos de páginas web.
Se usa para:
- Recopilar precios de productos
- Extraer noticias y artículos
- Monitorear cambios en sitios web
- Crear datasets para ML

CONSIDERACIONES ÉTICAS Y LEGALES:
--------------------------------
1. Revisa el robots.txt del sitio (ejemplo.com/robots.txt)
2. Respeta los términos de servicio
3. No sobrecargues el servidor (añade delays)
4. Considera usar APIs oficiales si existen
5. Identifícate con un User-Agent apropiado

LIBRERÍAS PRINCIPALES:
---------------------
- requests: Para hacer peticiones HTTP
- BeautifulSoup: Para parsear HTML
- Selenium: Para sitios con JavaScript
- Scrapy: Framework completo para scraping

INSTALACIÓN:
    pip install requests beautifulsoup4 lxml

================================================================================
"""

print("=" * 60)
print("WEB SCRAPING CON BEAUTIFULSOUP")
print("=" * 60)

try:
    import requests
    from bs4 import BeautifulSoup
    LIBS_DISPONIBLES = True
    print("Librerías importadas correctamente")
except ImportError as e:
    print(f"Error importando: {e}")
    print("Instala con: pip install requests beautifulsoup4")
    LIBS_DISPONIBLES = False


# ==============================================================================
# CONCEPTOS BÁSICOS DE HTML
# ==============================================================================

print("\n" + "=" * 60)
print("REPASO: Estructura HTML")
print("=" * 60)

print("""
HTML es el lenguaje de marcado de las páginas web.

Estructura básica:
<html>
  <head>
    <title>Título de la página</title>
  </head>
  <body>
    <h1>Encabezado</h1>
    <p class="intro">Un párrafo con clase "intro"</p>
    <a href="https://ejemplo.com" id="enlace1">Un enlace</a>
    <div class="contenedor">
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
    </div>
  </body>
</html>

SELECTORES IMPORTANTES:
- tag: Nombre del elemento (p, div, a, h1)
- class: Atributo que agrupa elementos (.clase)
- id: Identificador único (#id)
- atributos: href, src, data-*, etc.
""")


# ==============================================================================
# EJEMPLO CON HTML LOCAL
# ==============================================================================

if LIBS_DISPONIBLES:
    print("\n" + "=" * 60)
    print("EJEMPLO 1: Parsear HTML local")
    print("=" * 60)

    html_ejemplo = """
    <html>
    <body>
        <h1>Productos en oferta</h1>
        <div class="producto">
            <h2 class="nombre">Laptop HP</h2>
            <span class="precio">$899.99</span>
            <p class="descripcion">Laptop potente para trabajo</p>
        </div>
        <div class="producto">
            <h2 class="nombre">Monitor Samsung</h2>
            <span class="precio">$299.99</span>
            <p class="descripcion">Monitor 4K 27 pulgadas</p>
        </div>
        <div class="producto destacado">
            <h2 class="nombre">Teclado Mecánico</h2>
            <span class="precio">$149.99</span>
            <p class="descripcion">Teclado RGB gaming</p>
        </div>
    </body>
    </html>
    """

    # Crear objeto BeautifulSoup
    soup = BeautifulSoup(html_ejemplo, 'lxml')

    # ENCONTRAR ELEMENTOS
    print("\n--- Métodos de búsqueda ---\n")

    # find() - Encuentra el PRIMER elemento que coincide
    titulo = soup.find('h1')
    print(f"find('h1'): {titulo.text}")

    # find_all() - Encuentra TODOS los elementos
    productos = soup.find_all('div', class_='producto')
    print(f"find_all('div', class_='producto'): {len(productos)} elementos")

    # Buscar por clase
    destacado = soup.find('div', class_='destacado')
    print(f"Producto destacado: {destacado.find('h2').text if destacado else 'No encontrado'}")

    # EXTRAER INFORMACIÓN
    print("\n--- Extraer datos de productos ---\n")

    for producto in productos:
        nombre = producto.find('h2', class_='nombre').text
        precio = producto.find('span', class_='precio').text
        descripcion = producto.find('p', class_='descripcion').text

        print(f"Producto: {nombre}")
        print(f"  Precio: {precio}")
        print(f"  Descripción: {descripcion}")
        print()


# ==============================================================================
# SELECTORES CSS
# ==============================================================================

if LIBS_DISPONIBLES:
    print("=" * 60)
    print("SELECTORES CSS con select()")
    print("=" * 60)

    print("""
    select() usa selectores CSS, más potentes y familiares:

    soup.select('tag')           # Por tag
    soup.select('.clase')        # Por clase
    soup.select('#id')           # Por ID
    soup.select('div.clase')     # Tag con clase
    soup.select('div p')         # p dentro de div
    soup.select('div > p')       # p hijo directo de div
    soup.select('a[href]')       # a con atributo href
    soup.select('[data-id="5"]') # Atributo específico
    """)

    # Ejemplos con selectores CSS
    precios = soup.select('.precio')
    print(f"Todos los precios: {[p.text for p in precios]}")

    nombres = soup.select('.producto .nombre')
    print(f"Todos los nombres: {[n.text for n in nombres]}")


# ==============================================================================
# HACER PETICIONES HTTP
# ==============================================================================

if LIBS_DISPONIBLES:
    print("\n" + "=" * 60)
    print("PETICIONES HTTP con requests")
    print("=" * 60)

    print("""
    # GET request básico
    response = requests.get('https://ejemplo.com')

    # Con headers personalizados
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)

    # Con parámetros
    params = {'q': 'python', 'page': 1}
    response = requests.get(url, params=params)

    # Verificar respuesta
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
    """)

    # Ejemplo real (sitio que permite scraping)
    print("\n--- Ejemplo: Scraping de Wikipedia ---")

    try:
        url = "https://es.wikipedia.org/wiki/Python"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Educational Bot)'
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            # Obtener título
            titulo = soup.find('h1', id='firstHeading')
            print(f"Título: {titulo.text if titulo else 'No encontrado'}")

            # Contar párrafos
            parrafos = soup.select('#mw-content-text p')
            print(f"Número de párrafos: {len(parrafos)}")

            # Primer párrafo (resumen)
            if parrafos:
                primer_parrafo = parrafos[0].text[:200]
                print(f"Resumen: {primer_parrafo}...")
        else:
            print(f"Error: {response.status_code}")

    except Exception as e:
        print(f"Error en la petición: {e}")


# ==============================================================================
# EXTRAER ENLACES E IMÁGENES
# ==============================================================================

if LIBS_DISPONIBLES:
    print("\n" + "=" * 60)
    print("EXTRAER ENLACES E IMÁGENES")
    print("=" * 60)

    html_enlaces = """
    <html>
    <body>
        <a href="https://google.com">Google</a>
        <a href="https://github.com">GitHub</a>
        <a href="/pagina-interna">Página interna</a>
        <img src="imagen1.jpg" alt="Imagen 1">
        <img src="https://ejemplo.com/imagen2.png" alt="Imagen 2">
    </body>
    </html>
    """

    soup = BeautifulSoup(html_enlaces, 'lxml')

    # Extraer todos los enlaces
    print("Enlaces encontrados:")
    for enlace in soup.find_all('a'):
        texto = enlace.text
        href = enlace.get('href')
        print(f"  {texto}: {href}")

    # Extraer todas las imágenes
    print("\nImágenes encontradas:")
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt', 'Sin descripción')
        print(f"  {alt}: {src}")


# ==============================================================================
# BUENAS PRÁCTICAS
# ==============================================================================

print("\n" + "=" * 60)
print("BUENAS PRÁCTICAS DE WEB SCRAPING")
print("=" * 60)

print("""
1. RESPETAR AL SERVIDOR:
   import time
   time.sleep(1)  # Esperar entre peticiones

2. MANEJAR ERRORES:
   try:
       response = requests.get(url, timeout=10)
       response.raise_for_status()
   except requests.RequestException as e:
       print(f"Error: {e}")

3. USAR SESIONES (mantiene cookies, más eficiente):
   session = requests.Session()
   session.headers.update({'User-Agent': 'Mi Bot'})
   response = session.get(url1)
   response = session.get(url2)

4. GUARDAR DATOS:
   import json
   with open('datos.json', 'w') as f:
       json.dump(datos, f, indent=2)

5. PARA SITIOS CON JAVASCRIPT:
   - Usa Selenium o Playwright
   - O busca la API que usa el sitio
""")


# ==============================================================================
# EJEMPLO COMPLETO
# ==============================================================================

if LIBS_DISPONIBLES:
    print("\n" + "=" * 60)
    print("EJEMPLO COMPLETO: Scraper de noticias")
    print("=" * 60)

    def scrape_ejemplo():
        """
        Ejemplo de scraper estructurado.
        """
        import time

        class NoticiasScraper:
            def __init__(self):
                self.session = requests.Session()
                self.session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Educational Bot)'
                })
                self.datos = []

            def obtener_pagina(self, url):
                """Obtiene y parsea una página."""
                try:
                    response = self.session.get(url, timeout=10)
                    response.raise_for_status()
                    return BeautifulSoup(response.text, 'lxml')
                except requests.RequestException as e:
                    print(f"Error obteniendo {url}: {e}")
                    return None

            def extraer_titulares(self, soup):
                """Extrae titulares de la página."""
                titulares = []
                # Esto dependería de la estructura real del sitio
                for h2 in soup.find_all('h2')[:5]:
                    titulares.append(h2.text.strip())
                return titulares

            def guardar_json(self, archivo):
                """Guarda los datos en JSON."""
                import json
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(self.datos, f, indent=2, ensure_ascii=False)
                print(f"Datos guardados en {archivo}")

        print("Estructura de un scraper:")
        print("1. Clase con sesión persistente")
        print("2. Métodos separados para cada tarea")
        print("3. Manejo de errores")
        print("4. Delays entre peticiones")
        print("5. Guardado de datos")

    scrape_ejemplo()

print("\n" + "=" * 60)
print("PRÓXIMO: 02_selenium_dinamico.py (sitios con JavaScript)")
print("=" * 60)
