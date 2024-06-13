import os
import time

# Lista de pacientes
pacientes = []

# Limpia la pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Pausa la ejecución
def pausar():
    input("Presiona Enter para continuar...")

while True:
    limpiar_pantalla()
    print("Hospital.py")
    print("1.- Registrar Paciente")
    print("2.- Atencion Paciente")
    print("3.- Gestionar Paciente")
    print("4.- Salir")
    
    try:
        opcMenu = int(input("Ingrese una opción (1/2/3/4): "))
    except ValueError:
        print("Ingrese tipo de dato válido!")
        time.sleep(1)
        continue

    if opcMenu == 1:
        limpiar_pantalla()
        print("-Registrar Paciente-")
        
        while True:
            try:
                rut = int(input("Ingrese rut: \n"))
                if 5000000 < rut < 99999999:
                    break
                else:
                    print("RUT fuera de rango. Intente de nuevo.")
            except ValueError:
                print("Ingrese un dato válido.")

        nombre = ""
        while not nombre.strip():
            nombre = input("Ingrese el nombre: \n")
            if not nombre.strip():
                print("El nombre no puede estar vacío.")
        
        direccion = ""
        while not direccion.strip():
            direccion = input("Ingrese direccion: \n")
            if not direccion.strip():
                print("La dirección no puede estar vacía.")
        
        while True:
            correo = input("Ingrese correo: \n")
            if "@" in correo:
                break
            else:
                print("Ingrese correo válido.")
        
        while True:
            try:
                edad = int(input("Ingrese edad (0 a 110): \n"))
                if 0 <= edad <= 110:
                    break
                else:
                    print("Edad fuera de rango. Intente de nuevo.")
            except ValueError:
                print("Ingrese un dato válido.")
        
        while True:
            sexo = input("Ingrese sexo (f o m): \n").lower()
            if sexo in ("f", "m"):
                break
            else:
                print("Ingrese sexo válido (f o m).")
        
        while True:
            ps = input("Ingrese su prevision de salud (Isapre o Fonasa): \n")
            if ps in ("Isapre", "Fonasa"):
                break
            else:
                print("Ingrese su prevision de salud válida (Isapre o Fonasa).")
        
        paciente = [rut, nombre, direccion, correo, edad, sexo, ps]
        pacientes.append(paciente)
        print("Paciente agregado!")
        pausar()

    elif opcMenu == 2:
        limpiar_pantalla()
        print("-Atencion Paciente-")
        if not pacientes:
            print("No se ha ingresado ningún paciente!")
            pausar()
            continue

        while True:
            try:
                rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                if 5000000 < rut_ingresado < 99999999:
                    break
                else:
                    print("RUT fuera de rango. Intente de nuevo.")
            except ValueError:
                print("Ingrese un dato válido.")

        for paciente in pacientes:
            if paciente[0] == rut_ingresado:
                while True:
                    registro = input("Ingrese motivo de consulta: \n")
                    if registro.strip():
                        paciente.append(registro)
                        print("Registro ingresado!")
                        break
                    else:
                        print("El registro no puede estar vacío.")
                pausar()
                break
        else:
            print("Paciente no encontrado!")
            pausar()

    elif opcMenu == 3:
        if not pacientes:
            limpiar_pantalla()
            print("-Gestionar Paciente-")
            print("Ningún paciente ha sido ingresado!")
            pausar()
            continue

        while True:
            limpiar_pantalla()
            print("-Gestionar Paciente-")
            print("1.- Consultar datos paciente")
            print("2.- Eliminar paciente")
            print("3.- Modificar paciente")
            print("4.- Regresar al menú principal")
            
            try:
                opcGestionar = int(input("Ingrese una opción (1/2/3/4): "))
            except ValueError:
                print("Ingrese tipo de dato válido!")
                time.sleep(1)
                continue

            if opcGestionar == 1:
                limpiar_pantalla()
                print("-Consultar datos paciente-")
                while True:
                    try:
                        rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                        if 5000000 < rut_ingresado < 99999999:
                            break
                        else:
                            print("RUT fuera de rango. Intente de nuevo.")
                    except ValueError:
                        print("Ingrese un dato válido.")
                
                for paciente in pacientes:
                    if paciente[0] == rut_ingresado:
                        print(f"Rut: {paciente[0]}")
                        print(f"Nombre: {paciente[1]}")
                        print(f"Direccion: {paciente[2]}")
                        print(f"Correo: {paciente[3]}")
                        print(f"Edad: {paciente[4]}")
                        print(f"Sexo: {paciente[5]}")
                        print(f"Prevision: {paciente[6]}")
                        if len(paciente) > 7:
                            print(f"Registro: {paciente[7]}")
                        else:
                            print("Paciente aún no ha sido atendido")
                        pausar()
                        break
                else:
                    print("Paciente no registrado!")
                    pausar()

            elif opcGestionar == 2:
                limpiar_pantalla()
                print("-Eliminar paciente-")
                while True:
                    try:
                        rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                        if 5000000 < rut_ingresado < 99999999:
                            break
                        else:
                            print("RUT fuera de rango. Intente de nuevo.")
                    except ValueError:
                        print("Ingrese un dato válido.")

                for paciente in pacientes:
                    if paciente[0] == rut_ingresado:
                        pacientes.remove(paciente)
                        print("Paciente eliminado!")
                        pausar()
                        break
                else:
                    print("Paciente no encontrado!")
                    pausar()

            elif opcGestionar == 3:
                limpiar_pantalla()
                print("-Modificar Paciente-")
                while True:
                    try:
                        rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                        if 5000000 < rut_ingresado < 99999999:
                            break
                        else:
                            print("RUT fuera de rango. Intente de nuevo.")
                    except ValueError:
                        print("Ingrese un dato válido.")
                
                for paciente in pacientes:
                    if paciente[0] == rut_ingresado:
                        while True:
                            print("1.- Nombre ")
                            print("2.- Direccion ")
                            print("3.- Correo")
                            print("4.- Edad")
                            print("5.- Sexo")
                            print("6.- Prevision")
                            print("7.- Salir")
                            try:
                                modificar = int(input("Ingrese qué campo desea modificar (1/2/3/4/5/6/7): "))
                            except ValueError:
                                print("Ingrese tipo de dato válido!")
                                time.sleep(1)
                                continue

                            if modificar == 1:
                                while True:
                                    nombre = input("Ingrese el nombre: \n")
                                    if nombre.strip():
                                        paciente[1] = nombre
                                        break
                                    else:
                                        print("El nombre no puede estar vacío.")
                            elif modificar == 2:
                                while True:
                                    direccion = input("Ingrese direccion: \n")
                                    if direccion.strip():
                                        paciente[2] = direccion
                                        break
                                    else:
                                        print("La dirección no puede estar vacía.")
                            elif modificar == 3:
                                while True:
                                    correo = input("Ingrese correo: \n")
                                    if "@" in correo:
                                        paciente[3] = correo
                                        break
                                    else:
                                        print("Ingrese correo válido.")
                            elif modificar == 4:
                                while True:
                                    try:
                                        edad = int(input("Ingrese edad (0 a 110): \n"))
                                        if 0 <= edad <= 110:
                                            paciente[4] = edad
                                            break
                                        else:
                                            print("Edad fuera de rango. Intente de nuevo.")
                                    except ValueError:
                                        print("Ingrese un dato válido.")
                            elif modificar == 5:
                                while True:
                                    sexo = input("Ingrese sexo (f o m): \n").lower()
                                    if sexo in ("f", "m"):
                                        paciente[5] = sexo
                                        break
                                    else:
                                        print("Ingrese sexo válido (f o m).")
                            elif modificar == 6:
                                while True:
                                    ps = input("Ingrese su prevision de salud (Isapre o Fonasa): \n")
                                    if ps in ("Isapre", "Fonasa"):
                                        paciente[6] = ps
                                        break
                                    else:
                                        print("Ingrese su prevision de salud válida (Isapre o Fonasa).")
                            elif modificar == 7:
                                break
                            print("Campo modificado!")
                            pausar()
                        break
                else:
                    print("Paciente no encontrado!")
                    pausar()

            elif opcGestionar == 4:
                break

    elif opcMenu == 4:
        print("Ha salido del programa...")
        break
