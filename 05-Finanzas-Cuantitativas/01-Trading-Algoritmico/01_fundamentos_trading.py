"""
================================================================================
FUNDAMENTOS DE TRADING ALGORÍTMICO
================================================================================

ADVERTENCIA:
-----------
- El trading conlleva riesgo de pérdida de capital
- Los ejemplos son educativos, no consejos de inversión
- Siempre hacer backtesting antes de operar con dinero real
- Considerar comisiones, slippage y otros costos

¿QUÉ ES EL TRADING ALGORÍTMICO?
------------------------------
Es el uso de programas informáticos para ejecutar operaciones
de compra/venta siguiendo reglas predefinidas.

VENTAJAS:
- Elimina emociones del trading
- Puede operar 24/7
- Ejecuta operaciones más rápido
- Permite backtesting

PYTHON EN FINANZAS:
------------------
- Análisis de datos financieros
- Backtesting de estrategias
- Conexión con APIs de brokers
- Machine Learning para predicciones

================================================================================
"""

import numpy as np
from datetime import datetime, timedelta
from collections import defaultdict

# ==============================================================================
# CONCEPTOS BÁSICOS DE MERCADOS
# ==============================================================================

print("=" * 60)
print("CONCEPTOS BÁSICOS DE MERCADOS FINANCIEROS")
print("=" * 60)

print("""
TIPOS DE DATOS FINANCIEROS:
--------------------------
- OHLCV: Open, High, Low, Close, Volume
- Tick data: Cada transacción individual
- Order book: Órdenes de compra/venta pendientes

TIPOS DE ÓRDENES:
----------------
- Market order: Compra/vende al precio actual
- Limit order: Compra/vende a un precio específico
- Stop loss: Vende si el precio baja de cierto nivel
- Take profit: Vende si el precio sube a cierto nivel

MÉTRICAS IMPORTANTES:
--------------------
- Retorno: Cambio porcentual del precio
- Volatilidad: Variación de los retornos
- Sharpe Ratio: Retorno ajustado por riesgo
- Drawdown: Caída desde el máximo
""")


# ==============================================================================
# SIMULACIÓN DE DATOS DE MERCADO
# ==============================================================================

print("\n" + "=" * 60)
print("SIMULACIÓN DE DATOS DE MERCADO")
print("=" * 60)


def generar_datos_ohlcv(dias=100, precio_inicial=100, volatilidad=0.02):
    """
    Genera datos OHLCV simulados usando movimiento browniano geométrico.

    En la práctica, usar APIs como:
    - yfinance: pip install yfinance
    - Alpha Vantage
    - Polygon.io
    """
    np.random.seed(42)

    fechas = []
    precios_close = [precio_inicial]

    # Generar precios usando random walk
    for i in range(dias - 1):
        retorno = np.random.normal(0.0005, volatilidad)  # Ligero sesgo positivo
        nuevo_precio = precios_close[-1] * (1 + retorno)
        precios_close.append(nuevo_precio)

    # Generar OHLCV
    datos = []
    fecha_inicial = datetime.now() - timedelta(days=dias)

    for i in range(dias):
        fecha = fecha_inicial + timedelta(days=i)
        close = precios_close[i]

        # Simular variación intradía
        variacion = close * volatilidad
        high = close + abs(np.random.normal(0, variacion))
        low = close - abs(np.random.normal(0, variacion))
        open_price = low + (high - low) * np.random.random()

        # Volumen aleatorio
        volumen = int(np.random.exponential(1000000))

        datos.append({
            'fecha': fecha.strftime('%Y-%m-%d'),
            'open': round(open_price, 2),
            'high': round(high, 2),
            'low': round(low, 2),
            'close': round(close, 2),
            'volume': volumen
        })

    return datos


# Generar datos de ejemplo
datos_mercado = generar_datos_ohlcv(100)
print(f"Generados {len(datos_mercado)} días de datos OHLCV")
print(f"\nÚltimos 5 días:")
for d in datos_mercado[-5:]:
    print(f"  {d['fecha']}: O={d['open']:.2f} H={d['high']:.2f} L={d['low']:.2f} C={d['close']:.2f}")


# ==============================================================================
# CÁLCULO DE INDICADORES TÉCNICOS
# ==============================================================================

print("\n" + "=" * 60)
print("INDICADORES TÉCNICOS")
print("=" * 60)


def calcular_sma(precios, periodo):
    """
    Simple Moving Average (Media Móvil Simple).

    SMA = Promedio de los últimos N precios.
    """
    if len(precios) < periodo:
        return []

    sma = []
    for i in range(periodo - 1, len(precios)):
        promedio = sum(precios[i - periodo + 1:i + 1]) / periodo
        sma.append(promedio)

    return sma


def calcular_ema(precios, periodo):
    """
    Exponential Moving Average (Media Móvil Exponencial).

    Da más peso a los precios recientes.
    """
    if len(precios) < periodo:
        return []

    multiplicador = 2 / (periodo + 1)
    ema = [sum(precios[:periodo]) / periodo]  # Primer EMA es SMA

    for precio in precios[periodo:]:
        nuevo_ema = (precio - ema[-1]) * multiplicador + ema[-1]
        ema.append(nuevo_ema)

    return ema


def calcular_rsi(precios, periodo=14):
    """
    Relative Strength Index (Índice de Fuerza Relativa).

    RSI > 70: Sobrecomprado (posible caída)
    RSI < 30: Sobrevendido (posible subida)
    """
    if len(precios) < periodo + 1:
        return []

    # Calcular cambios
    cambios = [precios[i] - precios[i-1] for i in range(1, len(precios))]

    # Separar ganancias y pérdidas
    ganancias = [max(0, c) for c in cambios]
    perdidas = [abs(min(0, c)) for c in cambios]

    # Promedio inicial
    avg_ganancia = sum(ganancias[:periodo]) / periodo
    avg_perdida = sum(perdidas[:periodo]) / periodo

    rsi = []
    for i in range(periodo, len(cambios)):
        avg_ganancia = (avg_ganancia * (periodo - 1) + ganancias[i]) / periodo
        avg_perdida = (avg_perdida * (periodo - 1) + perdidas[i]) / periodo

        if avg_perdida == 0:
            rsi.append(100)
        else:
            rs = avg_ganancia / avg_perdida
            rsi.append(100 - (100 / (1 + rs)))

    return rsi


# Calcular indicadores
precios_close = [d['close'] for d in datos_mercado]

sma_20 = calcular_sma(precios_close, 20)
ema_12 = calcular_ema(precios_close, 12)
rsi_14 = calcular_rsi(precios_close, 14)

print("\nIndicadores calculados:")
print(f"  SMA(20): {len(sma_20)} valores, último = {sma_20[-1]:.2f}")
print(f"  EMA(12): {len(ema_12)} valores, último = {ema_12[-1]:.2f}")
print(f"  RSI(14): {len(rsi_14)} valores, último = {rsi_14[-1]:.2f}")


# ==============================================================================
# ESTRATEGIA DE TRADING SIMPLE
# ==============================================================================

print("\n" + "=" * 60)
print("ESTRATEGIA: Cruce de Medias Móviles")
print("=" * 60)

print("""
ESTRATEGIA DE CRUCE DE MEDIAS:
- Comprar cuando SMA corto cruza hacia arriba el SMA largo
- Vender cuando SMA corto cruza hacia abajo el SMA largo

Es una estrategia de seguimiento de tendencia.
""")


class EstrategiaCruceMedias:
    """
    Estrategia de cruce de medias móviles.
    """

    def __init__(self, periodo_corto=10, periodo_largo=20):
        self.periodo_corto = periodo_corto
        self.periodo_largo = periodo_largo
        self.posicion = 0  # 0: sin posición, 1: comprado
        self.historial = []

    def calcular_señal(self, precios):
        """
        Calcula señal de trading.
        Retorna: 1 (comprar), -1 (vender), 0 (mantener)
        """
        if len(precios) < self.periodo_largo:
            return 0

        sma_corto = calcular_sma(precios, self.periodo_corto)
        sma_largo = calcular_sma(precios, self.periodo_largo)

        if len(sma_corto) < 2 or len(sma_largo) < 2:
            return 0

        # Ajustar índices (SMA largo tiene menos valores)
        offset = self.periodo_largo - self.periodo_corto

        # Señal de cruce
        cruce_actual = sma_corto[-1] > sma_largo[-1]
        cruce_anterior = sma_corto[-2] > sma_largo[-1 - offset] if len(sma_largo) > 1 else cruce_actual

        if cruce_actual and not cruce_anterior:
            return 1  # Cruce alcista: comprar
        elif not cruce_actual and cruce_anterior:
            return -1  # Cruce bajista: vender

        return 0  # Mantener

    def ejecutar_backtest(self, datos):
        """
        Ejecuta backtest de la estrategia.
        """
        capital_inicial = 10000
        capital = capital_inicial
        acciones = 0
        operaciones = []
        precios = []

        for i, d in enumerate(datos):
            precios.append(d['close'])

            if i < self.periodo_largo:
                continue

            señal = self.calcular_señal(precios)

            if señal == 1 and self.posicion == 0:
                # Comprar
                acciones = capital / d['close']
                capital = 0
                self.posicion = 1
                operaciones.append({
                    'tipo': 'COMPRA',
                    'fecha': d['fecha'],
                    'precio': d['close'],
                    'acciones': acciones
                })

            elif señal == -1 and self.posicion == 1:
                # Vender
                capital = acciones * d['close']
                self.posicion = 0
                operaciones.append({
                    'tipo': 'VENTA',
                    'fecha': d['fecha'],
                    'precio': d['close'],
                    'capital': capital
                })
                acciones = 0

        # Valor final
        if self.posicion == 1:
            capital_final = acciones * datos[-1]['close']
        else:
            capital_final = capital

        return {
            'capital_inicial': capital_inicial,
            'capital_final': round(capital_final, 2),
            'retorno_pct': round((capital_final / capital_inicial - 1) * 100, 2),
            'operaciones': len([o for o in operaciones if o['tipo'] == 'COMPRA']),
            'historial': operaciones
        }


# Ejecutar backtest
estrategia = EstrategiaCruceMedias(periodo_corto=10, periodo_largo=20)
resultados = estrategia.ejecutar_backtest(datos_mercado)

print(f"\nResultados del backtest:")
print(f"  Capital inicial: ${resultados['capital_inicial']:,.2f}")
print(f"  Capital final: ${resultados['capital_final']:,.2f}")
print(f"  Retorno: {resultados['retorno_pct']}%")
print(f"  Número de operaciones: {resultados['operaciones']}")

print("\nHistorial de operaciones:")
for op in resultados['historial'][:6]:
    print(f"  {op['tipo']:6} | {op['fecha']} | ${op['precio']:.2f}")


# ==============================================================================
# MÉTRICAS DE RENDIMIENTO
# ==============================================================================

print("\n" + "=" * 60)
print("MÉTRICAS DE RENDIMIENTO")
print("=" * 60)


def calcular_metricas(precios, retornos_estrategia):
    """
    Calcula métricas de rendimiento de una estrategia.
    """
    retornos = []
    for i in range(1, len(precios)):
        retorno = (precios[i] - precios[i-1]) / precios[i-1]
        retornos.append(retorno)

    # Retorno total
    retorno_total = (precios[-1] / precios[0] - 1) * 100

    # Volatilidad anualizada (asumiendo datos diarios)
    volatilidad = np.std(retornos) * np.sqrt(252) * 100

    # Sharpe Ratio (asumiendo tasa libre de riesgo = 2%)
    retorno_anual = np.mean(retornos) * 252 * 100
    sharpe = (retorno_anual - 2) / volatilidad if volatilidad > 0 else 0

    # Maximum Drawdown
    max_precio = precios[0]
    max_drawdown = 0
    for precio in precios:
        if precio > max_precio:
            max_precio = precio
        drawdown = (max_precio - precio) / max_precio * 100
        if drawdown > max_drawdown:
            max_drawdown = drawdown

    return {
        'retorno_total': round(retorno_total, 2),
        'volatilidad_anual': round(volatilidad, 2),
        'sharpe_ratio': round(sharpe, 2),
        'max_drawdown': round(max_drawdown, 2)
    }


metricas = calcular_metricas(precios_close, None)

print(f"Métricas del activo (Buy & Hold):")
print(f"  Retorno total: {metricas['retorno_total']}%")
print(f"  Volatilidad anualizada: {metricas['volatilidad_anual']}%")
print(f"  Sharpe Ratio: {metricas['sharpe_ratio']}")
print(f"  Maximum Drawdown: {metricas['max_drawdown']}%")


# ==============================================================================
# LIBRERÍAS Y HERRAMIENTAS
# ==============================================================================

print("\n" + "=" * 60)
print("LIBRERÍAS PARA TRADING")
print("=" * 60)

print("""
DATOS DE MERCADO:
  pip install yfinance       # Yahoo Finance (gratis)
  pip install alpha_vantage  # Alpha Vantage API
  pip install polygon-api    # Polygon.io (profesional)

ANÁLISIS TÉCNICO:
  pip install ta             # Indicadores técnicos
  pip install talib          # TA-Lib (más completo)
  pip install pandas-ta      # Pandas + TA

BACKTESTING:
  pip install backtrader     # Framework de backtesting
  pip install zipline        # Quantopian (avanzado)
  pip install bt             # Backtesting simple

BROKERS (APIs para trading real):
  pip install alpaca-trade-api  # Alpaca (sin comisiones)
  pip install ib_insync         # Interactive Brokers
  pip install ccxt              # Exchanges de crypto

MACHINE LEARNING:
  pip install scikit-learn   # ML clásico
  pip install tensorflow     # Deep Learning
  pip install pytorch        # Deep Learning
""")

print("\n" + "=" * 60)
print("PRÓXIMO: Análisis de mercados con yfinance y pandas")
print("=" * 60)
