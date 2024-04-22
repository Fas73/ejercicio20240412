def main():
    a = True
    b = True
    c = False
    d = True
    e = False

    resultado = None

    resultado = a or b
    print(f"Resultado 1: {resultado}")

    resultado = a or c
    print(f"Resultado 2: {resultado}")

    resultado = a and e
    print(f"Resultado 3: {resultado}")

    aux1 = a or e
    resultado = aux1 and b
    print(f"Resultado 4: {resultado}")

    resultado = aux1 and c
    print(f"Resultado 5: {resultado}")

    aux2 = c or b
    resultado = aux1 and aux2
    print(f"Resultado 6: {resultado}")

    aux3 = a and b
    resultado = aux3 and c or e
    print(f"Resultado 7: {resultado}")

if __name__ == "__main__":
    main()
