import time, os

banderaMenu = True
usu1 = None 
usu2 = None 
usu3 = None 
con1 = None 
con2 = None 
con3 = None

def validar_celular(numero):
    if len(numero) != 9:
        return False
    if numero[0] != '9':
        return False
    return numero.isdigit()

def validar_correo(correo):
    return '@' in correo

while banderaMenu:
    print("1. Iniciar Sesion")
    print("2. Registrar Usuario")
    print("3. Salir")
    
    opcion = int(input("Ingrese opción: "))
    
    if opcion == 1:
        print("1. Iniciar Sesion")
        
        if (usu1 is None or con1 is None) and (usu2 is None or con2 is None) and (usu3 is None or con3 is None):
            print("No existen usuarios para acceder.")
            time.sleep(2)
            continue
        
        else:
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            
            if (username == usu1 and password == con1) or \
               (username == usu2 and password == con2) or \
               (username == usu3 and password == con3):
                
                while True:
                    print("\nMenú principal:")
                    print("1) Realizar llamada")
                    print("2) Enviar correo electrónico")
                    print("3) Cerrar sesión")
                    
                    opcion_menu = input("Seleccione una opción: ")
                    
                    if opcion_menu == '1':
                        celular = input("Ingrese el número de celular: ")
                        if validar_celular(celular):
                            print(f"Llamando al número {celular}...")
                        else:
                            print("Número de celular inválido.")
                    
                    elif opcion_menu == '2':
                        correo = input("Ingrese el correo electrónico: ")
                        while not validar_correo(correo):
                            print("Correo electrónico inválido.")
                            correo = input("Ingrese el correo electrónico: ")
                        
                        mensaje = input("Ingrese el mensaje a enviar: ")
                        print(f"Enviando correo a {correo} con el mensaje: {mensaje}")
                    
                    elif opcion_menu == '3':
                        print("Cerrando sesión...")
                        break
                    
                    else:
                        print("Opción inválida. Intente nuevamente.")
            else:
                print("Usuario o contraseña incorrectos.")
    
    elif opcion == 2:
        print("2. Registrar Usuario")
        
        if usu1 is None or con1 is None:
            usu1 = input("Ingrese usuario: ")
            con1 = input("Ingrese clave: ")
        elif usu2 is None or con2 is None:
            usu2 = input("Ingrese usuario: ")
            con2 = input("Ingrese clave: ")
        elif usu3 is None or con3 is None:
            usu3 = input("Ingrese usuario: ")
            con3 = input("Ingrese clave: ")
        else:
            print("Ya se han registrado el número máximo de usuarios.")
    
    elif opcion == 3:
        print("3. Salir")
        banderaMenu = False
    
    else:
        print("Opción no válida.")
