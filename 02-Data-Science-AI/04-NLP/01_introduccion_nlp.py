"""
================================================================================
PROCESAMIENTO DE LENGUAJE NATURAL (NLP)
================================================================================

¿QUÉ ES NLP?
------------
NLP (Natural Language Processing) es el campo que permite a las computadoras
entender, interpretar y generar lenguaje humano.

APLICACIONES:
- Chatbots y asistentes virtuales
- Traducción automática
- Análisis de sentimientos
- Resumen de textos
- Búsqueda semántica
- Generación de texto (GPT, Claude)

================================================================================
CONCEPTOS FUNDAMENTALES
================================================================================

1. TOKENIZACIÓN: Dividir texto en unidades (palabras, subpalabras)
2. STOPWORDS: Palabras comunes a filtrar (el, la, de, etc.)
3. STEMMING: Reducir palabras a su raíz (corriendo → corr)
4. LEMMATIZATION: Reducir a forma base (corriendo → correr)
5. EMBEDDINGS: Representar palabras como vectores numéricos
6. TRANSFORMERS: Arquitectura moderna (BERT, GPT)

INSTALACIÓN:
    pip install nltk spacy transformers

================================================================================
"""

import re
from collections import Counter

# ==============================================================================
# PREPROCESAMIENTO BÁSICO (sin librerías)
# ==============================================================================

print("=" * 60)
print("PREPROCESAMIENTO BÁSICO DE TEXTO")
print("=" * 60)

texto_ejemplo = """
¡Hola! Este es un EJEMPLO de procesamiento de texto.
Los textos pueden tener números como 123 y caracteres especiales @#$.
También múltiples    espacios   y
saltos de línea.
"""

print(f"Texto original:\n{texto_ejemplo}")


def limpiar_texto(texto):
    """
    Limpieza básica de texto.

    Pasos típicos:
    1. Convertir a minúsculas
    2. Eliminar caracteres especiales
    3. Eliminar números (opcional)
    4. Eliminar espacios extra
    """
    # Minúsculas
    texto = texto.lower()

    # Eliminar caracteres especiales (mantener letras, números, espacios)
    texto = re.sub(r'[^a-záéíóúñü0-9\s]', '', texto)

    # Eliminar números (opcional)
    # texto = re.sub(r'\d+', '', texto)

    # Eliminar espacios extra
    texto = ' '.join(texto.split())

    return texto


texto_limpio = limpiar_texto(texto_ejemplo)
print(f"\nTexto limpio:\n{texto_limpio}")


# ==============================================================================
# TOKENIZACIÓN SIMPLE
# ==============================================================================

print("\n" + "=" * 60)
print("TOKENIZACIÓN")
print("=" * 60)


def tokenizar(texto):
    """
    Tokenización simple: dividir por espacios.

    En la práctica, se usan tokenizadores más sofisticados
    que manejan casos especiales.
    """
    return texto.split()


tokens = tokenizar(texto_limpio)
print(f"Tokens: {tokens}")
print(f"Número de tokens: {len(tokens)}")


# ==============================================================================
# STOPWORDS
# ==============================================================================

print("\n" + "=" * 60)
print("ELIMINACIÓN DE STOPWORDS")
print("=" * 60)

# Stopwords en español (lista parcial)
STOPWORDS_ES = {
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
    'de', 'del', 'al', 'a', 'en', 'con', 'por', 'para',
    'es', 'son', 'este', 'esta', 'esto', 'estos', 'estas',
    'y', 'o', 'pero', 'que', 'como', 'se', 'su', 'sus'
}


def eliminar_stopwords(tokens, stopwords=STOPWORDS_ES):
    """Elimina stopwords de una lista de tokens."""
    return [t for t in tokens if t not in stopwords]


tokens_filtrados = eliminar_stopwords(tokens)
print(f"Tokens originales: {tokens}")
print(f"Sin stopwords: {tokens_filtrados}")


# ==============================================================================
# BAG OF WORDS
# ==============================================================================

print("\n" + "=" * 60)
print("BAG OF WORDS (Bolsa de Palabras)")
print("=" * 60)

print("""
Bag of Words es una representación simple de texto:
- Cuenta la frecuencia de cada palabra
- Ignora el orden de las palabras
- Cada documento es un vector de conteos
""")

documentos = [
    "el gato come pescado",
    "el perro come carne",
    "el gato y el perro juegan"
]


def crear_vocabulario(documentos):
    """Crea un vocabulario único de todos los documentos."""
    vocabulario = set()
    for doc in documentos:
        tokens = doc.lower().split()
        vocabulario.update(tokens)
    return sorted(list(vocabulario))


def bow(documento, vocabulario):
    """Convierte un documento en vector Bag of Words."""
    tokens = documento.lower().split()
    conteo = Counter(tokens)
    return [conteo.get(palabra, 0) for palabra in vocabulario]


vocabulario = crear_vocabulario(documentos)
print(f"Vocabulario: {vocabulario}")
print(f"\nVectores Bag of Words:")

for doc in documentos:
    vector = bow(doc, vocabulario)
    print(f"  '{doc}'")
    print(f"   → {vector}")


# ==============================================================================
# TF-IDF (Term Frequency - Inverse Document Frequency)
# ==============================================================================

print("\n" + "=" * 60)
print("TF-IDF")
print("=" * 60)

print("""
TF-IDF pondera las palabras por su importancia:

TF (Term Frequency):
    Frecuencia del término en el documento

IDF (Inverse Document Frequency):
    log(N / df) donde N = total documentos, df = docs que contienen el término

Palabras comunes en todos los documentos tienen IDF bajo.
Palabras raras pero presentes tienen IDF alto.

TF-IDF = TF × IDF
""")

import math


def calcular_tfidf(documentos):
    """Calcula TF-IDF para una colección de documentos."""
    # Tokenizar todos los documentos
    docs_tokens = [doc.lower().split() for doc in documentos]
    n_docs = len(documentos)

    # Calcular DF (document frequency)
    df = Counter()
    for tokens in docs_tokens:
        palabras_unicas = set(tokens)
        for palabra in palabras_unicas:
            df[palabra] += 1

    # Calcular IDF
    idf = {palabra: math.log(n_docs / freq) for palabra, freq in df.items()}

    # Calcular TF-IDF para cada documento
    tfidf_docs = []
    for tokens in docs_tokens:
        tf = Counter(tokens)
        total_tokens = len(tokens)
        tfidf = {palabra: (freq/total_tokens) * idf[palabra]
                 for palabra, freq in tf.items()}
        tfidf_docs.append(tfidf)

    return tfidf_docs, idf


tfidf_docs, idf = calcular_tfidf(documentos)

print("IDF de cada palabra:")
for palabra, valor in sorted(idf.items(), key=lambda x: x[1], reverse=True):
    print(f"  {palabra}: {valor:.3f}")

print("\nTF-IDF por documento:")
for i, (doc, tfidf) in enumerate(zip(documentos, tfidf_docs)):
    print(f"\n  Doc {i+1}: '{doc}'")
    for palabra, valor in sorted(tfidf.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"    {palabra}: {valor:.3f}")


# ==============================================================================
# NLTK (Natural Language Toolkit)
# ==============================================================================

print("\n" + "=" * 60)
print("NLTK: Natural Language Toolkit")
print("=" * 60)

try:
    import nltk

    # Descargar recursos necesarios (primera vez)
    # nltk.download('punkt')
    # nltk.download('stopwords')
    # nltk.download('wordnet')

    print("""
    NLTK proporciona herramientas completas para NLP:

    # Tokenización
    from nltk.tokenize import word_tokenize, sent_tokenize
    tokens = word_tokenize("Hola mundo.")
    oraciones = sent_tokenize("Primera oración. Segunda oración.")

    # Stopwords
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('spanish'))

    # Stemming
    from nltk.stem import SnowballStemmer
    stemmer = SnowballStemmer('spanish')
    stemmer.stem('corriendo')  # → 'corr'

    # Lematización
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatizer.lemmatize('running', pos='v')  # → 'run'
    """)
    NLTK_DISPONIBLE = True

except ImportError:
    print("NLTK no instalado. Instálalo con: pip install nltk")
    NLTK_DISPONIBLE = False


# ==============================================================================
# spaCy
# ==============================================================================

print("\n" + "=" * 60)
print("spaCy: NLP Industrial")
print("=" * 60)

print("""
spaCy es una librería de NLP optimizada para producción:

# Instalación
pip install spacy
python -m spacy download es_core_news_sm  # Modelo español

# Uso básico
import spacy
nlp = spacy.load('es_core_news_sm')
doc = nlp("El gato negro duerme en el sofá.")

# Tokenización y análisis
for token in doc:
    print(token.text, token.pos_, token.lemma_)

# Entidades nombradas (NER)
for ent in doc.ents:
    print(ent.text, ent.label_)

# Similitud semántica
doc1 = nlp("Me gusta el café")
doc2 = nlp("Prefiero el té")
print(doc1.similarity(doc2))
""")


# ==============================================================================
# TRANSFORMERS Y HUGGING FACE
# ==============================================================================

print("\n" + "=" * 60)
print("TRANSFORMERS: El estado del arte")
print("=" * 60)

print("""
Los Transformers revolucionaron el NLP (2017+).
Hugging Face es la plataforma más usada para acceder a modelos.

# Instalación
pip install transformers torch

# Análisis de sentimiento
from transformers import pipeline
clasificador = pipeline("sentiment-analysis")
resultado = clasificador("Me encanta este producto!")
# → [{'label': 'POSITIVE', 'score': 0.99}]

# Generación de texto
generador = pipeline("text-generation", model="gpt2")
texto = generador("El futuro de la IA es", max_length=50)

# Traducción
traductor = pipeline("translation_en_to_es")
traduccion = traductor("Hello, how are you?")

# Preguntas y respuestas
qa = pipeline("question-answering")
resultado = qa(
    question="¿Cuál es la capital de Francia?",
    context="Francia es un país europeo. Su capital es París."
)

# Modelos populares:
# - BERT: Bidireccional, bueno para clasificación
# - GPT: Generativo, bueno para crear texto
# - T5: Texto-a-texto, versátil
# - RoBERTa: BERT mejorado
# - DistilBERT: BERT más pequeño y rápido
""")


# ==============================================================================
# EJEMPLO COMPLETO: ANÁLISIS DE SENTIMIENTOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO: Análisis de Sentimientos Simple")
print("=" * 60)

# Diccionario simple de sentimientos (en producción usar modelos)
PALABRAS_POSITIVAS = {
    'bueno', 'excelente', 'genial', 'increíble', 'fantástico',
    'amor', 'feliz', 'alegre', 'mejor', 'maravilloso', 'encanta',
    'recomiendo', 'perfecto', 'útil', 'fácil'
}

PALABRAS_NEGATIVAS = {
    'malo', 'terrible', 'horrible', 'pésimo', 'peor',
    'odio', 'triste', 'difícil', 'problema', 'error',
    'lento', 'caro', 'feo', 'aburrido', 'inútil'
}


def analizar_sentimiento(texto):
    """
    Análisis de sentimiento basado en diccionario.

    En producción, usar modelos de ML o Transformers.
    """
    texto = texto.lower()
    tokens = set(texto.split())

    positivas = len(tokens & PALABRAS_POSITIVAS)
    negativas = len(tokens & PALABRAS_NEGATIVAS)

    if positivas > negativas:
        return 'POSITIVO', positivas - negativas
    elif negativas > positivas:
        return 'NEGATIVO', negativas - positivas
    else:
        return 'NEUTRAL', 0


# Probar con reseñas
reseñas = [
    "Este producto es excelente, lo recomiendo totalmente",
    "Terrible experiencia, muy malo el servicio",
    "El producto llegó en buen estado",
    "No me gustó, muy caro para lo que ofrece"
]

print("Análisis de reseñas:")
for reseña in reseñas:
    sentimiento, score = analizar_sentimiento(reseña)
    print(f"  [{sentimiento:>8}] (score: {score}) '{reseña[:40]}...'")


print("\n" + "=" * 60)
print("PRÓXIMO: Explora spaCy y Transformers en profundidad")
print("=" * 60)
