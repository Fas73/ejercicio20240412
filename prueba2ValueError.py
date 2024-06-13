try:
    numero = int(input("Ingrese un número:\n"))
except ValueError:
    raise ValueError("Debe ingresar un número entero")

print(f"El número ingresado es {numero} y es un entero válido.")
