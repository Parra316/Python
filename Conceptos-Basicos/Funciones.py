
#Funciones con *args y **kwargs

# def fun1(*args):
#     return print(sum(args)*0.05)

# fun1(40,50,760)

# def fun2(**kwargs):
#     if 'fruit' in kwargs:
#         print('La fruta que escogi es: {}'.format(kwargs['fruit']))
#     else: 
#         print('No hay fruta')

# fun2(fruit = 'mango', vegetal = 'zanahoria')

# def fun3(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print("Me gustaria {} {}".format(args[0], kwargs["comida"]))

# fun3(12, 23, 34, comida="Ensalada", animal="gato")

#Funciones Lambda

primer_lista = [x for x in range(0, 11, 2)]

print(f'Lista de numeros pares: {primer_lista}')

lista_mapeo = list(map(lambda num: num ** 2, primer_lista))

print(f'Lista mapeada con numeros elevados al cuadrado: {lista_mapeo}')

segunda_lista = [x for x in range(0, 11)]

print(f'Lista de numeros: {segunda_lista}')

lista_filtro = list(filter(lambda num: num%2 == 0, segunda_lista))

print(f'Lista con filtro para conocer los numeros pares: {lista_filtro}')