def mostrar_asientos(asientos):
    print("\nEstado actual de los asientos:")
    for i in range(0, 120, 8):
        print(f"{i+1:3} {'X' if asientos[i] else 'O'} | "
              f"{i+2:3} {'X' if asientos[i+1] else 'O'} | "
              f"{i+3:3} {'X' if asientos[i+2] else 'O'} | "
              f"{i+4:3} {'X' if asientos[i+3] else 'O'} | "
              f"{i+5:3} {'X' if asientos[i+4] else 'O'} | "
              f"{i+6:3} {'X' if asientos[i+5] else 'O'} | "
              f"{i+7:3} {'X' if asientos[i+6] else 'O'} | "
              f"{i+8:3} {'X' if asientos[i+7] else 'O'}")

def reservar_asiento(asientos, reservas):
    while True:
        try:
            asiento = int(input("Ingrese el número del asiento que desea reservar (1-40): "))
            if asiento < 1 or asiento > 40:
                print("Número de asiento inválido. Intente nuevamente.")
                continue
            if asientos[asiento-1]:
                print("El asiento ya está reservado. Intente con otro asiento.")
                continue
            break
        except:
            print("Entrada inválida. Ingrese un número de asiento.")
    
    nombre = input("\nIngrese su nombre: ").capitalize()
    while nombre.strip() == "":
        nombre = input("\nEl campo no puede venir vacío. Ingrese un nombre válido: ").capitalize()
    while True:
        try:
            rut = int(input("\nIngrese su RUT: "))
            break
        except:
            print("Ingrese su RUT con números...")
    destino = input("\nIngrese ciudad de destino: ").capitalize()
    while destino.strip() == "":
        destino = input("Debe ingresar una ciudad de destino: ").capitalize()
    
    hora_salida = input("\nIngrese la hora de salida: ")
    while hora_salida.strip() == "":
        hora_salida = input("Debe ingresar una hora de salida: ")

    asientos[asiento-1] = True
    reservas[asiento] = {
        'nombre'    : nombre,
        'rut'       : rut,
        'destino'   : destino,
        'hora_salida': hora_salida
    }
    print(f"Reserva realizada con éxito para el asiento {asiento}.")

def mostrar_reservas(reservas):
    if not reservas:
        print("No hay reservas realizadas.")
    else:
        print("\nReservas actuales:")
        for asiento, datos in reservas.items():
            print(f"Asiento {asiento}:")
            print(f"  Nombre: {datos['nombre']}")
            print(f"  RUT: {datos['rut']}")
            print(f"  Destino: {datos['destino']}")
            print(f"  Hora de salida: {datos['hora_salida']}")

def menu():
    asientos = [False] * 120
    reservas = {}

    while True:
        print("\n=== Menú Reservas de Asientos Bus ===")
        print("1) Mostrar Asientos")
        print("2) Reservar Asiento")
        print("3) Mostrar Reservas")
        print("4) Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                mostrar_asientos(asientos)
            elif opcion == 2:
                reservar_asiento(asientos, reservas)
            elif opcion == 3:
                mostrar_reservas(reservas)
            elif opcion == 4:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except:
            print("Entrada inválida. Ingrese un número correspondiente a las opciones.")

if __name__ == "__main__":
    menu()
