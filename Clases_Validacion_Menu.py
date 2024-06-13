
usu1= None 
usu2= None 
usu3= None
con1= None 
con2= None 
con3= None

banderaMenu = True
while banderaMenu:
    print("1. Iniciar Sesión")
    print("2. Registrar Usuario")
    print("3. Salir")
    opcion = int(input("Ingrese opción\n"))
    if opcion ==1:
        print("1. Iniciar Sesión")
        if (usu1== None and con1 == None) and (usu2== None and con2 == None) and (usu3== None and con3 == None):
            print("No existe usuario")
            continue
        
        else:
         username = input("Ingrese su nombre de usuario: \n")
         password = input("Ingrese su contraseña: \n")
        # por acá debo comparar lo que se ingresa en username y los usu
        # mismo caso para password con
        
        print("")
    elif opcion == 2:
        print("2. Registrar Usuario: ")
        usu1 = input("Ingrese Usuario: \n")
        con1 = input ("Ingrese Contraseña: ")
        opc = int(input("Desea agregar más Usuarios?: 1.Si 2.No\n"))
        if opc == 1:
            usu2 = input("Ingrese Usuario: \n")
            con2 = input ("Ingrese Contraseña: ")
            opc = int(input("Desea agregar más Usuarios?: 1.Si 2.No\n"))
            if opc == 1:
                usu3 = input("Ingrese Usuario: \n")
                con3 = input ("Ingrese Contraseña: ")
                print(f"Usuario: {usu1}")
                print(f"Contraseña: ******")
                print(f"Usuario: {usu2}")
                print(f"Contraseña: ******")
                print(f"Usuario: {usu3}")
                print(f"Contraseña: ******")
            else:
                print(f"Usuario: {usu1}")
                print(f"Contraseña: ******")
                print(f"Usuario: {usu2}")
                print(f"Contraseña: ******")
