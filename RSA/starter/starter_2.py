p, q = 17, 23 # primos
N = p * q # cálculo
e = 65537 # exponente
number = 12 # número a codificar

c = (number**e) % N # respuesta

print (c) # impresión del valor

