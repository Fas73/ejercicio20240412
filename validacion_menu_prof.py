import time, os
banderaMenu = True
usu1= None 
usu2=None 
usu3=None
con1= None 
con2=None 
con3= None

while banderaMenu:
    print("1. Iniciar Sesion")
    print("2. Registrar Usuario")
    print("3. Salir")
    opcion = int(input("ingrese opcion\n"))
    if opcion ==1 :
        print("1. Iniciar Sesion")
        if (usu1 is None and con1 is None) and (usu2 is None and con2 is None)and (usu3 is None and con3 is None):
            print("No existen usuarios para acceder.")
            time.sleep(2)
            continue

        else:
            username = input("Ingrese su nombre de usuario: \n")
            password = input("Ingrese su contraseña: \n")
            #por aca debo comparar lo que se ingrese en username y los usu
            #mismo caso para password y con 
    elif opcion == 2:
        print("2. Registrar Usuario")
        usu1 = input("ingrese usuario\n")
        con1 = input("ingrese clave")
        opc = int(input("desea agregar mas usuarios?  1.si  2.no\n"))
        if opc == 1:
            usu2 = input("ingrese usuario\n")
            con2 = input("ingrese clave")
            opc = int(input("desea agregar mas usuarios?  1.si  2.no\n"))
            if opc == 1:
                usu3 = input("ingrese usuario\n")
                con3 = input("ingrese clave")
                print(f"usuario: {usu1}")
                print(f"clave: ******")
                print(f"usuario: {usu2}")
                print(f"clave: ******")
                print(f"usuario: {usu3}")
                print(f"clave: ******")
            else:
                print(f"usuario: {usu1}")
                print(f"clave: ******")
                print(f"usuario: {usu2}")
                print(f"clave: ******")
        else:
            print(f"usuario: {usu1}")
            print(f"clave: ******")
    elif opcion == 3:
        print("3. Salir")
        banderaMenu = False
    else:
        print("opcion  no valida")