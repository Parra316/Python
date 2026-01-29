"""
================================================================================
PROGRAMACIÓN ORIENTADA A OBJETOS (POO) - AVANZADO
================================================================================

Conceptos avanzados de POO:
- Herencia
- Polimorfismo
- Clases abstractas
- Herencia múltiple
- Composición vs Herencia
- Mixins
- Dataclasses

================================================================================
"""

# ==============================================================================
# HERENCIA BÁSICA
# ==============================================================================

print("=" * 60)
print("HERENCIA BÁSICA")
print("=" * 60)

print("""
La herencia permite crear nuevas clases basadas en clases existentes.
La clase hija hereda atributos y métodos de la clase padre.
""")

# Clase padre (base)
class Animal:
    """Clase base para todos los animales."""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años"

    def hacer_sonido(self):
        return "..."

    def comer(self):
        return f"{self.nombre} está comiendo"


# Clases hijas (derivadas)
class Perro(Animal):
    """Perro hereda de Animal."""

    def __init__(self, nombre, edad, raza):
        # Llamar al constructor del padre
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau guau!"

    def traer_pelota(self):
        return f"{self.nombre} trae la pelota"


class Gato(Animal):
    """Gato hereda de Animal."""

    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "¡Miau!"

    def ronronear(self):
        return f"{self.nombre} está ronroneando"


# Usar las clases
perro = Perro("Max", 3, "Labrador")
gato = Gato("Michi", 2, "naranja")

print(f"Perro: {perro.presentarse()}")  # Método heredado
print(f"  Raza: {perro.raza}")
print(f"  Sonido: {perro.hacer_sonido()}")  # Método sobrescrito
print(f"  {perro.traer_pelota()}")  # Método propio

print(f"\nGato: {gato.presentarse()}")
print(f"  Color: {gato.color}")
print(f"  Sonido: {gato.hacer_sonido()}")
print(f"  {gato.ronronear()}")

# Verificar herencia
print(f"\n¿Perro es Animal?: {isinstance(perro, Animal)}")
print(f"¿Gato es Animal?: {isinstance(gato, Animal)}")
print(f"¿Perro es subclase de Animal?: {issubclass(Perro, Animal)}")


# ==============================================================================
# POLIMORFISMO
# ==============================================================================

print("\n" + "=" * 60)
print("POLIMORFISMO")
print("=" * 60)

print("""
El polimorfismo permite tratar objetos de diferentes clases
de manera uniforme si comparten una interfaz común.
""")

class Vehiculo:
    """Clase base para vehículos."""

    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        raise NotImplementedError("Subclase debe implementar mover()")

    def descripcion(self):
        return f"Vehículo {self.marca}"


class Coche(Vehiculo):
    def mover(self):
        return f"{self.marca} conduciendo por la carretera"


class Barco(Vehiculo):
    def mover(self):
        return f"{self.marca} navegando por el agua"


class Avion(Vehiculo):
    def mover(self):
        return f"{self.marca} volando por el cielo"


# Función polimórfica
def hacer_viaje(vehiculo):
    """Funciona con cualquier vehículo."""
    print(f"  {vehiculo.descripcion()}: {vehiculo.mover()}")


vehiculos = [
    Coche("Toyota"),
    Barco("Yamaha"),
    Avion("Boeing"),
    Coche("Honda")
]

print("Viaje con diferentes vehículos:")
for v in vehiculos:
    hacer_viaje(v)


# ==============================================================================
# CLASES ABSTRACTAS
# ==============================================================================

print("\n" + "=" * 60)
print("CLASES ABSTRACTAS")
print("=" * 60)

print("""
Las clases abstractas definen una interfaz que las subclases deben implementar.
No se pueden instanciar directamente.
""")

from abc import ABC, abstractmethod

class Figura(ABC):
    """Clase abstracta para figuras geométricas."""

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def area(self):
        """Debe ser implementado por subclases."""
        pass

    @abstractmethod
    def perimetro(self):
        """Debe ser implementado por subclases."""
        pass

    def descripcion(self):
        """Método concreto (no abstracto)."""
        return f"{self.nombre}: área={self.area():.2f}, perímetro={self.perimetro():.2f}"


class Rectangulo(Figura):
    """Rectángulo concreto."""

    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


class Circulo(Figura):
    """Círculo concreto."""

    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio ** 2

    def perimetro(self):
        import math
        return 2 * math.pi * self.radio


class Triangulo(Figura):
    """Triángulo concreto."""

    def __init__(self, a, b, c):
        super().__init__("Triángulo")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Fórmula de Herón
        s = self.perimetro() / 2
        import math
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimetro(self):
        return self.a + self.b + self.c


# No se puede instanciar Figura directamente
# figura = Figura("test")  # Error: TypeError

figuras = [
    Rectangulo(4, 5),
    Circulo(3),
    Triangulo(3, 4, 5)
]

print("Figuras:")
for fig in figuras:
    print(f"  {fig.descripcion()}")


# ==============================================================================
# HERENCIA MÚLTIPLE
# ==============================================================================

print("\n" + "=" * 60)
print("HERENCIA MÚLTIPLE")
print("=" * 60)

print("""
Python permite heredar de múltiples clases.
El orden de resolución de métodos (MRO) determina qué método se usa.
""")

class Volador:
    """Capacidad de volar."""

    def volar(self):
        return "Volando por el cielo"

    def despegar(self):
        return "Despegando..."


class Nadador:
    """Capacidad de nadar."""

    def nadar(self):
        return "Nadando en el agua"

    def bucear(self):
        return "Buceando..."


class Corredor:
    """Capacidad de correr."""

    def correr(self):
        return "Corriendo por tierra"


class Pato(Animal, Volador, Nadador, Corredor):
    """El pato puede hacer de todo."""

    def __init__(self, nombre):
        Animal.__init__(self, nombre, 2)

    def hacer_sonido(self):
        return "¡Cuac cuac!"


pato = Pato("Donald")
print(f"Pato: {pato.presentarse()}")
print(f"  Sonido: {pato.hacer_sonido()}")
print(f"  {pato.volar()}")
print(f"  {pato.nadar()}")
print(f"  {pato.correr()}")

# Ver el MRO (Method Resolution Order)
print(f"\nMRO de Pato:")
for cls in Pato.__mro__:
    print(f"  {cls.__name__}")


# ==============================================================================
# MIXINS
# ==============================================================================

print("\n" + "=" * 60)
print("MIXINS")
print("=" * 60)

print("""
Los Mixins son clases diseñadas para agregar funcionalidad
a otras clases mediante herencia múltiple.
No están pensadas para usarse solas.
""")

class SerializableMixin:
    """Mixin que añade capacidad de serialización."""

    def to_dict(self):
        """Convierte el objeto a diccionario."""
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith('_')}

    def to_json(self):
        """Convierte el objeto a JSON."""
        import json
        return json.dumps(self.to_dict(), indent=2)


class ComparableMixin:
    """Mixin que añade comparaciones basadas en un atributo."""

    def _get_comparison_key(self):
        """Subclase debe implementar esto."""
        raise NotImplementedError

    def __lt__(self, other):
        return self._get_comparison_key() < other._get_comparison_key()

    def __le__(self, other):
        return self._get_comparison_key() <= other._get_comparison_key()

    def __gt__(self, other):
        return self._get_comparison_key() > other._get_comparison_key()

    def __ge__(self, other):
        return self._get_comparison_key() >= other._get_comparison_key()


class LoggableMixin:
    """Mixin que añade logging."""

    def log(self, mensaje):
        print(f"[{self.__class__.__name__}] {mensaje}")


# Usar mixins
class Producto(SerializableMixin, ComparableMixin, LoggableMixin):
    """Producto con capacidades de serialización y comparación."""

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def _get_comparison_key(self):
        return self.precio

    def __repr__(self):
        return f"Producto('{self.nombre}', {self.precio})"


p1 = Producto("Laptop", 1000)
p2 = Producto("Mouse", 30)
p3 = Producto("Teclado", 80)

print(f"Producto: {p1}")
print(f"Como dict: {p1.to_dict()}")
print(f"Como JSON:\n{p1.to_json()}")

productos = [p1, p2, p3]
print(f"\nProductos ordenados por precio:")
for p in sorted(productos):
    print(f"  {p}")

p1.log("Producto creado")


# ==============================================================================
# COMPOSICIÓN VS HERENCIA
# ==============================================================================

print("\n" + "=" * 60)
print("COMPOSICIÓN VS HERENCIA")
print("=" * 60)

print("""
HERENCIA: "es un" (is-a)
  - Perro ES UN Animal
  - Usa cuando hay relación de tipo

COMPOSICIÓN: "tiene un" (has-a)
  - Coche TIENE UN Motor
  - Más flexible, preferir cuando sea posible
""")

# Ejemplo de composición
class Motor:
    """Motor de un vehículo."""

    def __init__(self, cilindrada, tipo="gasolina"):
        self.cilindrada = cilindrada
        self.tipo = tipo
        self.encendido = False

    def arrancar(self):
        self.encendido = True
        return f"Motor {self.tipo} {self.cilindrada}cc arrancado"

    def apagar(self):
        self.encendido = False
        return "Motor apagado"


class Ruedas:
    """Ruedas de un vehículo."""

    def __init__(self, cantidad, tamaño):
        self.cantidad = cantidad
        self.tamaño = tamaño

    def girar(self, direccion):
        return f"Girando {self.cantidad} ruedas hacia {direccion}"


class SistemaAudio:
    """Sistema de audio."""

    def __init__(self, potencia):
        self.potencia = potencia

    def reproducir(self, cancion):
        return f"Reproduciendo '{cancion}' a {self.potencia}W"


# Coche usa COMPOSICIÓN (tiene partes)
class Coche:
    """Coche compuesto de diferentes partes."""

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Composición: el coche TIENE estas partes
        self.motor = Motor(2000, "gasolina")
        self.ruedas = Ruedas(4, "R17")
        self.audio = SistemaAudio(200)

    def arrancar(self):
        return self.motor.arrancar()

    def conducir(self, direccion):
        if not self.motor.encendido:
            return "Primero arranca el coche"
        return self.ruedas.girar(direccion)

    def poner_musica(self, cancion):
        return self.audio.reproducir(cancion)


coche = Coche("Toyota", "Corolla")
print(f"Coche: {coche.marca} {coche.modelo}")
print(f"  {coche.arrancar()}")
print(f"  {coche.conducir('derecha')}")
print(f"  {coche.poner_musica('Highway to Hell')}")


# ==============================================================================
# DATACLASSES (Python 3.7+)
# ==============================================================================

print("\n" + "=" * 60)
print("DATACLASSES")
print("=" * 60)

print("""
Las dataclasses generan automáticamente __init__, __repr__, __eq__, etc.
Ideal para clases que principalmente almacenan datos.
""")

from dataclasses import dataclass, field
from typing import List

@dataclass
class Punto:
    """Punto en coordenadas 2D."""
    x: float
    y: float

    def distancia_al_origen(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)


@dataclass
class Persona:
    """Persona con datos básicos."""
    nombre: str
    edad: int
    email: str = ""  # Valor por defecto

    def es_adulto(self):
        return self.edad >= 18


@dataclass(order=True)  # Habilita comparaciones
class Estudiante:
    """Estudiante ordenable por promedio."""
    sort_index: float = field(init=False, repr=False)
    nombre: str
    notas: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.sort_index = self.promedio

    @property
    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0


# Usar dataclasses
p1 = Punto(3, 4)
p2 = Punto(3, 4)
p3 = Punto(1, 1)

print(f"Punto: {p1}")
print(f"Distancia al origen: {p1.distancia_al_origen()}")
print(f"p1 == p2: {p1 == p2}")  # __eq__ generado automáticamente
print(f"p1 == p3: {p1 == p3}")

persona = Persona("Ana", 25, "ana@email.com")
print(f"\nPersona: {persona}")
print(f"Es adulto: {persona.es_adulto()}")

# Estudiantes ordenables
e1 = Estudiante("Luis", [85, 90, 88])
e2 = Estudiante("María", [95, 92, 98])
e3 = Estudiante("Carlos", [70, 75, 80])

estudiantes = [e1, e2, e3]
print("\nEstudiantes ordenados por promedio:")
for est in sorted(estudiantes, reverse=True):
    print(f"  {est.nombre}: {est.promedio:.1f}")


# ==============================================================================
# SLOTS (OPTIMIZACIÓN DE MEMORIA)
# ==============================================================================

print("\n" + "=" * 60)
print("SLOTS (Optimización)")
print("=" * 60)

print("""
__slots__ restringe los atributos permitidos y reduce uso de memoria.
Útil cuando se crean muchas instancias.
""")

class PuntoNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PuntoSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


import sys

p_normal = PuntoNormal(1, 2)
p_slots = PuntoSlots(1, 2)

print(f"Tamaño PuntoNormal: {sys.getsizeof(p_normal)} bytes + __dict__")
print(f"Tamaño PuntoSlots: {sys.getsizeof(p_slots)} bytes")

# PuntoNormal permite atributos dinámicos
p_normal.z = 3
print(f"\nPuntoNormal.z = {p_normal.z} (permitido)")

# PuntoSlots no permite
try:
    p_slots.z = 3
except AttributeError as e:
    print(f"PuntoSlots.z = Error: {e}")


# ==============================================================================
# EJEMPLO COMPLETO: SISTEMA DE EMPLEADOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO COMPLETO: SISTEMA DE EMPLEADOS")
print("=" * 60)

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from datetime import date

@dataclass
class InformacionPersonal:
    """Información personal de un empleado."""
    nombre: str
    fecha_nacimiento: date
    direccion: str = ""
    telefono: str = ""

    @property
    def edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year


class Empleado(ABC):
    """Clase abstracta base para empleados."""

    _id_counter = 0

    def __init__(self, info_personal: InformacionPersonal, salario_base: float):
        Empleado._id_counter += 1
        self.id = Empleado._id_counter
        self.info = info_personal
        self._salario_base = salario_base
        self.activo = True

    @property
    def salario_base(self):
        return self._salario_base

    @abstractmethod
    def calcular_salario(self) -> float:
        """Calcula el salario total."""
        pass

    @abstractmethod
    def descripcion_puesto(self) -> str:
        """Describe el puesto."""
        pass

    def __str__(self):
        return f"[{self.id}] {self.info.nombre} - {self.descripcion_puesto()}"


class Desarrollador(Empleado):
    """Desarrollador de software."""

    def __init__(self, info_personal, salario_base, lenguajes: List[str]):
        super().__init__(info_personal, salario_base)
        self.lenguajes = lenguajes
        self.bono_tecnologia = 500 * len(lenguajes)

    def calcular_salario(self):
        return self._salario_base + self.bono_tecnologia

    def descripcion_puesto(self):
        return f"Desarrollador ({', '.join(self.lenguajes)})"


class Gerente(Empleado):
    """Gerente con equipo a cargo."""

    def __init__(self, info_personal, salario_base, departamento: str):
        super().__init__(info_personal, salario_base)
        self.departamento = departamento
        self.equipo: List[Empleado] = []

    def agregar_empleado(self, empleado: Empleado):
        self.equipo.append(empleado)

    def calcular_salario(self):
        bono_equipo = 100 * len(self.equipo)
        return self._salario_base + bono_equipo

    def descripcion_puesto(self):
        return f"Gerente de {self.departamento} ({len(self.equipo)} empleados)"


class Practicante(Empleado):
    """Practicante o pasante."""

    def __init__(self, info_personal, salario_base, universidad: str):
        super().__init__(info_personal, salario_base)
        self.universidad = universidad

    def calcular_salario(self):
        return self._salario_base  # Sin bonos

    def descripcion_puesto(self):
        return f"Practicante de {self.universidad}"


# Crear empleados
info1 = InformacionPersonal("Ana García", date(1990, 5, 15))
info2 = InformacionPersonal("Luis Martínez", date(1985, 8, 20))
info3 = InformacionPersonal("María López", date(2000, 3, 10))

dev = Desarrollador(info1, 5000, ["Python", "JavaScript", "Go"])
gerente = Gerente(info2, 7000, "Tecnología")
practicante = Practicante(info3, 1500, "UNAM")

gerente.agregar_empleado(dev)
gerente.agregar_empleado(practicante)

empleados = [dev, gerente, practicante]

print("Empleados:")
for emp in empleados:
    print(f"  {emp}")
    print(f"    Salario: ${emp.calcular_salario():,.2f}")
    print(f"    Edad: {emp.info.edad} años")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea una jerarquía de clases para un RPG:
   - Clase abstracta Personaje (nombre, vida, ataque)
   - Subclases: Guerrero, Mago, Arquero
   - Cada uno con habilidad especial diferente

2. Implementa un sistema de formas geométricas 3D:
   - Clase abstracta Forma3D
   - Subclases: Cubo, Esfera, Cilindro
   - Métodos: volumen(), area_superficie()

3. Crea un sistema de notificaciones con mixins:
   - EmailMixin, SMSMixin, PushMixin
   - Clase Usuario que puede usar cualquier combinación

4. Implementa el patrón Observer:
   - Clase Observable (sujeto)
   - Clase Observer (observador)
   - Ejemplo: Sistema de noticias

5. Crea un sistema de permisos usando composición:
   - Clase Permiso
   - Clase Rol (tiene múltiples permisos)
   - Clase Usuario (tiene múltiples roles)

6. Diseña un sistema de comercio electrónico:
   - Carrito, Producto, Usuario, Pedido
   - Usa dataclasses donde sea apropiado
   - Implementa descuentos polimórficos
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 18_decoradores.py")
print("=" * 60)
