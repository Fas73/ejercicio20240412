import time, os
user = "admin"
password = "123"
while True:
    os.system("cls")
    print("\n")
    print("Bienvenido al Hotel Paradise Dreams")
    print("\n")
    print("Sistema de Gestión de Huéspedes")
    print("\n")
    print("1. Registrar Huésped")
    print("2. Consultar Datos de Huésped")
    print("3. Salir")
    try:
        opcion = int(input("Ingrese una opción\n"))
        if opcion == 1:
            os.system("cls")
            print("REGISTRO DE HUÉSPEDES")
            nombre = input("Registre su nombre\n")
            while nombre == "":
                nombre = input("No ha ingresado un nombre\n")
            direccion = input("Ingrese su direccion\n")
            while direccion == "":
                direccion = input("No ha ingresado una dirección\n")
            reserva = int(input("Ingrese su Nro de Reserva\n"))
            while reserva <= 999 or reserva >= 9999:
                reserva = int(input("Ingrese su Nro de Reserva, mayor a 999 y menor a 10000 \n"))
            edad = int(input("Ingrese su edad\n"))
            while edad < 18 or edad >120:
                edad = int(input("Ingrese edad\n"))
            correo = input("Ingrese su e-mail\n")
            while '@' not in correo:
                correo = input("Ingrese un e-mail válido\n")
            acompanantes = int(input("Ingrese Nro. de acompañantes\n"))
            while acompanantes <= 0 or acompanantes >4:
                acompanantes = input("Huésped con demasiados acompañantes\n")
            
        elif opcion == 2:
            os.system("cls")
            print("CONSULTA DATOS HUÉSPEDES")
            username = input("Ingrese usuario\n")
            psswrd = input("Ingrese password\n")
            if(user == username and password == psswrd):
                res_huesped = int(input("Ingrese Nro reserva del huésped a buscar\n"))
                if res_huesped == reserva:
                    print(f"Nombre\t: {nombre}")
                    print("Direccion\t: ", direccion)
                    print(f"Edad\t: {edad}")
                    print("Correo\t: ", correo)
                    print(f"Nro. Acompañantes\t: {acompanantes}")
                    if acompanantes <= 4:
                        print("Huésped dentro de límite de acompañantes")
                    else:
                        print("Huésped con demasiados acompañantes")
                else:
                    print("El Nro de Reserva ingresado no existe")
                    time.sleep(3)
                print("Pulse tecla para continuar...")
                #x = input()
        elif opcion == 3:
            os.system("cls")
            print("SALIR")
            break
            
    except:
        print("Opción no existe")
print("Ha salido del sistema de reservas")