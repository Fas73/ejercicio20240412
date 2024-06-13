import os
import time

pacientes = []
banMenu1 = True

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

while banMenu1:
    limpiar_pantalla()
    print("\n==== Centro Médico ====\n\n*** Menú Principal: ***")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")
    try:
        opc1 = int(input("\nIngrese una opción (1-4): "))
        if opc1 == 1:
            limpiar_pantalla()
            print("\nREGISTRO DE PACIENTE")
            banderaPaciente = True
            
            while banderaPaciente:
                banderaRut = True
                banderaEdad = True
                while banderaRut:
                    try:
                        rut = int(input("\nIngrese su RUT sin puntos ni guion: "))
                        while rut <= 5000000 or rut >= 99999999:
                            rut = int(input("\nIngrese su RUT dentro del rango de 5000000 y 99999999: "))
                        banderaRut = False
                    except:
                        print("\nFavor, ingrese RUT con números, sin punto ni guión...")

                nombre = input("\nIngrese su nombre: ").capitalize()
                while nombre.strip() == "":
                    nombre = input("\nIngrese un nombre válido: ").capitalize()

                direccion = input("\nIngrese su dirección: ").capitalize()
                while direccion.strip() == "":
                    direccion = input("\nIngrese una dirección válida: ").capitalize()
                
                while banderaEdad:
                    try:
                        edad = int(input("\nIngrese edad: "))
                        while edad <= 0 or edad > 110:
                            edad = int(input("Su rango de edad debe estar entre 0 y 110: "))
                        banderaEdad = False
                    except:
                        print("El campo edad no recibe texto ni símbolos...")

                banderaSexo = True
                while banderaSexo:
                    sexo = input("\nIngrese su sexo: Masculino o Femenino (M/F): ").upper()
                    if sexo == 'M' or sexo == 'F':
                        banderaSexo = False
                    else:
                        print("Ingrese su sexo, sólo con las letras 'M' o 'F'...")

                banderaPs = True        
                while banderaPs:
                    ps = input("\nIngrese su Previsión de Salud (PS) Fonasa o Isapre: ").capitalize()
                    if ps == "Fonasa" or ps == "Isapre":
                        banderaPs = False
                    else:
                        print("Ingrese su PS, indicando si es Isapre o Fonasa...")

                banderaMail = True
                while banderaMail:
                    mail = input("\nIngrese su e-mail: ")
                    if "@" in mail:
                        print("\nDatos ingresados exitosamente!\n")
                        time.sleep(3)
                        banderaMail = False
                    else:
                        print("Su e-mail debe incluir un @. Vuelva a ingresarlo... \n")

                paciente = [rut, nombre, direccion, mail, edad, sexo, ps]
                pacientes.append(paciente)
                agregarPaciente = input("Deseas agregar otro paciente? S o N: ").lower()
                if agregarPaciente == "s":
                    continue
                else:
                    banderaPaciente = False
                print(pacientes)
                input("Enter para continuar...")
        elif opc1 == 2:
            limpiar_pantalla()
            print("\nATENCION PACIENTE")
            while True:
                try:
                    rutPaciente = int(input("Ingrese RUT de Paciente: "))
                    break
                except:
                    print("Por favor, ingrese un número válido para el RUT.")

            paciente_encontrado = False
            for paciente in pacientes:
                if paciente[0] == rutPaciente:
                    paciente_encontrado = True
                    print("Hola, ", paciente[1])
                    registro = input("Motivo de la consulta: ").capitalize()
                    while registro.strip() == "":
                        registro = input("Motivo de la consulta: ").capitalize()
                    paciente.append(registro)
                    break
            if not paciente_encontrado:
                print("Paciente no encontrado!")
            input("Presione enter para continuar...")

        elif opc1 == 3:
            banderaSubMenu = True
            while banderaSubMenu:
                limpiar_pantalla()
                print("=== Menú Gestión de Pacientes ===")
                print("1) Consultar datos del Paciente")
                print("2) Modificar datos del Paciente")
                print("3) Eliminar datos del Paciente")
                print("4) Regresar al Menú Principal")
                try:
                    opcion2 = int(input("\nIngrese opción: \n"))
                    if opcion2 == 1:
                        limpiar_pantalla()
                        print("*** Consultar datos Paciente ***")
                        while True:
                            try:
                                rut_consultar = int(input("Ingrese RUT del paciente:\n"))
                                break
                            except:
                                print("Vuelva a intentar ingresando un RUT válido del paciente...")
                        paciente_encontrado = None
                        for paciente in pacientes:
                            if paciente[0] == rut_consultar:
                                paciente_encontrado = paciente
                                break
                        if paciente_encontrado:
                            print("\n*** Paciente encontrado: ***")
                            print("Rut      : ", paciente_encontrado[0])
                            print("Nombre   : ", paciente_encontrado[1])
                            print("Direccion: ", paciente_encontrado[2])
                            print("Correo   : ", paciente_encontrado[3])
                            print("Edad     : ", paciente_encontrado[4])
                            print("Sexo     : ", paciente_encontrado[5])
                            print("Prevision: ", paciente_encontrado[6])
                            if len(paciente_encontrado) > 7:
                                print("Registro : ", paciente_encontrado[7])
                        else:
                            print("Según los registros, el RUT no existe en nuestra BBDD")    
                        input("Enter para continuar...")

                    elif opcion2 == 2:
                        limpiar_pantalla()
                        print("*** Modificar Paciente ***")
                        while True:
                            try:
                                rut_editar = int(input("Ingrese RUT del paciente:\n"))
                                break
                            except:
                                print("Por favor, ingrese un RUT válido...")
                        paciente_editado = None
                        for paciente in pacientes:
                            if paciente[0] == rut_editar:
                                paciente_editado = paciente
                                break
                        if paciente_editado:
                            campo = input("Ingrese el campo que desea editar: (nombre, direccion, correo, edad, sexo, prevision)").lower()
                            if campo in ['nombre', 'direccion', 'correo', 'edad', 'sexo', 'prevision']:
                                nuevo_valor = input(f"Ingrese valor para el campo {campo}: ")
                                if campo == 'edad':
                                    nuevo_valor = int(nuevo_valor)
                                campo_indices = {'nombre': 1, 'direccion': 2, 'correo': 3, 'edad': 4, 'sexo': 5, 'prevision': 6}
                                paciente_editado[campo_indices[campo]] = nuevo_valor
                                print("Campo actualizado con éxito.")
                        else:
                            print("El paciente no fue encontrado.")
                        input("Presione enter para continuar...")

                    elif opcion2 == 3:
                        limpiar_pantalla()
                        print("*** Eliminar Paciente ***")
                        while True:
                            try:
                                rut_eliminar = int(input("Ingrese RUT del paciente:\n"))
                                break
                            except:
                                print("Por favor, ingrese un RUT válido...")
                        paciente_encontrado = False
                        for paciente in pacientes:
                            if paciente[0] == rut_eliminar:
                                paciente_encontrado = True
                                try:
                                    pacientes.remove(paciente)
                                    print("Paciente eliminado con éxito!")
                                    time.sleep(1)
                                except:
                                    print("Error al intentar eliminar el paciente...")
                                break
                        if not paciente_encontrado:
                            print("Según los registros, no existe el RUT...")
                        input("Presione enter para continuar...")
                    elif opcion2 == 4:
                        print("Regresando al Menú Principal...")
                        time.sleep(1)
                        banderaSubMenu = False
                except:
                    print("Opción ingresada no es válida...")
                    input("Presione enter para continuar...")

        elif opc1 == 4:
            limpiar_pantalla()
            print("\nHa salido del sistema...\n")
            banMenu1 = False

    except:
        print("Opción ingresada no existe. Vuelva a intentar con Opción 1 al 4...")
        input("Presione enter para continuar...")
