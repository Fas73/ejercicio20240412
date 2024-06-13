import os, time
os.system("cls")

nombre = ""
direc = ""
user_Admin = "admin"
passwd_Admin = "1234"

banMenu1 = True
while banMenu1:
    print("\nBienvenido a Hotel Paradise Dreams")
    print("\nSistema de gestión de Huéspedes")
    print("\n1) Registrar Huéspedes")
    print("2) Consultar Datos de Huéspedes")
    print("3) Salir")
    try:
        opc1 = int(input("Ingrese una Opción: "))
        if opc1 == 1:
            nombre = input("\nIngrese su nombre: ")
            while nombre == "" or nombre == " ":
                nombre = input("\nFavor, Ingrese un nombre: ")
                
            direc = input("\nIngrese su dirección: ")
            while direc == "" or direc == " ":
                direc = input("\nFavor, ingrese una dirección: ")

            try:
                ban_Reser = True
                while ban_Reser:
                    num_res = int(input("\nIngrese su Nro de Reserva: "))
                    if 1000 <= num_res <= 10000:
                        print("\nNúmero de reserva registrado exitosamente")
                        ban_Reser = False
                    else:
                        os.system("cls")
                        print("El número de reserva no existe... Vuelva a intentar")
            except:
                print("Número de reserva no válido...")
                
            try:
                ban_Edad = True
                while ban_Edad:
                    edad = int(input("\nIngrese su edad (sólo con números): "))
                    if 18 <= edad <= 120:
                        print("\nEdad ingresada exitosamente")
                        ban_Edad = False
                    else:
                        os.system("cls")
                        print("\nEdad no válida, intente nuevamente...")
            except:
                print("\nEdad ingresada no es válida...")
                
            correo = input("\nIngrese su e-mail: ")
            while "@" not in correo:
                correo = input("Ingrese un e-mail válido...\n")
                
            try:
                ban_Acomp = True
                while ban_Acomp:
                    acomp = int(input("\nIngrese número de acompañantes: "))
                    if acomp >= 0:
                        print("Número de acompañantes ingresado exitosamente.")
                        ban_Acomp = False
                    else:
                        os.system("cls")
                        print("Favor, ingrese un caracter con formato de número válido...")
            except:
                print("Favor, ingrese un número entero válido")
        elif opc1 == 2:
            user = input("\nIngrese usuario de admin: ")
            password = input("Ingrese contraseña de admin: ")
            if user == user_Admin and password == passwd_Admin:
                os.system("cls")
                print("Datos confirmados")
                print("\n")
                print("\nDATOS DEL HUÉSPED")
                print(f"Nombre\t\t\t: {nombre}")
                print(f"Dirección\t\t: {direc}")
                print(f"Nro. reserva\t\t: {num_res}")
                print(f"Edad\t\t\t: {edad}")
                print(f"e-mail\t\t\t: {correo}")
                print(f"Nro. acompañantes\t: {acomp}")

                if acomp > 3:
                    print("*** Huésped con demasiados acompañantes ***")
                    input("\nPresione Enter para continuar...")
                    os.system("cls")

                else:
                    print("*** Huésped dentro del límite de acompañantes ***")
                    input("\nPresione Enter para continuar...")
                    os.system("cls")
            else:
                os.system("cls")
                print("\nCredenciales no válidas, intente nuevamente.")
                
        elif opc1 == 3:
            os.system("cls")
            print("\nGracias por visitar Hotel Paradise Dreams\n")
            banMenu1 = False
        
        else:
            os.system("cls")
            print("\nHa ingresado una opción no válida, intente nuevamente...")
                
    except:
        os.system("cls")
        print("\nHa ingresado una opción inválida. Vuelva a intentarlo...")

