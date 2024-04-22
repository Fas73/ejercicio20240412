# print ("Ingrese un número entero entre 7 y 10, para generar su serie Fibonacci")
# print()
# nTerminos = int(input("¿Cuántos términos?"))
# n1, n2 = 0,1
# count = 0

# if nTerminos <= 0:
#     print("Por favor, ingrese un número entero positivo...")

# elif nTerminos==1:
#     print("Secuencia de Fibonacci hasta ", nTerminos, ":")
#     print(n1)
# else:
#     print("Secuencia de Fibonacci:")
#     while count < nTerminos:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count +=1


# while True:
#     try:
#         n = int(input("Ingrese un número entero entre 7 y 10 para generar secuencia Fibonacci: "))
#         if 7 <= n <= 10:
#             break
#         else:
#             print("Por favor, ingrese un número entero válido")

# n1,n2 = 0,1
# count = 0

# print(f"Serie de Fibonacci de los primeros {n} números:")

# while count < n:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1


while True:
    try:
        n = int(input("Ingrese un número entero entre 7 y 10 para generar su serie Fibonacci: "))
        if 7 <= n <= 10:
            break
        else:
            print()
            print("Por favor, ingrese un número entero entre 7 y 10.")
            print()
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

n1, n2 = 0, 1
count = 0

print("Serie Fibonacci hasta el término", n, ":")
while count < n:
    print(n1)
    nth = n1 + n2
    # Actualizar valores
    n1 = n2
    n2 = nth
    count += 1

# def fibonacci(n):
#     n1, n2 = 0, 1
#     count = 0
#     series = []

#     while count < n:
#         series.append(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

#     return series

# def golden_ratio(n):
#     fib_series = fibonacci(n)
    
#     # Calcula el número áureo
#     golden_ratio = fib_series[-1] / fib_series[-2]
    
#     return golden_ratio

# valid_numbers = [7, 8, 9, 10]

# while True:
#     try:
#         n = int(input("Ingrese un número entre 7, 8, 9 y 10 para obtener el número áureo: "))
        
#         if n in valid_numbers:
#             break
#         else:
#             print("Por favor, ingrese un número válido entre 7, 8, 9 y 10.")
#     except ValueError:
#         print("Por favor, ingrese un número entero válido.")

# ratio = golden_ratio(n)
# print(f"Número Áureo para los primeros {n} números: {ratio}")


