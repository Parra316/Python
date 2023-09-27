
primer_lista = [x for x in range(0, 11)]
segunda_lista = [x**2 for x in range(0, 11)]

for index, letra in zip(primer_lista, segunda_lista):
    print(f'{index}.- {letra}')


celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)