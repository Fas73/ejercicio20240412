# Solicita al usuario ingresar un número y verifica si es un entero

numero = input("Ingrese un número:\n")

try:
    numero = int(numero)
    print(f"El número ingresado es {numero} y es un entero válido.")
except ValueError:
    raise ValueError(f"{numero} debe ser un número entero")
