def main():
    productos = {
        "Agua": 600,
        "Azúcar": 1200,
        "Aceite": 1500,
        "Arroz": 1250,
        "Fideos": 790,
        "Bebida": 1780,
        "Chocolate": 2500,
        "Pan molde": 1340
    }

    total = 0
    preferencial = input("¿Es cliente preferencial? (s/n): ").lower() == 's'

    for producto, precio in productos.items():
        print(f"{producto} - ${precio}")
        seleccion = input(f"¿Desea llevar {producto}? (s/n): ").lower()
        if seleccion == 's':
            total += precio

    if preferencial:
        total *= 0.75  # Aplicar descuento del 25%

    print(f"Total a pagar: ${total}")

    efectivo = float(input("Ingrese el efectivo: "))
    
    if efectivo >= total:
        vuelto = efectivo - total
        print(f"Vuelto: ${vuelto}")
    else:
        print("Dinero insuficiente, Guardias!")

if __name__ == "__main__":
    main()


