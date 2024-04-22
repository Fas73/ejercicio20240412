#Ejercicio 5
while True:
  num = int(input("Ingrese número que sea Impar: \n"))
  if(num%2==0):
    print("El número ingresado es Par. Por favor, Ingrese un número Impar: \n")
    continue
  else:
    result = num * 4
    print(f"El número Impar {num} multiplicado por 4 es: {result}\n")
    break