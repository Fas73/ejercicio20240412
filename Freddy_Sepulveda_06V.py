import time, os
os.system("cls")
usu = "assault"
passwr = "assault"
banMenu1 = True
while banMenu1:
    print('\nSistema de Gestión de Jugadores - "Epic Quest"')
    print("1) Registrar Jugador")
    print("2) Consultar Datos de Jugador")
    print("3) Salir")
    try:
        opc1 =int(input("\nIngrese una opción (1-3): "))
        if opc1 == 1:
            os.system("cls")
            print("\n===Registrar Jugador===")
            nombre = input("\nIngrese nombre de usuario: ")
            while nombre == "" or nombre == " ":
                nombre = input("\nIngrese un nombre válido: ")
            banderaId = True
            while banderaId:
                try:
                    usuId = int(input("\nIngrese ID de Jugador: "))
                    while usuId < 10000 or usuId > 99999:
                        usuId = int(input("\nIngrese ID de Jugador, con un número dentro del rango de 10000 y 99999: "))
                    banderaId = False
                except:
                    print("\nVuelva a intentar, ingresando un número dentro del rango de 10000 a 99999...")
            banderaNivel = True
            while banderaNivel:
                try:
                    nivel = int(input("\nIngrese Nivel de Jugador: "))
                    while nivel < 1 or nivel > 100:
                        nivel = int(input("\nIngrese Nivel de Jugador, con un número dentro del rango de 1 al 100: "))
                    banderaNivel = False
                except:
                    print("\nVuelva a intentar, ingresando un número dentro del rango de 1 a 100...")
            banderaMail = True
            while banderaMail:
                try:
                    mail = input("\nIngrese su e-mail: ")
                    while "@" not in mail:
                        mail = input("Su e-mail debe incluir un @. Vuelva a ingresarlo: \n")
                    banderaMail = False
                except:
                    print("e-mail no válido. Debe contener al menos un caracter de @...")
            banderaRol = True
            while banderaRol:
                try:
                    rol = input('\nIngrese su rol de juego: "objective", "slayer", "support" o "anchor": ')
                    while rol != "objective" and rol != "slayer" and rol != "support" and rol != "anchor":
                        rol = input('\nIngrese su rol de juego. Elija "objective", "slayer", "support" o "anchor": ')
                    banderaRol = False
                except:
                    print('Debe elegir su rol entre: "objective", "slayer", "support" o "anchor" ')
                    print("Vuelva a intetarlo...")
            banderaExpe = True
            while banderaExpe:
                try:
                    ptsExpe = int(input("\nIngrese Puntos de Experiencia acumulados: "))
                    while ptsExpe <= 0:
                        ptsExpe = int(input("\nIngrese Puntos de Experiencia acumulados: con un número mayor o igual a cero: "))
                    banderaExpe = False
                except:
                    print("\nVuelva a intentar, ingresando un número entero mayor o igual a cero...")
        elif opc1 == 2:
            os.system("cls")
            print("\n===Consultar Datos de Jugador===")
            banderaConsulta = True
            while banderaConsulta:
                try:
                    consultaId = int(input("\nIngrese la ID del jugador: "))
                    usuAdm = input("\nIngrese usuario de Admin ")
                    usuPass = input("\nIngrese password de Admin: ")
                    if consultaId == usuId and usuAdm == usu and usuPass == passwr:
                        print("\nCredenciales confirmadas\n")
                        print("\n====DATOS DEL JUGADOR====")
                        print(f"Nombre de usuario\t: {nombre}")
                        print(f"ID de Jugador\t\t: {usuId}")
                        print(f"Nivel de jugador\t: {nivel}")
                        print(f"e-mail\t\t\t: {mail}")
                        print(f"Rol de jugador\t: {rol}")
                        print(f"Ptos de exp. acumulados: {ptsExpe}")
                        
                        if nivel > 50 and ptsExpe > 999: 
                            print("Jugador Experimentado") 
                        else: 
                            print("Jugador Novato") 
                        banderaConsulta = False
                except:
                    os.system("cls")
                    print("\nDatos no válidos. Intente nuevamente...")
        elif opc1 == 3:
            os.system("cls")
            print("\nHa salido del sistema...")
            banMenu1 = False
                    
    except:
        print("\nOpción ingresada no existe. Intente ingresado un número del 1 al 3")
