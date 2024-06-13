from funciones20240607 import *

# cantidad_sin_iva = int(input("\nIngrese el valor neto para calcular el IVA: \n"))
# calcular_total_factura(cantidad_sin_iva)
cls()

while True:
    try:
        # Solicitar al usuario que ingrese una cifra
        cantidad_sin_iva = float(input("Ingrese el valor neto para calcular el IVA: "))
        # Calcular el total de la factura con IVA
        calcular_total_factura(cantidad_sin_iva)
        break  # Salir del bucle después de una entrada válida
    except:
        print("Por favor ingrese un valor numérico válido...")


while True:
    try:
        # Solicitar al usuario que ingrese el radio
        radio = float(input("\nIngrese el radio del círculo: "))
        
        # Validar que el radio sea un número positivo
        if radio <= 0:
            print("\nPor favor, ingrese un número positivo...")
            continue
        
        # Calcular el área del círculo
        area = area_circulo(radio)
        
        # Mostrar el resultado
        print(f"\nEl área del círculo con radio {radio} es {area:.2f}")
        break
    
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número...")


while True:
    try:
        # Solicitar al usuario que ingrese los números separados por comas
        entrada = input("\nIngrese una lista de números separados por comas: ")
        # Convertir la entrada en una lista de números
        lista_numeros = [float(num) for num in entrada.split(',')]
        # Calcular la media
        media = media_lista(lista_numeros)
        # Mostrar el resultado
        print(f"\nLa media de los números ingresados es: {media:.2f}")
        break  # Salir del bucle después de una entrada válida
    except:
        print("\nPor favor, ingrese una lista válida de números separados por comas...")


while True:
    try:
        # Solicitar al usuario que ingrese los números separados por comas
        entrada = input("\nIngrese una lista de números separados por comas: ")
        # Convertir la entrada en una lista de números
        lista_numeros = [float(num) for num in entrada.split(',')]
        # Calcular los cuadrados
        cuadrados = cuadrados_lista(lista_numeros)
        # Mostrar el resultado
        print(f"\nLos cuadrados de los números ingresados son: {cuadrados}")
        break  # Salir del bucle después de una entrada válida
    except:
        print("\nPor favor ingrese una lista válida de números separados por comas...")

while True:
    try:
        # Solicitar al usuario que ingrese una cadena de texto
        texto = input("\nIngrese una cadena de texto: ")
        # Verificar que la cadena no esté vacía
        if texto.strip() == "":
            errar=("\nLa cadena no puede estar vacía...")
            print(errar)
        # Contar las palabras en la cadena
        numero_de_palabras = contar_palabras(texto)
        # Mostrar el resultado
        print(f"\nLa cantidad de palabras en la cadena ingresada es: {numero_de_palabras}")
        break  # Salir del bucle después de una entrada válida
    except:
        print(errar)

while True:
    try:
        # Solicitar al usuario que ingrese una cadena de texto
        texto = input("\nIngrese una cadena de texto: ")
        # Verificar que la cadena no esté vacía
        if texto.strip() == "":
            errar=("\nLa cadena no puede estar vacía...")
            print(errar)
        # Contar las letras en la cadena
        numero_de_letras = contar_letras(texto)
        # Mostrar el resultado
        print(f"\nLa cantidad de letras en la cadena ingresada es: {numero_de_letras}")
        break  # Salir del bucle después de una entrada válida
    except:
        print(errar)
