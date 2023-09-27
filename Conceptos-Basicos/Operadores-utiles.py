
palabra = "hola"

for index in enumerate(palabra):
    print(index)

print("+++++++++++++++++++++++++++++++++")    

for index, letra in enumerate(palabra):
    print(f'{index}.- {letra}')

print("+++++++++++++++++++++++++++++++++")

primer_Lista = [1,2,3]
segunda_Lista = ['a', 'b', 'c']

for item in zip(primer_Lista, segunda_Lista):
    print(item)