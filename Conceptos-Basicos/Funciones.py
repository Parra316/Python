
#Funciones con *args y **kwargs

"""def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

resultado = suma(1, 2, 3, 4)
print(resultado)"""
# Salida: 10

"""def detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

detalles(nombre="Juan", edad=30, ciudad="Ejemplo")"""

# Salida:
# nombre: Juan
# edad: 30
# ciudad: Ejemplo

"""def fun3(*args, **kwargs):
    print(args)
    print(kwargs)
    print("Me gustaria {} {}".format(args[0], kwargs["comida"]))

fun3(12, 23, 34, comida="Ensalada", animal="gato")"""

#Funciones Lambda

primer_lista = [x for x in range(0, 11, 2)]

print(f'Lista de numeros pares: {primer_lista}')

lista_mapeo = list(map(lambda num: num ** 2, primer_lista))

print(f'Lista mapeada con numeros elevados al cuadrado: {lista_mapeo}')

segunda_lista = [x for x in range(0, 11)]

print(f'Lista de numeros: {segunda_lista}')

lista_filtro = list(filter(lambda num: num%2 == 0, segunda_lista))

print(f'Lista con filtro para conocer los numeros pares: {lista_filtro}')

personas = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "María", "edad": 35}
]

personas_ordenadas = sorted(personas, key=lambda x: x["edad"])
print(personas_ordenadas)