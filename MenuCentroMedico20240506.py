import time, os
os.system("cls")


banMenu1 = True
while banMenu1:
    print("\n===Centro Médico DUOC===")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    try:
        opc1 = int(input("\nIngrese una opción: "))
        if opc1 == 1:
            print("\nREGISTRO DE PACIENTE")
            rut = int(input("\nIngrese su RUT sin puntos ni guión: "))
            banderaRut = True
            while rut <= 5000000 or rut >= 99999999:
                rut = int(input("\nIngrese su rut, dentro del rango de 5000000 y 99999999 \n"))

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
                    while edad <= 0 or edad > 110:
                        edad =int(input("Su rango edad debe estar entre 0 y 110: "))
                    banderaEdad = False
                except:
                    print("El campo edad no recibe texto ni símbolos...")

            banderaSexo = True
            while banderaSexo:
                try:
                    sexo = input("\nIngrese sexo (F/M): ").upper()
                    while "F" not in sexo and "M" not in sexo:
                        sexo = input("Ingrese sexo, con las letras 'M' o 'F': ").upper()
                    banderaSexo = False
                except:
                    print("El caracter ingresado es incorrecto. Intente 'M' o 'F'...")

            banderaPs = True        
            while banderaPs:
                try:
                    ps = input("\nIngrese su Previsión de Salud (PS) Fonasa o Isapre: ").upper()
                    while "FONASA" not in ps and "ISAPRE" not in ps:
                        ps = input("Ingrese su PS, indicando si es Isapre o Fonasa: \n")
                    banderaPs = False
                except:
                    print("La Previsión de Salud indicada es incorrecta. Intente nuevamente...")

            banderaMail = True
            while banderaMail:
                    try:
                        mail = input("Ingrese su e-mail: \n")
                        while "@" not in mail:
                            mail = input("Su e-mail debe incluir un @. Vuelva a intentarlo... \n")
                        banderaMail = False
                    except:
                        print("e-mail incorrecto. Debe contener al menos un caracter de @")
                        
        elif opc1 == 2:
            print("\nATENCION PACIENTE")
            user = int(input("\nIngrese el RUT del paciente: "))
            if user == rut:
                os.system("cls")
                print("\nEl RUT del paciente ha sido confirmado")
            else:
                os.system("cls")
                print("\nRUT no válido, intente nuevamente.")
            fecha = int(input("Ingrese fecha: "))
            obser = input("Ingrese obervaciones de su visita: ")

        elif opc1 == 3:
            print("\nCONSULTAR DATOS PACIENTE")
            user = int(input("\nIngrese el RUT del paciente: "))
            if user == rut:
                os.system("cls")
                print("\nEl RUT del paciente ha sido confirmado")
            else:
                os.system("cls")
                print("\nRUT no válido, intente nuevamente.")
            print("\n====DATOS DEL PACIENTE====")
            print(f"RUT: {rut}")
            print(f"Nombre: {nombre}")
            print(f"Dirección: {direc}")
            print(f"E-mail: {mail}")
            print(f"Edad: {edad}")
            print(f"Sexo: {sexo}")
            print(f"Registros: {obser}")
            print(f"Previsión: {ps}")
            time.sleep(3)

        elif opc1 == 4:
            os.system("cls")
            print("\nHa salido del sistema...")
            banMenu1 = False
            
    except:
        print("Opción ingresa no existe...")
    