"""
================================================================================
SCIKIT-LEARN: LA LIBRERÍA ESTÁNDAR DE MACHINE LEARNING
================================================================================

¿QUÉ ES SCIKIT-LEARN?
---------------------
Scikit-learn es la librería más usada para Machine Learning tradicional.
Proporciona:

1. Algoritmos de ML implementados y optimizados
2. Herramientas de preprocesamiento
3. Métricas de evaluación
4. Utilidades para validación cruzada
5. API consistente y fácil de usar

INSTALACIÓN:
    pip install scikit-learn

================================================================================
API CONSISTENTE DE SCIKIT-LEARN
================================================================================

Todos los modelos siguen el mismo patrón:

    modelo = Algoritmo()           # Crear
    modelo.fit(X_train, y_train)   # Entrenar
    predicciones = modelo.predict(X_test)  # Predecir

================================================================================
"""

print("=" * 60)
print("SCIKIT-LEARN: Ejemplos prácticos")
print("=" * 60)

try:
    import numpy as np
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    from sklearn.metrics import mean_squared_error, r2_score
    from sklearn.datasets import load_iris, load_diabetes, make_classification

    SKLEARN_DISPONIBLE = True
    print("Scikit-learn importado correctamente")

except ImportError:
    print("Scikit-learn no instalado. Instálalo con: pip install scikit-learn")
    print("Este archivo muestra el código que usarías.")
    SKLEARN_DISPONIBLE = False


# ==============================================================================
# EJEMPLO 1: CLASIFICACIÓN CON IRIS
# ==============================================================================

if SKLEARN_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO 1: Clasificación - Dataset Iris")
    print("=" * 60)

    print("""
    El dataset Iris es el "Hello World" del ML:
    - 150 flores de 3 especies (setosa, versicolor, virginica)
    - 4 características: largo/ancho de sépalo y pétalo
    - Tarea: predecir la especie
    """)

    # Cargar datos
    iris = load_iris()
    X = iris.data
    y = iris.target
    nombres_clases = iris.target_names
    nombres_features = iris.feature_names

    print(f"Shape de X: {X.shape}")
    print(f"Features: {nombres_features}")
    print(f"Clases: {list(nombres_clases)}")

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Probar varios modelos
    modelos = {
        'Regresión Logística': LogisticRegression(max_iter=200),
        'Árbol de Decisión': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
    }

    print("\nComparación de modelos:")
    print("-" * 50)

    for nombre, modelo in modelos.items():
        # Entrenar
        modelo.fit(X_train, y_train)

        # Predecir
        y_pred = modelo.predict(X_test)

        # Evaluar
        accuracy = accuracy_score(y_test, y_pred)
        print(f"{nombre}: Accuracy = {accuracy:.4f}")

    # Detalles del mejor modelo (Random Forest)
    print("\n--- Detalles de Random Forest ---")
    mejor_modelo = modelos['Random Forest']
    y_pred = mejor_modelo.predict(X_test)

    print("\nReporte de clasificación:")
    print(classification_report(y_test, y_pred, target_names=nombres_clases))

    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))


# ==============================================================================
# EJEMPLO 2: REGRESIÓN CON DIABETES
# ==============================================================================

if SKLEARN_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO 2: Regresión - Dataset Diabetes")
    print("=" * 60)

    print("""
    Dataset de diabetes:
    - 442 pacientes
    - 10 variables fisiológicas
    - Target: medida de progresión de la enfermedad
    """)

    # Cargar datos
    diabetes = load_diabetes()
    X = diabetes.data
    y = diabetes.target

    print(f"Shape: {X.shape}")

    # Dividir
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Escalar features (importante para regresión)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Entrenar modelo
    modelo_reg = LinearRegression()
    modelo_reg.fit(X_train_scaled, y_train)

    # Predecir
    y_pred = modelo_reg.predict(X_test_scaled)

    # Evaluar
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"\nMétricas de regresión:")
    print(f"  MSE:  {mse:.2f}")
    print(f"  RMSE: {rmse:.2f}")
    print(f"  R²:   {r2:.4f}")

    # Coeficientes
    print(f"\nCoeficientes del modelo:")
    for nombre, coef in zip(diabetes.feature_names, modelo_reg.coef_):
        print(f"  {nombre}: {coef:.2f}")


# ==============================================================================
# PREPROCESAMIENTO DE DATOS
# ==============================================================================

if SKLEARN_DISPONIBLE:
    print("\n" + "=" * 60)
    print("PREPROCESAMIENTO DE DATOS")
    print("=" * 60)

    print("""
    Scikit-learn ofrece muchas herramientas de preprocesamiento:

    1. Escalado:
       - StandardScaler: media=0, std=1
       - MinMaxScaler: rango [0, 1]
       - RobustScaler: resistente a outliers

    2. Encoding de categorías:
       - LabelEncoder: convierte etiquetas a números
       - OneHotEncoder: crea columnas binarias

    3. Imputación de valores faltantes:
       - SimpleImputer: reemplaza con media/mediana/moda

    4. Transformaciones:
       - PolynomialFeatures: crea términos polinómicos
       - PCA: reducción de dimensionalidad
    """)

    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from sklearn.impute import SimpleImputer

    # Ejemplo: StandardScaler
    datos = np.array([[100, 0.5], [200, 0.8], [150, 0.6]])
    print(f"Datos originales:\n{datos}")

    scaler = StandardScaler()
    datos_scaled = scaler.fit_transform(datos)
    print(f"\nDatos escalados (StandardScaler):\n{datos_scaled.round(2)}")

    # Ejemplo: MinMaxScaler
    scaler_mm = MinMaxScaler()
    datos_minmax = scaler_mm.fit_transform(datos)
    print(f"\nDatos escalados (MinMaxScaler):\n{datos_minmax.round(2)}")


# ==============================================================================
# VALIDACIÓN CRUZADA
# ==============================================================================

if SKLEARN_DISPONIBLE:
    print("\n" + "=" * 60)
    print("VALIDACIÓN CRUZADA (Cross-Validation)")
    print("=" * 60)

    print("""
    La validación cruzada es una técnica más robusta para evaluar modelos.

    K-Fold Cross-Validation:
    1. Divide los datos en K partes (folds)
    2. Entrena K veces, cada vez usando un fold diferente como prueba
    3. Promedia las K métricas obtenidas

    Ventajas:
    - Usa todos los datos tanto para entrenar como para evaluar
    - Da una estimación más confiable del rendimiento
    - Detecta mejor el overfitting
    """)

    # Usar iris nuevamente
    iris = load_iris()
    X, y = iris.data, iris.target

    # Validación cruzada con 5 folds
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    scores = cross_val_score(modelo, X, y, cv=5, scoring='accuracy')

    print(f"Scores por fold: {scores.round(4)}")
    print(f"Accuracy promedio: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")


# ==============================================================================
# PIPELINE: ENCADENAR PASOS
# ==============================================================================

if SKLEARN_DISPONIBLE:
    print("\n" + "=" * 60)
    print("PIPELINES: Encadenar preprocesamiento y modelo")
    print("=" * 60)

    from sklearn.pipeline import Pipeline

    print("""
    Un Pipeline encadena múltiples pasos de preprocesamiento y un modelo.
    Garantiza que las transformaciones se apliquen consistentemente.
    """)

    # Crear pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(max_iter=200))
    ])

    # El pipeline se usa como un modelo normal
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    pipeline.fit(X_train, y_train)
    accuracy = pipeline.score(X_test, y_test)

    print(f"Pipeline [Scaler + LogisticRegression]")
    print(f"Accuracy: {accuracy:.4f}")

    # Cross-validation con pipeline
    scores = cross_val_score(pipeline, iris.data, iris.target, cv=5)
    print(f"CV Accuracy: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")


# ==============================================================================
# BÚSQUEDA DE HIPERPARÁMETROS
# ==============================================================================

if SKLEARN_DISPONIBLE:
    print("\n" + "=" * 60)
    print("BÚSQUEDA DE HIPERPARÁMETROS (GridSearchCV)")
    print("=" * 60)

    from sklearn.model_selection import GridSearchCV

    print("""
    Los hiperparámetros son configuraciones del modelo que no se aprenden.
    GridSearchCV prueba todas las combinaciones para encontrar la mejor.
    """)

    # Definir modelo y parámetros a probar
    modelo = RandomForestClassifier(random_state=42)
    parametros = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 10, None],
        'min_samples_split': [2, 5, 10]
    }

    # Búsqueda
    print("Buscando mejores hiperparámetros (puede tardar)...")
    grid_search = GridSearchCV(
        modelo,
        parametros,
        cv=3,
        scoring='accuracy',
        n_jobs=-1  # Usar todos los CPUs
    )
    grid_search.fit(iris.data, iris.target)

    print(f"\nMejores parámetros: {grid_search.best_params_}")
    print(f"Mejor accuracy: {grid_search.best_score_:.4f}")


# ==============================================================================
# RESUMEN DE ALGORITMOS
# ==============================================================================

print("\n" + "=" * 60)
print("RESUMEN: Algoritmos principales de Scikit-learn")
print("=" * 60)

print("""
CLASIFICACIÓN:
-------------
LogisticRegression      - Lineal, rápido, interpretable
DecisionTreeClassifier  - Fácil de interpretar
RandomForestClassifier  - Robusto, buen rendimiento general
GradientBoostingClassifier - Muy preciso
SVC (SVM)               - Bueno para datos no lineales
KNeighborsClassifier    - Simple, basado en distancia

REGRESIÓN:
----------
LinearRegression        - Lineal básico
Ridge, Lasso, ElasticNet - Regresión con regularización
DecisionTreeRegressor   - No lineal, interpretable
RandomForestRegressor   - Robusto, buen rendimiento
GradientBoostingRegressor - Muy preciso

CLUSTERING (No supervisado):
---------------------------
KMeans                  - El más común
DBSCAN                  - Detecta outliers
AgglomerativeClustering - Jerárquico

REDUCCIÓN DIMENSIONAL:
---------------------
PCA                     - El más usado
t-SNE                   - Para visualización
UMAP                    - Alternativa moderna a t-SNE
""")

print("\n" + "=" * 60)
print("PRÓXIMO: 03_modelos_avanzados.py (XGBoost, etc.)")
print("=" * 60)
