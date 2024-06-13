import os, time

#arreglos
pacientes = []

#variables globales
cont_registro = 0
cont_pacientes = 0

while True:
    os.system("cls")
    #variables
    rut = 0
    nombre = ""
    direccion = ""
    correo = ""
    edad = 0
    sexo = ""
    ps = ""
    registro = ""

    #banderas integers
    bool_rut = True
    bool_edad = True
    bool_registro = True
    #menu
    print("Hospital.py")
    print("1.- Registrar Paciente")
    print("2.- Atencion Paciente")
    print("3.- Gestionar Paciente ")
    print("4.- Salir")
    try:
        opcMenu = int(input("Ingrese una opcion (1/2/3/4): "))
    except:
        print("Ingrese tipo de dato valido!")
        time.sleep(1)
        continue
    
    if opcMenu == 1:
        os.system("cls")
        print("-Registrar Paciente-")
        while bool_rut:
            try:
                rut = int(input("Ingrese rut: \n"))
                if rut > 5000000 and rut < 99999999:
                    print("Rut ingresado!")
                    bool_rut = False
                    time.sleep(1)
                else:
                    time.sleep(1)
            except:
                os.system("cls")
                print("Ingrese un dato valido!")
                time.sleep(1)
                
        os.system("cls")    
        print("-Registrar Paciente-")
        nombre = input("Ingrese el nombre: \n")
        while not nombre:
            os.system("cls")
            nombre = input("Ingrese un nombre no vacio: \n")
        else:
            print("Nombre guardado!")
            time.sleep(1)
        
        os.system("cls")
        print("-Registrar Paciente-")   
        direccion = input("Ingrese direccion: \n")
        while not direccion:
            os.system("cls")
            direccion = input("Ingrese una direccion no vacia: \n")
        else:
            print("Direccion guardada!")
            time.sleep(1)
        
        os.system("cls")
        print("-Registrar Paciente-") 
        correo = input("Ingrese correo: \n")
        while "@" not in correo:
            os.system("cls")
            correo = input("Ingrese correo valido: \n")
        else:
            print("Correo ingresado!")
            time.sleep(1)
        
        
        while bool_edad:
            os.system("cls")
            print("-Registrar Paciente-")
            try:
                edad = int(input("Ingrese edad (0 a 110): \n"))
                if edad >= 0 and edad <= 110:
                    print("Edad ingresada!")
                    bool_edad = False
                    time.sleep(1)
                else:
                    time.sleep(1)
            except:
                os.system("cls")
                print("Ingrese un dato valido!")
                time.sleep(1)
        
        os.system("cls")    
        print("-Registrar Paciente-")  
        sexo = input("Ingrese sexo (f o m): \n")
        while sexo != "f" and sexo != "m":
            sexo = input("Ingrese sexo valido (f o m): \n")
        else:
            print("Sexo ingresado!")
            time.sleep(1)
        
        os.system("cls")
        print("-Registrar Paciente-")    
        ps = input("Ingrese su prevision de salud (Isapre o Fonasa): \n")
        while ps != "Isapre" and ps != "Fonasa":
            ps = input("Ingrese su prevision de salud valida (Isapre o Fonasa): \n")
        else:
            print("Prevision ingresada!")
            time.sleep(1)
            
        paciente = [rut,nombre,direccion,correo,edad,sexo,ps]
        pacientes.append(paciente)
        cont_pacientes += 1
        os.system("cls")
        print("Paciente agregado!")
        time.sleep(1)
    if opcMenu == 2:
        os.system("cls")
        print("-Atencion Paciente-")
        bool_rut = True
        if cont_pacientes > 0:
            while bool_rut:
                try:
                    rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                    if rut_ingresado > 5000000 and rut_ingresado < 99999999:
                        print("Rut ingresado!")
                        bool_rut = False
                        time.sleep(1)
                    else:
                        time.sleep(1)
                except:
                    print("Ingrese un dato valido!")
                    time.sleep(1)
        else:
            print("No se ha ingresado ningun paciente!")
            time.sleep(1)
                
        for paciente in pacientes:
            if paciente[0] == rut_ingresado:
                print("Ingrese paciente ", paciente[1])
                while bool_registro:
                    registro = input("Ingrese motivo de consulta: \n")
                    if not registro:
                        print("Registro no puede estar vacio!")
                    else:
                        print("Registro ingresado!")
                        cont_registro += 1
                        bool_registro = False
                        time.sleep(1)
                    paciente.append(registro)
                    print(paciente)
                    input("Enter para continuar...")  
    if opcMenu == 3:
        bool_modificar = True
        if cont_pacientes > 0:
            while True:
                os.system("cls")
                print("-Gestionar Paciente-")
                print("1.- Consultar datos paciente")
                print("2.- Eliminar paciente")
                print("3.- Modificar paciente")
                print("4.- Regresar al menu principal")
                try:
                    opcGestionar = int(input("Ingrese una opcion (1/2/3/4): "))
                except:
                    print("Ingrese tipo de dato valido!")
                    time.sleep(1)
                    continue
                if opcGestionar == 1:
                    os.system("cls")
                    print("-Consultar datos paciente-")
                    bool_rut = True
                    bool_consulta = None
                    while bool_rut:
                        try:
                            rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                            if rut_ingresado > 5000000 and rut_ingresado < 99999999:
                                print("Rut ingresado!")
                                bool_rut = False
                                bool_consulta = True
                                time.sleep(1)
                            else:
                                time.sleep(1)
                        except:
                            print("Ingrese un dato valido!")
                            time.sleep(1)
                    paciente_ingresado = None
                    for paciente in pacientes:
                        if paciente[0] == rut_ingresado:
                            paciente_ingresado = paciente
                            
                        if bool_consulta:
                            print("Paciente encontrado...")
                            print("Rut: ", paciente_ingresado[0])
                            print("Nombre: ", paciente_ingresado[1])
                            print("Direccion: ", paciente_ingresado[2])
                            print("Correo: ", paciente_ingresado[3])
                            print("Edad: ", paciente_ingresado[4])
                            print("Sexo: ", paciente_ingresado[5])
                            print("Prevision: ", paciente_ingresado[6])
                            print(cont_registro)
                            if cont_registro > 0:
                                print("Registro: ", paciente_ingresado[7])
                            else:
                                print("Paciente aun no ha sido atendido")
                            bool_consulta = False  
                        else:
                            print("Paciente no registrado!")
                        input("Enter para continuar...")
                if opcGestionar == 2:
                    os.system("cls")
                    print("-Eliminar paciente-")
                    bool_rut = True
                    while bool_rut:
                        try:
                            rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                            if rut_ingresado > 5000000 and rut_ingresado < 99999999:
                                print("Rut ingresado!")
                                bool_rut = False
                                time.sleep(1)
                            else:
                                time.sleep(1)
                        except:
                            print("Ingrese un dato valido!")
                            time.sleep(1)
                    for paciente in pacientes:
                        if paciente[0] == rut_ingresado:
                            try:
                                pacientes.remove(paciente)
                                print("Paciente eliminado!")
                                cont_pacientes -= 1
                                time.sleep(1)
                            except:
                                print("Paciente no encontrado!")
                if opcGestionar == 3:
                    bool_rut = True
                    bool_edad = True
                    bool_modificar = None
                    os.system("cls")
                    print("Modificar paciente-")
                    while bool_rut:
                        try:
                            rut_ingresado = int(input("Ingrese un rut a buscar: \n"))
                            if rut_ingresado > 5000000 and rut_ingresado < 99999999:
                                print("Rut ingresado!")
                                bool_rut = False
                                bool_modificar = True
                                time.sleep(1)
                            else:
                                time.sleep(1)
                        except:
                            print("Ingrese un dato valido!")
                            time.sleep(1)
                    paciente_modificar = None
                    for paciente in pacientes:
                        if paciente[0] == rut_ingresado:
                            paciente_modificar = paciente
                        if bool_modificar:
                            while bool_modificar:
                                print("1.- Nombre ")
                                print("2.- Direccion ")
                                print("3.- Correo")
                                print("4.- Edad")
                                print("5.- Sexo")
                                print("6.- Prevision")
                                print("7.- Salir")
                                try:  
                                    modificar = int(input("Ingrese que campo desea modificar (1/2/3/4/5/6/7): "))
                                except:
                                    print("Ingrese tipo de dato valido!")
                                    time.sleep(1)
                                    continue
                                nuevo_valor = None

                                if modificar == 1:
                                    print("-Modificar Paciente-")
                                    nombre = input("Ingrese el nombre: \n")
                                    while not nombre:
                                        os.system("cls")
                                        nombre = input("Ingrese un nombre no vacio: \n")
                                    else:
                                        print("Nombre modificado!")
                                        paciente[1] = nombre
                                        time.sleep(1)
            
                                if modificar == 2:
                                    os.system("cls")
                                    print("-Modificar Paciente-")   
                                    direccion = input("Ingrese direccion: \n")
                                    while not direccion:
                                        os.system("cls")
                                        direccion = input("Ingrese una direccion no vacia: \n")
                                    else:
                                        print("Direccion modificda!")
                                        paciente[2] = direccion
                                        time.sleep(1)

                                if modificar == 3:
                                    os.system("cls")
                                    print("-Modificar Paciente-") 
                                    correo = input("Ingrese correo: \n")
                                    while "@" not in correo:
                                        os.system("cls")
                                        correo = input("Ingrese correo valido: \n")
                                    else:
                                        print("Correo modificado!")
                                        paciente[3] = correo
                                        time.sleep(1)

                                if modificar == 4:
                                    while bool_edad:
                                        os.system("cls")
                                        print("-Modificar Paciente-")
                                        try:
                                            edad = int(input("Ingrese edad (0 a 110): \n"))
                                            if edad >= 0 and edad <= 110:
                                                print("Edad modificada!")
                                                paciente[4] = edad
                                                bool_edad = False
                                                time.sleep(1)
                                            else:
                                                time.sleep(1)
                                        except:
                                            os.system("cls")
                                            print("Ingrese un dato valido!")
                                            time.sleep(1)

                                if modificar == 5:
                                    os.system("cls")    
                                    print("-Modificar Paciente-")  
                                    sexo = input("Ingrese sexo (f o m): \n")
                                    while sexo != "f" and sexo != "m":
                                        sexo = input("Ingrese sexo valido (f o m): \n")
                                    else:
                                        os.system("cls")
                                        print("Sexo modificado!")
                                        paciente[5] = sexo
                                        time.sleep(1)

                                if modificar == 6:
                                    os.system("cls")
                                    print("-Modificar Paciente-")    
                                    ps = input("Ingrese su prevision de salud (Isapre o Fonasa): \n")
                                    while ps != "Isapre" and ps != "Fonasa":
                                        ps = input("Ingrese su prevision de salud valida (Isapre o Fonasa): \n")
                                    else:
                                        print("Prevision modificada!")
                                        paciente[6] = ps
                                        time.sleep(1)
                                
                                if modificar == 7:
                                    print("Saliendo de menu de modificacion...")
                                    bool_modificar = False
                                    time.sleep(2)
                                
                                for paciente in pacientes:
                                    print(paciente)
                                input("Enter para continuar...")
                        
                if opcGestionar == 4:
                    print("Volviendo al menu principal...")
                    time.sleep(2)
                    break  
        else:
            os.system("cls")
            print("-Gestionar Paciente-")
            print("Ningun paciente ha sido ingresado!")
            time.sleep(1)
    if opcMenu == 4:
        print("Ha salido de programa...")
        break