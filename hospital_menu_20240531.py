import os
import time

# Lista de pacientes
pacientes = []

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("Presiona Enter para continuar...")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: \n"))
            if 5000000 < rut < 99999999:
                return rut
            else:
                print("RUT fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Ingrese un dato válido.")

def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese edad (0 a 110): \n"))
            if 0 <= edad <= 110:
                return edad
            else:
                print("Edad fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Ingrese un dato válido.")

def validar_campo_no_vacio(campo, mensaje):
    while not campo.strip():
        print(mensaje)
        campo = input()
    return campo

def validar_correo():
    while True:
        correo = input("Ingrese correo: \n")
        if "@" in correo:
            return correo
        else:
            print("Ingrese correo válido.")

def validar_sexo():
    while True:
        sexo = input("Ingrese sexo (f o m): \n").lower()
        if sexo in ("f", "m"):
            return sexo
        else:
            print("Ingrese sexo válido (f o m).")

def validar_prevision():
    while True:
        ps = input("Ingrese su prevision de salud (Isapre o Fonasa): \n")
        if ps in ("Isapre", "Fonasa"):
            return ps
        else:
            print("Ingrese su prevision de salud válida (Isapre o Fonasa).")

def registrar_paciente():
    limpiar_pantalla()
    print("-Registrar Paciente-")
    rut = validar_rut()
    nombre = validar_campo_no_vacio(input("Ingrese el nombre: \n"), "Ingrese un nombre no vacío: \n")
    direccion = validar_campo_no_vacio(input("Ingrese direccion: \n"), "Ingrese una dirección no vacía: \n")
    correo = validar_correo()
    edad = validar_edad()
    sexo = validar_sexo()
    ps = validar_prevision()

    paciente = [rut, nombre, direccion, correo, edad, sexo, ps]
    pacientes.append(paciente)
    print("Paciente agregado!")
    pausar()

def atencion_paciente():
    limpiar_pantalla()
    print("-Atencion Paciente-")
    if not pacientes:
        print("No se ha ingresado ningún paciente!")
        pausar()
        return

    rut_ingresado = validar_rut()
    for paciente in pacientes:
        if paciente[0] == rut_ingresado:
            registro = validar_campo_no_vacio(input("Ingrese motivo de consulta: \n"), "Registro no puede estar vacío!")
            paciente.append(registro)
            print("Registro ingresado!")
            pausar()
            return
    print("Paciente no encontrado!")
    pausar()

def gestionar_paciente():
    if not pacientes:
        limpiar_pantalla()
        print("-Gestionar Paciente-")
        print("Ningún paciente ha sido ingresado!")
        pausar()
        return

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
            consultar_datos_paciente()
        elif opcGestionar == 2:
            eliminar_paciente()
        elif opcGestionar == 3:
            modificar_paciente()
        elif opcGestionar == 4:
            break

def consultar_datos_paciente():
    limpiar_pantalla()
    print("-Consultar datos paciente-")
    rut_ingresado = validar_rut()
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
            return
    print("Paciente no registrado!")
    pausar()

def eliminar_paciente():
    limpiar_pantalla()
    print("-Eliminar paciente-")
    rut_ingresado = validar_rut()
    for paciente in pacientes:
        if paciente[0] == rut_ingresado:
            pacientes.remove(paciente)
            print("Paciente eliminado!")
            pausar()
            return
    print("Paciente no encontrado!")
    pausar()

def modificar_paciente():
    limpiar_pantalla()
    print("-Modificar Paciente-")
    rut_ingresado = validar_rut()
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
                    modificar = int(input("Ingrese que campo desea modificar (1/2/3/4/5/6/7): "))
                except ValueError:
                    print("Ingrese tipo de dato válido!")
                    time.sleep(1)
                    continue

                if modificar == 1:
                    paciente[1] = validar_campo_no_vacio(input("Ingrese el nombre: \n"), "Ingrese un nombre no vacío: \n")
                elif modificar == 2:
                    paciente[2] = validar_campo_no_vacio(input("Ingrese direccion: \n"), "Ingrese una dirección no vacía: \n")
                elif modificar == 3:
                    paciente[3] = validar_correo()
                elif modificar == 4:
                    paciente[4] = validar_edad()
                elif modificar == 5:
                    paciente[5] = validar_sexo()
                elif modificar == 6:
                    paciente[6] = validar_prevision()
                elif modificar == 7:
                    break
                print("Campo modificado!")
                pausar()
            return
    print("Paciente no encontrado!")
    pausar()

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
        registrar_paciente()
    elif opcMenu == 2:
        atencion_paciente()
    elif opcMenu == 3:
        gestionar_paciente()
    elif opcMenu == 4:
        print("Ha salido del programa...")
        break
