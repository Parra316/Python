"""
================================================================================
INTRODUCCIÓN A PYTORCH
================================================================================

PREREQUISITOS:
- 01_estructuras_de_datos_arbol.py
- 02_que_es_una_neurona.py
- 03_red_neuronal_desde_cero.py

INSTALACIÓN:
    pip install torch torchvision

================================================================================
¿QUÉ ES PYTORCH?
================================================================================

PyTorch es un framework de deep learning desarrollado por Meta (Facebook) que:

1. Usa grafos dinámicos (define-by-run) vs. estáticos de TensorFlow
2. Es más "pythónico" e intuitivo
3. Preferido en investigación y academia
4. Tiene excelente soporte para debugging

================================================================================
TENSORFLOW vs PYTORCH
================================================================================

TensorFlow (Keras):
- API de alto nivel más simple para principiantes
- Mejor para producción y deployment
- TensorFlow Serving, TensorFlow Lite

PyTorch:
- Más flexibilidad y control
- Debugging más fácil (código Python estándar)
- Preferido en papers de investigación
- TorchServe para producción

Ambos son excelentes. La elección depende del caso de uso.

================================================================================
"""

# ==============================================================================
# IMPORTACIONES Y CONFIGURACIÓN
# ==============================================================================

print("=" * 60)
print("PYTORCH: Configuración inicial")
print("=" * 60)

try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
    import numpy as np

    print(f"PyTorch versión: {torch.__version__}")
    print(f"CUDA disponible: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    TORCH_DISPONIBLE = True

except ImportError:
    print("PyTorch no está instalado.")
    print("Instálalo con: pip install torch torchvision")
    print("\nEste archivo muestra el código que usarías con PyTorch.")
    TORCH_DISPONIBLE = False


# ==============================================================================
# TENSORES EN PYTORCH
# ==============================================================================

if TORCH_DISPONIBLE:
    print("\n" + "=" * 60)
    print("TENSORES: La base de PyTorch")
    print("=" * 60)

    print("""
    Los tensores de PyTorch son similares a los de TensorFlow,
    pero con una sintaxis más parecida a NumPy.
    """)

    # Crear tensores
    tensor_lista = torch.tensor([1, 2, 3, 4])
    tensor_zeros = torch.zeros(3, 4)
    tensor_random = torch.randn(2, 3)  # Normal estándar
    tensor_numpy = torch.from_numpy(np.array([1, 2, 3]))

    print(f"Desde lista: {tensor_lista}")
    print(f"Zeros (3x4):\n{tensor_zeros}")
    print(f"Random (2x3):\n{tensor_random}")
    print(f"Desde numpy: {tensor_numpy}")

    # Operaciones
    print("\nOperaciones con tensores:")
    a = torch.tensor([1.0, 2.0, 3.0])
    b = torch.tensor([4.0, 5.0, 6.0])
    print(f"a + b = {a + b}")
    print(f"a * b = {a * b}")
    print(f"a @ b (producto punto) = {torch.dot(a, b)}")


# ==============================================================================
# AUTOGRAD: Diferenciación automática
# ==============================================================================

if TORCH_DISPONIBLE:
    print("\n" + "=" * 60)
    print("AUTOGRAD: Cálculo automático de gradientes")
    print("=" * 60)

    print("""
    PyTorch rastrea las operaciones para calcular gradientes automáticamente.
    Esto es el corazón del backpropagation.
    """)

    # Ejemplo: y = x² + 2x + 1
    # dy/dx = 2x + 2
    x = torch.tensor(3.0, requires_grad=True)  # Rastrear gradientes
    y = x**2 + 2*x + 1

    print(f"x = {x}")
    print(f"y = x² + 2x + 1 = {y}")

    # Calcular gradiente
    y.backward()  # dy/dx
    print(f"dy/dx en x=3: {x.grad}")  # Debería ser 2(3) + 2 = 8

    # Ejemplo con múltiples variables
    print("\nEjemplo con múltiples variables:")
    w = torch.tensor([1.0, 2.0], requires_grad=True)
    x_input = torch.tensor([3.0, 4.0])
    y_output = torch.sum(w * x_input)  # 1*3 + 2*4 = 11

    y_output.backward()
    print(f"w = {w.data}")
    print(f"x = {x_input}")
    print(f"y = w·x = {y_output}")
    print(f"∂y/∂w = {w.grad}")  # Debería ser [3, 4]


# ==============================================================================
# EJEMPLO 1: XOR con PyTorch
# ==============================================================================

if TORCH_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO 1: Resolver XOR con PyTorch")
    print("=" * 60)

    # Datos
    X_xor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
    y_xor = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

    # Definir modelo como clase (forma típica en PyTorch)
    class RedXOR(nn.Module):
        """
        Red neuronal para resolver XOR.

        En PyTorch, los modelos heredan de nn.Module.
        Definimos las capas en __init__ y el flujo en forward.
        """

        def __init__(self):
            super(RedXOR, self).__init__()
            # Definir capas
            self.capa_oculta = nn.Linear(2, 4)  # 2 entradas, 4 neuronas
            self.capa_salida = nn.Linear(4, 1)  # 4 entradas, 1 salida
            self.relu = nn.ReLU()
            self.sigmoid = nn.Sigmoid()

        def forward(self, x):
            """Define cómo fluyen los datos a través de la red."""
            x = self.capa_oculta(x)
            x = self.relu(x)
            x = self.capa_salida(x)
            x = self.sigmoid(x)
            return x

    # Crear modelo
    modelo_xor = RedXOR()
    print(f"Modelo:\n{modelo_xor}")

    # Definir pérdida y optimizador
    criterio = nn.BCELoss()  # Binary Cross Entropy
    optimizador = optim.Adam(modelo_xor.parameters(), lr=0.1)

    # Entrenar
    print("\nEntrenando...")
    for epoca in range(1000):
        # Forward
        predicciones = modelo_xor(X_xor)
        perdida = criterio(predicciones, y_xor)

        # Backward
        optimizador.zero_grad()  # Limpiar gradientes anteriores
        perdida.backward()       # Calcular nuevos gradientes
        optimizador.step()       # Actualizar pesos

        if (epoca + 1) % 200 == 0:
            print(f"  Época {epoca + 1}: Pérdida = {perdida.item():.4f}")

    # Evaluar
    print("\nPredicciones después de entrenar:")
    with torch.no_grad():  # No calcular gradientes
        predicciones = modelo_xor(X_xor)
        for i in range(4):
            entrada = X_xor[i].tolist()
            pred = predicciones[i].item()
            real = y_xor[i].item()
            print(f"  {int(entrada[0])} XOR {int(entrada[1])} = {pred:.4f} → {round(pred)} (real: {int(real)})")


# ==============================================================================
# EJEMPLO 2: Clasificación MNIST
# ==============================================================================

if TORCH_DISPONIBLE:
    print("\n" + "=" * 60)
    print("EJEMPLO 2: MNIST con PyTorch")
    print("=" * 60)

    try:
        from torchvision import datasets, transforms
        from torch.utils.data import DataLoader

        # Transformaciones
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))  # Media y std de MNIST
        ])

        # Cargar datos
        train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
        test_dataset = datasets.MNIST('./data', train=False, transform=transform)

        # DataLoaders (cargan datos en batches)
        train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=1000)

        print(f"Datos de entrenamiento: {len(train_dataset)}")
        print(f"Datos de prueba: {len(test_dataset)}")

        # Modelo
        class RedMNIST(nn.Module):
            def __init__(self):
                super(RedMNIST, self).__init__()
                self.flatten = nn.Flatten()
                self.capas = nn.Sequential(
                    nn.Linear(784, 128),
                    nn.ReLU(),
                    nn.Dropout(0.2),
                    nn.Linear(128, 64),
                    nn.ReLU(),
                    nn.Dropout(0.2),
                    nn.Linear(64, 10)
                )

            def forward(self, x):
                x = self.flatten(x)
                x = self.capas(x)
                return x

        modelo_mnist = RedMNIST()
        criterio = nn.CrossEntropyLoss()
        optimizador = optim.Adam(modelo_mnist.parameters(), lr=0.001)

        # Función de entrenamiento
        def entrenar_epoca(modelo, loader, criterio, optimizador):
            modelo.train()
            total_perdida = 0
            for batch_x, batch_y in loader:
                optimizador.zero_grad()
                salida = modelo(batch_x)
                perdida = criterio(salida, batch_y)
                perdida.backward()
                optimizador.step()
                total_perdida += perdida.item()
            return total_perdida / len(loader)

        # Función de evaluación
        def evaluar(modelo, loader):
            modelo.eval()
            correctos = 0
            total = 0
            with torch.no_grad():
                for batch_x, batch_y in loader:
                    salida = modelo(batch_x)
                    _, predicciones = torch.max(salida, 1)
                    total += batch_y.size(0)
                    correctos += (predicciones == batch_y).sum().item()
            return correctos / total

        # Entrenar
        print("\nEntrenando (3 épocas)...")
        for epoca in range(3):
            perdida = entrenar_epoca(modelo_mnist, train_loader, criterio, optimizador)
            precision = evaluar(modelo_mnist, test_loader)
            print(f"  Época {epoca + 1}: Pérdida = {perdida:.4f}, Precisión = {precision * 100:.2f}%")

    except Exception as e:
        print(f"Error al cargar MNIST: {e}")
        print("Asegúrate de tener torchvision instalado: pip install torchvision")


# ==============================================================================
# DIFERENCIAS CLAVE: TENSORFLOW vs PYTORCH
# ==============================================================================

print("\n" + "=" * 60)
print("COMPARACIÓN: TensorFlow vs PyTorch")
print("=" * 60)

print("""
┌─────────────────┬─────────────────────┬─────────────────────┐
│ Aspecto         │ TensorFlow/Keras    │ PyTorch             │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Definir modelo  │ Sequential o        │ Clase heredando     │
│                 │ Functional API      │ nn.Module           │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Entrenamiento   │ model.fit()         │ Loop manual         │
│                 │ (automático)        │ (más control)       │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Gradientes      │ Automático en fit() │ loss.backward()     │
│                 │                     │ optimizer.step()    │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Evaluación      │ model.evaluate()    │ torch.no_grad()     │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Debugging       │ Más difícil         │ Más fácil           │
│                 │ (grafo estático)    │ (Python estándar)   │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Producción      │ TF Serving, TF Lite │ TorchServe, ONNX    │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Ecosistema      │ TensorBoard,        │ Hugging Face,       │
│                 │ TF Hub              │ PyTorch Lightning   │
└─────────────────┴─────────────────────┴─────────────────────┘

¿Cuál elegir?
- Principiantes: TensorFlow/Keras (más sencillo)
- Investigación: PyTorch (más flexible)
- Producción: TensorFlow (mejor soporte)
- Aprender ambos: Te hace más versátil
""")


# ==============================================================================
# PLANTILLA PYTORCH COMPLETA
# ==============================================================================

print("\n" + "=" * 60)
print("PLANTILLA: Modelo PyTorch completo")
print("=" * 60)

print("""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 1. PREPARAR DATOS
X_train = torch.tensor(datos_x, dtype=torch.float32)
y_train = torch.tensor(datos_y, dtype=torch.long)

dataset = TensorDataset(X_train, y_train)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# 2. DEFINIR MODELO
class MiModelo(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(MiModelo, self).__init__()
        self.red = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        return self.red(x)

modelo = MiModelo(input_dim=10, hidden_dim=64, output_dim=3)

# 3. PÉRDIDA Y OPTIMIZADOR
criterio = nn.CrossEntropyLoss()
optimizador = optim.Adam(modelo.parameters(), lr=0.001)

# 4. ENTRENAR
for epoca in range(num_epocas):
    modelo.train()
    for batch_x, batch_y in dataloader:
        optimizador.zero_grad()
        salida = modelo(batch_x)
        perdida = criterio(salida, batch_y)
        perdida.backward()
        optimizador.step()

# 5. EVALUAR
modelo.eval()
with torch.no_grad():
    predicciones = modelo(X_test)

# 6. GUARDAR
torch.save(modelo.state_dict(), 'modelo.pth')

# 7. CARGAR
modelo_nuevo = MiModelo(input_dim=10, hidden_dim=64, output_dim=3)
modelo_nuevo.load_state_dict(torch.load('modelo.pth'))
""")

print("\n" + "=" * 60)
print("¡Has completado la sección de Deep Learning!")
print("PRÓXIMO: Explora Machine Learning, NLP, o Computer Vision")
print("=" * 60)
