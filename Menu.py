import os, time
os.system("cls")

nombre = ""
direc = ""
userAdmin = "admin"
passwrdAdmin = "1234"

banMenu1 = True
while banMenu1:
    print("\nBienvenido a Hotel Paradise Dreams")
    print("\nSistema de gestión de Huéspedes", "="*4)
    print("\n1) Registrar Huéspedes")
    print("2) Consultar Datos de Huéspedes")
    print("3) Salir")
    try:
        opc1 = int(input("\nIngrese una opción del menú: "))
        if opc1 == 1:
            nombre = input("\nIngrese su Nombre: ")
            while nombre == "" or " ":
                print("\nEl campo Nombre es obligatorio...")
            direc = input("\nIngrese su Dirección: ")
            while direc == "" or " ":
                print("\nEl campo Dirección es obligatorio...")

            try:
                banReser = True
                while banReser:
                    num_res = int(input("\Ingrese su número de Reservación: "))
                    if 1000 <= num_res <=10000:
                        print("\nNúmero de Reserva ingresado exitosamente")
                        banReser = False
                    else:
                        os.system("cls")
                        print("\nNúmero de reserva no existe. Vuelva a intentarlo...")
            except:
                print("\nNúmero de reserva no válido...")

            try:
                banEdad = True
                while banEdad:
                    edad = int(input("\nIngrese su edad (sólo con números): "))
                    if 18 <= edad <= 120:
                        print("\nEdad ingresada correctamente")
                        banEdad = False
                    else:
                        print("\n")
                        print("Edad ingresada no válida. Intente nuevamente...")
            except:
                print("\No cumple el requisito de edad...")

            correo = input("\nIngrese su e-mail: ")
            while "@" not in correo:
                print("\nIngrese un e-mail que contenga un @ ")

            try:
                banAcom = True
                while banAcom:
                    acomp = int(input("\nIngrese el número de acompañantes: "))
                    if 0 >= acomp:
                        print("\nNúmero de acompañantes ingresado correctamente")
                        banAcom = False
                    else:
                        os.system("cls")
                        print("\nFavor ingrese un caracter con formato de número...")
            except:
                print("Favor, ingrese un número entero válido")
        elif opc1 == 2:
            user = input("\nIngrese usuario de Administrador: ")
            password = input("\nIngrese password de Administrador: ")
            if user == userAdmin and password == passwrdAdmin:
                

        







        else:
            pass
        elif opc1 == 2:
    
    except:
        os.system("cls")
        print("\nHa ingresado una opción inválida. Intente nuevamente...")
    break