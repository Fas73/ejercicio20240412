import time, os
os.system("cls")

#user_admin = "admin"
#passw_admin = "1234"

banMenu1 = True
while banMenu1:
    #os.system("cls")
    print("\n===Centro Médico DUOC===")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    try:
        opc1 = int(input("\nIngrese una opción (1-4): "))
        if opc1 == 1:
            os.system("cls")
            print("\nREGISTRO DE PACIENTE")
            banderaRut = True
            while banderaRut:
                try:
                    rut = int(input("\nIngrese su RUT sin puntos ni guión: "))
                    #while rut < 5000000 or rut > 99999999:
                    while rut <= 5000000 or rut >= 99999999:
                        rut = int(input("\nIngrese su rut, dentro del rango de 5000000 y 99999999 \n"))
                    banderaRut = False
                except:
                    print("\nFavor, ingrese RUT con números, sin punto ni guión...")

            nombre = input("\nIngrese su nombre: ")
            while nombre == "" or nombre == " ":
                nombre = input("\nIngrese un nombre válido: ")
                
            direc = input("\nIngrese su dirección: ")
            while direc == "" or direc == " ":
                direc = input("\nIngrese una dirección válida: ")

            banderaEdad = True
            while banderaEdad:
                try:
                    edad = int(input("\nIngrese edad: "))
                    #while edad < 0 or edad > 110:
                    while edad <= 0 or edad > 110:
                        edad =int(input("Su rango edad debe estar entre 0 y 110: "))
                    banderaEdad = False
                except:
                    print("El campo edad no recibe texto ni símbolos...")

            banderaSexo = True
            while banderaSexo:
                try:
                    #while sexo != 'm' and sexo != 'M' and sexo != 'f' and sexo != 'F':
                    sexo = input("\nIngrese su sexo: Masculino o Femenino (M/F): ").upper()
                    while "F" not in sexo and "M" not in sexo:
                        sexo = input("Ingrese su sexo, sólo con las letras 'M' o 'F': ").upper()
                    banderaSexo = False
                except:
                    print("El caracter ingresado es incorrecto. Intente 'M' o 'F'...")

            banderaPs = True        
            while banderaPs:
                try:
                    ps = input("\nIngrese su Previsión de Salud (PS) Fonasa o Isapre: ").upper()
                    #while ps != "fonasa" and ps != "isapre":
                    while "FONASA" not in ps and "ISAPRE" not in ps:
                        ps = input("Ingrese su PS, indicando si es Isapre o Fonasa: ").upper()
                    banderaPs = False
                except:
                    print("La Previsión de Salud indicada es incorrecta. Intente nuevamente...")

            banderaMail = True
            while banderaMail:
                    try:
                        mail = input("\nIngrese su e-mail: ")
                        while "@" not in mail:
                            mail = input("Su e-mail debe incluir un @. Vuelva a ingresarlo... \n")
                        print("\nDatos ingresados exitosamente!\n")
                        time.sleep(3)
                        banderaMail = False
                    except:
                        print("e-mail no válido. Debe contener al menos un caracter de @")
                        
        elif opc1 == 2:
            os.system("cls")
            print("\nATENCION PACIENTE")
            banderaPaciente = True
            while banderaPaciente:
                try:
                    user = int(input("\nIngrese el RUT del paciente: "))
                    if user == rut:
                        print("\nEl RUT del paciente ha sido confirmado\n")
                        fecha = input("\nIngrese fecha: ")
                        obser = input("\nIngrese obervaciones de su visita: ")
                        banderaPaciente = False

                except:
                    os.system("cls")
                    print("\nRUT no válido, intente nuevamente.")

        elif opc1 == 3:
            os.system("cls")
            print("\nCONSULTAR DATOS PACIENTE")
            banderaConsulta = True
            while banderaConsulta:
                try:
                    user = int(input("\nIngrese el RUT del paciente: "))
                    if user == rut:
                        print("\n====DATOS DEL PACIENTE====")
                        print(f"RUT\t\t: {rut}")
                        print(f"Nombre\t\t: {nombre}")
                        print(f"Dirección\t: {direc}")
                        print(f"E-mail\t\t: {mail}")
                        print(f"Edad\t\t: {edad}")
                        print(f"Sexo\t\t: {sexo}")
                        print(f"Registros\t: {obser}")
                        print(f"Previsión\t: {ps}")
                        x = input("\nPresione enter para continuar...")
                        banderaConsulta = False
                        
                except:
                    os.system("cls")
                    print("\nRUT no válido, intente nuevamente.")

        elif opc1 == 4:
            os.system("cls")
            print("\nHa salido del sistema...\n")
            banMenu1 = False
            
    except:
        print("Opción ingresa no existe. Vuelva a intentar con Opción 1 al 4...")

#            elif opc1 == 5:
#            user = input("\nIngrese usuario de admin: ")
#            password = input("Ingrese contraseña de admin: ")
#            if user == user_admin and password == passw_admin:
#                os.system("cls")
#                print("\n¡Credenciales confirmadas!")
#                if acomp > 3:
#                    print("\n---Datos de Huesped---")
#                    print(f"Nombre: {nombre}")
#                    print("*** Huesped con demasiados acompañantes ***")
#                    time.sleep(3)
#                else:
#                    print("\n---Datos de Huesped---")
#                    print(f"Nombre: {nombre}")
#                    print("*** Huesped dentro del límite de acompañantes ***")
#                    time.sleep(3)
#            else:
#                os.system("cls")
#                print("\nCredenciales no válidas, intente nuevamente.")
