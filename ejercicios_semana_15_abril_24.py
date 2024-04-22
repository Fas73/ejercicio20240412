print("\n" * 50)

# Ejercicio 1
for i in range (5):
    print (i)

# Ejercicio 2
for i in "Hola":
    print (i)

# Ejercicio 3
for i in range (5):
    i= i+2
    print (i)

# Ejercicio 4
numero = int(input("Ingrese un numero para obtener factorial: \n"))
i = 1
fact = 1
while i<=numero:
    fact = fact * i
    i += 1
print(f"el factorial de {numero} es {fact}")

# Ejercicio 5
while True:
  num = int(input("Ingrese número que sea Impar: \n"))
  if(num%2==0):
    print("Error! El número ingresado es Par. Por favor, ingrese un número Impar: \n")
    continue
  else:
    result = num * 4
    print(f"El número Impar {num} multiplicado por 4 es = {result}\n")
    break

#Ejercicio 6
resultado = 1
base = int(input("Ingrese número base: \n"))
exponente = int(input("Ingrese número exponente: \n"))
for i in range(exponente):
  resultado = resultado * base
print(f"El resultado de {base} elevado a {exponente} es = {resultado}")

#Ejercicio 7
numero = int(input("****Ingrese un número:***** \n"))
esPrimo = True
if numero <= 1:
    esPrimo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i==0:
            esPrimo = False
            break
if esPrimo:
    print(f"El número {numero} es primo.\n")
else:
    print(f"El número {numero} no es primo.\n")


#Ejercicio 8
inicio = 1 
fin = 10 
desde = 1 
hasta = 10 
##########
for x in range(inicio, fin + 1):  #range con 2 argumentos por que debo recorrer del 1 al 10 (10+1)
	print(f"Tabla del {x}:") 
	for y in range(desde, hasta + 1):
		print(f'{x} x {y} = {x * y}')
	print() ##aca solo pongo un espacio para darle orden xD

    