print("\n" * 50)

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
    print(f"El número {numero} es primo\n")
else:
    print(f"El número {numero} no es primo\n")
