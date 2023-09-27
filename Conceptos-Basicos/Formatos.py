area = 0
Altura = 10
Ancho = 20

#calculate the area of a triangle
area = Ancho * Altura /2 

#printing formatted float value with 2 decimal places
print("El Area del triangulo es igual a: %.2f" % area)

#printing the formatted decimal number with right justified to take up 6 spaces
#with leading zeros
print("Mi numero favorito es el: %06d !" % 42)

#do the same thing with the .format syntax to include numbers our output
print("El Area del triangulo es igual a: {0:f} ".format(area))
print("Mis numeros favoritos son: {0:d} y {1:d}".format(42, 34))

#this is an example with multiple numbers
#I have used the \ to indicate command continues on next line
print("Aqui hay 3 numeros:  " + \
    "El primero es: {p:d}, el segundo es: {s:5d} y por ultimo el: {t:d}".format(p=7,s=8,t=9))


valor1 = 4
valor2 = 5
valor3 = 6

print(f'los valores son: {valor1}, {valor2}, {valor3}')