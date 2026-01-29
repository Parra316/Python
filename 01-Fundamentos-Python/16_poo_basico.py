"""
================================================================================
PROGRAMACIÓN ORIENTADA A OBJETOS (POO) - BÁSICO
================================================================================

La POO es un paradigma de programación que organiza el código en "objetos"
que combinan datos (atributos) y comportamiento (métodos).

CONCEPTOS CLAVE:
- Clase: plantilla/molde para crear objetos
- Objeto/Instancia: ejemplar concreto creado a partir de una clase
- Atributo: variable que pertenece a un objeto
- Método: función que pertenece a un objeto

VENTAJAS:
- Organización del código
- Reutilización (herencia)
- Encapsulamiento
- Modelado del mundo real

================================================================================
"""

# ==============================================================================
# CREAR UNA CLASE BÁSICA
# ==============================================================================

print("=" * 60)
print("CREAR UNA CLASE BÁSICA")
print("=" * 60)

# Clase más simple posible
class MiPrimeraClase:
    """Una clase vacía."""
    pass

# Crear instancia (objeto)
objeto = MiPrimeraClase()
print(f"Objeto creado: {objeto}")
print(f"Tipo: {type(objeto)}")

# Clase con atributos de clase
class Perro:
    """Clase que representa un perro."""
    # Atributo de clase (compartido por todas las instancias)
    especie = "Canis familiaris"

perro1 = Perro()
perro2 = Perro()
print(f"\nPerro1 especie: {perro1.especie}")
print(f"Perro2 especie: {perro2.especie}")
print(f"¿Mismo atributo?: {perro1.especie is perro2.especie}")


# ==============================================================================
# EL MÉTODO __init__ (CONSTRUCTOR)
# ==============================================================================

print("\n" + "=" * 60)
print("EL MÉTODO __init__ (CONSTRUCTOR)")
print("=" * 60)

print("""
__init__ es el método inicializador (constructor).
Se ejecuta automáticamente al crear un objeto.
'self' es una referencia al objeto que se está creando.
""")

class Persona:
    """Clase que representa una persona."""

    def __init__(self, nombre, edad):
        """Inicializa una nueva persona."""
        # Atributos de instancia (únicos para cada objeto)
        self.nombre = nombre
        self.edad = edad
        print(f"  ¡Persona '{nombre}' creada!")

print("Creando personas:")
persona1 = Persona("Ana", 25)
persona2 = Persona("Luis", 30)

print(f"\nPersona 1: {persona1.nombre}, {persona1.edad} años")
print(f"Persona 2: {persona2.nombre}, {persona2.edad} años")

# Cada objeto tiene sus propios atributos
print(f"\n¿Mismo nombre?: {persona1.nombre is persona2.nombre}")


# ==============================================================================
# ATRIBUTOS DE CLASE VS INSTANCIA
# ==============================================================================

print("\n" + "=" * 60)
print("ATRIBUTOS DE CLASE VS INSTANCIA")
print("=" * 60)

class Empleado:
    """Clase que demuestra atributos de clase vs instancia."""

    # Atributo de clase - compartido por todos
    empresa = "TechCorp"
    contador_empleados = 0

    def __init__(self, nombre, salario):
        # Atributos de instancia - únicos por objeto
        self.nombre = nombre
        self.salario = salario
        self.id = Empleado.contador_empleados
        Empleado.contador_empleados += 1

emp1 = Empleado("María", 50000)
emp2 = Empleado("Carlos", 55000)
emp3 = Empleado("Elena", 60000)

print(f"Empresa (clase): {Empleado.empresa}")
print(f"Total empleados: {Empleado.contador_empleados}")
print(f"\nEmpleado 1: {emp1.nombre}, ID: {emp1.id}, Empresa: {emp1.empresa}")
print(f"Empleado 2: {emp2.nombre}, ID: {emp2.id}, Empresa: {emp2.empresa}")
print(f"Empleado 3: {emp3.nombre}, ID: {emp3.id}, Empresa: {emp3.empresa}")

# Modificar atributo de clase afecta a todos
Empleado.empresa = "NewTech Inc"
print(f"\nDespués de cambiar empresa de clase:")
print(f"  emp1.empresa = {emp1.empresa}")
print(f"  emp2.empresa = {emp2.empresa}")


# ==============================================================================
# MÉTODOS
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS")
print("=" * 60)

print("""
Los métodos son funciones definidas dentro de una clase.
El primer parámetro siempre es 'self' (la instancia).
""")

class Rectangulo:
    """Clase que representa un rectángulo."""

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        """Calcula el área del rectángulo."""
        return self.ancho * self.alto

    def perimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        """Verifica si es un cuadrado."""
        return self.ancho == self.alto

    def escalar(self, factor):
        """Escala el rectángulo por un factor."""
        self.ancho *= factor
        self.alto *= factor

    def descripcion(self):
        """Retorna una descripción del rectángulo."""
        tipo = "cuadrado" if self.es_cuadrado() else "rectángulo"
        return f"{tipo} de {self.ancho}x{self.alto}"


rect = Rectangulo(5, 3)
print(f"Rectángulo: {rect.ancho}x{rect.alto}")
print(f"Área: {rect.area()}")
print(f"Perímetro: {rect.perimetro()}")
print(f"¿Es cuadrado?: {rect.es_cuadrado()}")
print(f"Descripción: {rect.descripcion()}")

print("\nEscalando por factor 2...")
rect.escalar(2)
print(f"Nueva descripción: {rect.descripcion()}")
print(f"Nueva área: {rect.area()}")


# ==============================================================================
# MÉTODOS ESPECIALES (DUNDER METHODS)
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS ESPECIALES (DUNDER METHODS)")
print("=" * 60)

print("""
Los métodos con doble guión bajo (__método__) son especiales.
Python los llama automáticamente en ciertas situaciones.
""")

class Punto:
    """Clase que representa un punto en 2D."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Representación legible (para print)."""
        return f"Punto({self.x}, {self.y})"

    def __repr__(self):
        """Representación técnica (para debug)."""
        return f"Punto(x={self.x}, y={self.y})"

    def __eq__(self, otro):
        """Comparación de igualdad (==)."""
        if isinstance(otro, Punto):
            return self.x == otro.x and self.y == otro.y
        return False

    def __add__(self, otro):
        """Suma de puntos (+)."""
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """Resta de puntos (-)."""
        return Punto(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        """Multiplicación por escalar (*)."""
        return Punto(self.x * escalar, self.y * escalar)

    def __len__(self):
        """Para len() - distancia al origen como entero."""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

    def __bool__(self):
        """Para bool() - False si es el origen."""
        return self.x != 0 or self.y != 0


p1 = Punto(3, 4)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(f"p1 = {p1}")           # Usa __str__
print(f"p2 = {p2}")
print(f"repr(p1) = {repr(p1)}")  # Usa __repr__

print(f"\np1 == p2: {p1 == p2}")  # Usa __eq__
print(f"p1 == p3: {p1 == p3}")

print(f"\np1 + p2 = {p1 + p2}")   # Usa __add__
print(f"p1 - p2 = {p1 - p2}")    # Usa __sub__
print(f"p1 * 3 = {p1 * 3}")      # Usa __mul__

print(f"\nlen(p1) = {len(p1)}")   # Usa __len__
print(f"bool(p1) = {bool(p1)}")  # Usa __bool__
print(f"bool(Punto(0,0)) = {bool(Punto(0, 0))}")


# ==============================================================================
# ENCAPSULAMIENTO
# ==============================================================================

print("\n" + "=" * 60)
print("ENCAPSULAMIENTO")
print("=" * 60)

print("""
El encapsulamiento oculta los detalles internos de una clase.
En Python se usa convención de nombres:
- _atributo: "privado" (convención, no forzado)
- __atributo: name mangling (dificulta acceso externo)
""")

class CuentaBancaria:
    """Cuenta bancaria con encapsulamiento."""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular           # Público
        self._saldo = saldo_inicial      # "Privado" por convención
        self.__pin = "1234"              # Name mangling

    def depositar(self, cantidad):
        """Deposita dinero en la cuenta."""
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """Retira dinero si hay suficiente saldo."""
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

    def consultar_saldo(self):
        """Retorna el saldo actual."""
        return self._saldo

    def verificar_pin(self, pin):
        """Verifica si el PIN es correcto."""
        return self.__pin == pin


cuenta = CuentaBancaria("Ana García", 1000)

print(f"Titular: {cuenta.titular}")
print(f"Saldo: ${cuenta.consultar_saldo()}")

cuenta.depositar(500)
print(f"Después de depositar $500: ${cuenta.consultar_saldo()}")

cuenta.retirar(200)
print(f"Después de retirar $200: ${cuenta.consultar_saldo()}")

# Acceso a atributo "privado" (posible pero no recomendado)
print(f"\n_saldo (acceso directo): ${cuenta._saldo}")

# Name mangling - __pin se convierte en _CuentaBancaria__pin
# print(cuenta.__pin)  # Error: AttributeError
print(f"__pin con name mangling: {cuenta._CuentaBancaria__pin}")
print("(No se debe hacer esto en código real)")


# ==============================================================================
# PROPIEDADES (GETTERS Y SETTERS)
# ==============================================================================

print("\n" + "=" * 60)
print("PROPIEDADES (GETTERS Y SETTERS)")
print("=" * 60)

print("""
Las propiedades permiten definir getters y setters con sintaxis de atributo.
Útil para validación y cálculos dinámicos.
""")

class Temperatura:
    """Clase que maneja temperatura con conversión automática."""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter para celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Setter para celsius con validación."""
        if valor < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Getter para fahrenheit (calculado)."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Setter para fahrenheit."""
        self.celsius = (valor - 32) * 5/9

    @property
    def kelvin(self):
        """Getter para kelvin."""
        return self._celsius + 273.15


temp = Temperatura(25)
print(f"Temperatura inicial: {temp.celsius}°C")
print(f"En Fahrenheit: {temp.fahrenheit}°F")
print(f"En Kelvin: {temp.kelvin}K")

# Usar setters
temp.celsius = 100
print(f"\nDespués de temp.celsius = 100:")
print(f"  Celsius: {temp.celsius}°C, Fahrenheit: {temp.fahrenheit}°F")

temp.fahrenheit = 32
print(f"\nDespués de temp.fahrenheit = 32:")
print(f"  Celsius: {temp.celsius}°C, Fahrenheit: {temp.fahrenheit}°F")

# Validación
try:
    temp.celsius = -300
except ValueError as e:
    print(f"\nError al poner -300°C: {e}")


# ==============================================================================
# MÉTODOS DE CLASE Y ESTÁTICOS
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTODOS DE CLASE Y ESTÁTICOS")
print("=" * 60)

print("""
- Método normal: recibe self (la instancia)
- @classmethod: recibe cls (la clase) - útil para constructores alternativos
- @staticmethod: no recibe self ni cls - utilidad relacionada a la clase
""")

class Fecha:
    """Clase para manejar fechas."""

    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

    # Método de instancia normal
    def es_fin_de_año(self):
        """Verifica si es diciembre."""
        return self.mes == 12

    # Método de clase - constructor alternativo
    @classmethod
    def desde_string(cls, fecha_str):
        """Crea una fecha desde string 'dd/mm/yyyy'."""
        dia, mes, año = map(int, fecha_str.split('/'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        """Crea una fecha con la fecha actual."""
        from datetime import date
        hoy = date.today()
        return cls(hoy.day, hoy.month, hoy.year)

    # Método estático - no necesita instancia ni clase
    @staticmethod
    def es_bisiesto(año):
        """Verifica si un año es bisiesto."""
        return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

    @staticmethod
    def dias_en_mes(mes, año):
        """Retorna días en un mes dado."""
        dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mes == 2 and Fecha.es_bisiesto(año):
            return 29
        return dias[mes - 1]


# Crear con constructor normal
fecha1 = Fecha(15, 6, 2024)
print(f"Fecha normal: {fecha1}")

# Crear con método de clase
fecha2 = Fecha.desde_string("25/12/2024")
print(f"Desde string: {fecha2}")
print(f"¿Es fin de año?: {fecha2.es_fin_de_año()}")

fecha3 = Fecha.hoy()
print(f"Hoy: {fecha3}")

# Métodos estáticos - no necesitan instancia
print(f"\n¿2024 es bisiesto?: {Fecha.es_bisiesto(2024)}")
print(f"¿2023 es bisiesto?: {Fecha.es_bisiesto(2023)}")
print(f"Días en febrero 2024: {Fecha.dias_en_mes(2, 2024)}")
print(f"Días en febrero 2023: {Fecha.dias_en_mes(2, 2023)}")


# ==============================================================================
# EJEMPLO COMPLETO: SISTEMA DE INVENTARIO
# ==============================================================================

print("\n" + "=" * 60)
print("EJEMPLO COMPLETO: SISTEMA DE INVENTARIO")
print("=" * 60)

class Producto:
    """Representa un producto en el inventario."""

    _id_contador = 0

    def __init__(self, nombre, precio, cantidad=0):
        Producto._id_contador += 1
        self._id = Producto._id_contador
        self.nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    @property
    def id(self):
        return self._id

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def valor_total(self):
        """Valor total del stock de este producto."""
        return self._precio * self._cantidad

    def agregar_stock(self, cantidad):
        """Agrega unidades al stock."""
        if cantidad < 0:
            raise ValueError("No se puede agregar cantidad negativa")
        self._cantidad += cantidad

    def vender(self, cantidad):
        """Vende unidades del producto."""
        if cantidad > self._cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {self._cantidad}")
        self._cantidad -= cantidad
        return cantidad * self._precio

    def __str__(self):
        return f"[{self._id}] {self.nombre}: ${self._precio:.2f} (Stock: {self._cantidad})"

    def __repr__(self):
        return f"Producto('{self.nombre}', {self._precio}, {self._cantidad})"


class Inventario:
    """Sistema de gestión de inventario."""

    def __init__(self):
        self._productos = {}

    def agregar_producto(self, producto):
        """Agrega un producto al inventario."""
        self._productos[producto.id] = producto

    def buscar_por_id(self, id):
        """Busca un producto por ID."""
        return self._productos.get(id)

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre (parcial)."""
        nombre = nombre.lower()
        return [p for p in self._productos.values()
                if nombre in p.nombre.lower()]

    def listar_productos(self):
        """Lista todos los productos."""
        return list(self._productos.values())

    def valor_total_inventario(self):
        """Calcula el valor total del inventario."""
        return sum(p.valor_total for p in self._productos.values())

    def productos_sin_stock(self):
        """Retorna productos sin stock."""
        return [p for p in self._productos.values() if p.cantidad == 0]

    def __len__(self):
        return len(self._productos)


# Usar el sistema
print("--- Creando productos ---")
laptop = Producto("Laptop HP", 999.99, 10)
mouse = Producto("Mouse Logitech", 29.99, 50)
teclado = Producto("Teclado Mecánico", 79.99, 30)
monitor = Producto("Monitor 24\"", 199.99, 0)

print(laptop)
print(mouse)
print(teclado)
print(monitor)

print("\n--- Creando inventario ---")
inventario = Inventario()
inventario.agregar_producto(laptop)
inventario.agregar_producto(mouse)
inventario.agregar_producto(teclado)
inventario.agregar_producto(monitor)

print(f"Total productos: {len(inventario)}")
print(f"Valor total inventario: ${inventario.valor_total_inventario():,.2f}")

print("\n--- Operaciones ---")
print(f"Vendiendo 2 laptops: ${laptop.vender(2):,.2f}")
print(f"Stock laptops restante: {laptop.cantidad}")

mouse.agregar_stock(20)
print(f"Stock mouse después de agregar 20: {mouse.cantidad}")

print("\n--- Búsquedas ---")
print(f"Buscar ID 1: {inventario.buscar_por_id(1)}")
print(f"Buscar 'log': {inventario.buscar_por_nombre('log')}")

print("\n--- Productos sin stock ---")
for p in inventario.productos_sin_stock():
    print(f"  {p}")


# ==============================================================================
# EJERCICIOS
# ==============================================================================

print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

print("""
1. Crea una clase Libro con:
   - Atributos: titulo, autor, paginas, leido (bool)
   - Método: marcar_leido()
   - Método especial __str__

2. Crea una clase Circulo con:
   - Atributo: radio
   - Propiedades: diametro, area, perimetro
   - El radio no puede ser negativo

3. Crea una clase Estudiante con:
   - Atributos: nombre, notas (lista)
   - Métodos: agregar_nota, promedio, estado (Aprobado/Reprobado)
   - Método de clase: desde_diccionario

4. Crea una clase Vector con operaciones matemáticas:
   - Suma, resta, producto punto
   - Métodos especiales para +, -, *, ==
   - Propiedad: magnitud

5. Crea un sistema de biblioteca con:
   - Clase Libro
   - Clase Usuario
   - Clase Biblioteca (gestiona préstamos)

6. Implementa una clase Fraccion que soporte:
   - Suma, resta, multiplicación, división
   - Simplificación automática
   - Representación como string
""")

print("\n" + "=" * 60)
print("SIGUIENTE: 17_poo_avanzado.py")
print("=" * 60)
