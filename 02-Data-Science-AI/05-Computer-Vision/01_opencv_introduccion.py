"""
================================================================================
COMPUTER VISION CON OPENCV
================================================================================

¿QUÉ ES COMPUTER VISION?
------------------------
Computer Vision (Visión por Computadora) es el campo que permite a las
computadoras "ver" y entender imágenes y videos.

APLICACIONES:
- Reconocimiento facial
- Detección de objetos
- Vehículos autónomos
- Diagnóstico médico por imágenes
- Control de calidad industrial
- Realidad aumentada

¿QUÉ ES OPENCV?
---------------
OpenCV (Open Source Computer Vision) es la librería más usada para
procesamiento de imágenes y video. Es rápida (escrita en C++) y tiene
bindings para Python.

INSTALACIÓN:
    pip install opencv-python
    pip install opencv-contrib-python  # Módulos extra

================================================================================
"""

print("=" * 60)
print("OPENCV: Fundamentos de Computer Vision")
print("=" * 60)

try:
    import cv2
    import numpy as np
    print(f"OpenCV versión: {cv2.__version__}")
    OPENCV_DISPONIBLE = True
except ImportError:
    print("OpenCV no instalado. Instálalo con: pip install opencv-python")
    OPENCV_DISPONIBLE = False


# ==============================================================================
# CONCEPTOS BÁSICOS DE IMÁGENES
# ==============================================================================

print("\n" + "=" * 60)
print("CONCEPTOS: ¿Qué es una imagen digital?")
print("=" * 60)

print("""
Una imagen digital es una matriz de píxeles.

IMAGEN EN ESCALA DE GRISES:
- Matriz 2D de valores 0-255
- 0 = negro, 255 = blanco
- Shape: (altura, ancho)

IMAGEN A COLOR (RGB/BGR):
- Matriz 3D con 3 canales
- OpenCV usa BGR (no RGB!)
- Shape: (altura, ancho, 3)

Ejemplo imagen 100x100 a color:
    shape = (100, 100, 3)
    100 filas × 100 columnas × 3 canales

Cada píxel es un array [B, G, R] con valores 0-255.
""")

if OPENCV_DISPONIBLE:
    # Crear imagen de ejemplo
    # Imagen negra de 200x300 píxeles
    imagen_negra = np.zeros((200, 300, 3), dtype=np.uint8)
    print(f"Imagen negra shape: {imagen_negra.shape}")
    print(f"Tipo de datos: {imagen_negra.dtype}")

    # Imagen con colores
    imagen_color = np.zeros((200, 300, 3), dtype=np.uint8)
    imagen_color[:, :100] = [255, 0, 0]     # Azul (BGR)
    imagen_color[:, 100:200] = [0, 255, 0]  # Verde
    imagen_color[:, 200:] = [0, 0, 255]     # Rojo
    print("Imagen con franjas de colores creada")


# ==============================================================================
# OPERACIONES BÁSICAS
# ==============================================================================

if OPENCV_DISPONIBLE:
    print("\n" + "=" * 60)
    print("OPERACIONES BÁSICAS")
    print("=" * 60)

    print("""
    LECTURA Y ESCRITURA:
    --------------------
    # Leer imagen
    img = cv2.imread('imagen.jpg')
    img_gris = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

    # Guardar imagen
    cv2.imwrite('salida.jpg', img)

    # Mostrar imagen (en scripts)
    cv2.imshow('Ventana', img)
    cv2.waitKey(0)  # Esperar tecla
    cv2.destroyAllWindows()

    INFORMACIÓN DE LA IMAGEN:
    -------------------------
    alto, ancho = img.shape[:2]
    canales = img.shape[2] if len(img.shape) == 3 else 1
    tipo = img.dtype
    """)

    # Crear imagen de ejemplo para demostrar operaciones
    img = np.zeros((300, 400, 3), dtype=np.uint8)
    img[:] = [50, 50, 50]  # Gris oscuro de fondo

    # DIBUJAR FORMAS
    print("\n--- Dibujar formas ---")

    # Línea
    cv2.line(img, (50, 50), (350, 50), (0, 255, 0), 2)
    print("Línea: cv2.line(img, (x1,y1), (x2,y2), color, grosor)")

    # Rectángulo
    cv2.rectangle(img, (50, 80), (150, 150), (255, 0, 0), 2)
    cv2.rectangle(img, (200, 80), (300, 150), (255, 0, 0), -1)  # Relleno
    print("Rectángulo: cv2.rectangle(img, esquina1, esquina2, color, grosor)")

    # Círculo
    cv2.circle(img, (100, 220), 50, (0, 0, 255), 2)
    cv2.circle(img, (250, 220), 50, (0, 0, 255), -1)
    print("Círculo: cv2.circle(img, centro, radio, color, grosor)")

    # Texto
    cv2.putText(img, 'OpenCV', (280, 280),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    print("Texto: cv2.putText(img, texto, posicion, fuente, escala, color, grosor)")

    # Guardar imagen de ejemplo
    cv2.imwrite('/tmp/opencv_formas.png', img)
    print("\nImagen guardada en /tmp/opencv_formas.png")


# ==============================================================================
# TRANSFORMACIONES DE IMAGEN
# ==============================================================================

if OPENCV_DISPONIBLE:
    print("\n" + "=" * 60)
    print("TRANSFORMACIONES DE IMAGEN")
    print("=" * 60)

    print("""
    REDIMENSIONAR:
    img_resize = cv2.resize(img, (nuevo_ancho, nuevo_alto))
    img_resize = cv2.resize(img, None, fx=0.5, fy=0.5)  # 50%

    ROTAR:
    # Obtener matriz de rotación
    centro = (ancho//2, alto//2)
    matriz = cv2.getRotationMatrix2D(centro, angulo, escala)
    img_rotada = cv2.warpAffine(img, matriz, (ancho, alto))

    VOLTEAR:
    img_h = cv2.flip(img, 1)   # Horizontal
    img_v = cv2.flip(img, 0)   # Vertical
    img_hv = cv2.flip(img, -1) # Ambos

    RECORTAR (usando numpy):
    recorte = img[y1:y2, x1:x2]

    CONVERTIR ESPACIO DE COLOR:
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    """)


# ==============================================================================
# FILTROS Y SUAVIZADO
# ==============================================================================

if OPENCV_DISPONIBLE:
    print("\n" + "=" * 60)
    print("FILTROS Y SUAVIZADO")
    print("=" * 60)

    print("""
    Los filtros modifican los píxeles basándose en sus vecinos.
    Se usan para:
    - Reducir ruido
    - Suavizar bordes
    - Detectar características

    FILTROS COMUNES:
    ----------------
    # Blur (suavizado)
    blur = cv2.blur(img, (5, 5))

    # Gaussian Blur (más natural)
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)

    # Median Blur (bueno para ruido sal y pimienta)
    median = cv2.medianBlur(img, 5)

    # Bilateral (preserva bordes)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    DETECCIÓN DE BORDES:
    -------------------
    # Canny (el más usado)
    bordes = cv2.Canny(img, 100, 200)

    # Sobel (detecta gradientes)
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

    # Laplaciano
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    """)


# ==============================================================================
# DETECCIÓN DE OBJETOS
# ==============================================================================

if OPENCV_DISPONIBLE:
    print("\n" + "=" * 60)
    print("DETECCIÓN DE OBJETOS")
    print("=" * 60)

    print("""
    DETECCIÓN DE ROSTROS (Haar Cascades):
    ------------------------------------
    # Cargar clasificador pre-entrenado
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Detectar rostros
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rostros = face_cascade.detectMultiScale(gris, 1.1, 4)

    # Dibujar rectángulos
    for (x, y, w, h) in rostros:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    DETECCIÓN DE CONTORNOS:
    ----------------------
    # Encontrar contornos
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos
    cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
    """)


# ==============================================================================
# EJEMPLO: DETECCIÓN DE COLORES
# ==============================================================================

if OPENCV_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO: Detección de colores")
    print("=" * 60)

    # Crear imagen de prueba con círculos de colores
    img_colores = np.zeros((300, 400, 3), dtype=np.uint8)
    img_colores[:] = [255, 255, 255]  # Fondo blanco

    # Círculos de diferentes colores
    cv2.circle(img_colores, (80, 150), 50, (255, 0, 0), -1)   # Azul
    cv2.circle(img_colores, (200, 150), 50, (0, 255, 0), -1)  # Verde
    cv2.circle(img_colores, (320, 150), 50, (0, 0, 255), -1)  # Rojo

    # Convertir a HSV para detectar colores
    hsv = cv2.cvtColor(img_colores, cv2.COLOR_BGR2HSV)

    # Definir rango para color azul en HSV
    azul_bajo = np.array([100, 50, 50])
    azul_alto = np.array([130, 255, 255])

    # Crear máscara
    mascara_azul = cv2.inRange(hsv, azul_bajo, azul_alto)

    # Aplicar máscara
    resultado = cv2.bitwise_and(img_colores, img_colores, mask=mascara_azul)

    cv2.imwrite('/tmp/opencv_colores_original.png', img_colores)
    cv2.imwrite('/tmp/opencv_colores_mascara.png', mascara_azul)
    cv2.imwrite('/tmp/opencv_colores_resultado.png', resultado)

    print("Imágenes guardadas:")
    print("  /tmp/opencv_colores_original.png")
    print("  /tmp/opencv_colores_mascara.png (solo azul)")
    print("  /tmp/opencv_colores_resultado.png")


# ==============================================================================
# VIDEO Y WEBCAM
# ==============================================================================

print("\n" + "=" * 60)
print("PROCESAMIENTO DE VIDEO")
print("=" * 60)

print("""
CAPTURA DE VIDEO:
----------------
# Desde archivo
cap = cv2.VideoCapture('video.mp4')

# Desde webcam (0 = cámara principal)
cap = cv2.VideoCapture(0)

# Leer frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Procesar frame
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video', gris)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

GUARDAR VIDEO:
-------------
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('salida.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    out.write(frame)

out.release()
""")


# ==============================================================================
# DEEP LEARNING CON OPENCV
# ==============================================================================

print("\n" + "=" * 60)
print("DEEP LEARNING CON OPENCV")
print("=" * 60)

print("""
OpenCV puede cargar y ejecutar modelos de deep learning:

CARGAR MODELO PRE-ENTRENADO:
---------------------------
# Cargar modelo YOLO para detección de objetos
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# Cargar modelo de clasificación
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'model.caffemodel')
net = cv2.dnn.readNetFromTensorflow('model.pb')
net = cv2.dnn.readNetFromONNX('model.onnx')

EJECUTAR INFERENCIA:
-------------------
# Preparar imagen
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True)
net.setInput(blob)

# Obtener predicciones
outputs = net.forward(output_layers)

Para modelos más avanzados, considera:
- TensorFlow / Keras
- PyTorch
- detectron2 (Facebook)
- YOLOv5/v8 (Ultralytics)
""")

print("\n" + "=" * 60)
print("PRÓXIMO: Explora detección de objetos con YOLO")
print("=" * 60)
