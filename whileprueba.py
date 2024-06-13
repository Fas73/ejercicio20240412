banderaSexo = True
while banderaSexo:
    try:
        sexo = input("\nIngrese sexo (F/M): ").upper()
        while "F" not in sexo and "M" not in sexo:
            sexo = input("Ingrese sexo, con las letras 'M' o 'F': ").upper()
        banderaSexo = False
    except:
        print("El caracter ingresado es incorrecto. Intente 'M' o 'F'...")