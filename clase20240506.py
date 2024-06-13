import time, os
os.system("cls")
banderaEdad = True
banderaRut = True
banderaSexo = True
banderaMail = True
while True:
    print("Centro Médico DUOC\n")
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion == 1:
            print("REGISTRO DE PACIENTE")
            while banderaEdad:
                try:
                    edad = int(input("Ingrese edad: \n"))
                    while edad < 18 or edad > 110:
                        edad =int(input("Ingrese edad entre rango 18 y 110"))
                    banderaEdad = False
                except:
                    print("El campo edad no recibe texto ni símbolos")
            while banderaRut:
                    try:
                        rut = int(input("Ingrese RUT: \n"))
                        while rut <= 5000000 or rut > 100000000:
                            rut = int(input("Ingrese su RUT, dentro del rango de 5000000 y 99999999: \n"))
                        banderaRut = False
                    except:
                        print("El RUT ingresado es incorrecto")
            while banderaSexo:
                    try:
                        sexo = int(input("Ingrese sexo (F/M): \n"))
                        while "F" or "f" or "M" or "m":
                            sexo = int(input("Ingrese sexo, con las letra M o F \n"))
                        banderaSexo = False
                    except:
                        print("El caracter ingresado es incorrecto. Intente M o F...")
            while banderaPs:
                    try:
                        ps = int(input("Ingrese su Previsión de Salud (PS) Fonasa o Isapre: \n"))
                        while "Fonasa" or "fonasa" or "Isapre" or "isapre":
                            sexo = int(input("Ingrese su PS, indicando si es Isapre o Fonasa. \n"))
                        banderaPs = False
                    except:
                        print("La Previsión de Salud indicada es incorrecta. Intente nuevamente...")
            while banderaMail:
                    try:
                        mail = int(input("Ingrese su e-mail: \n"))
                        while "@":
                            mail = int(input("Su e-mail debe incluir un @ \n"))
                        banderaMail = False
                    except:
                        print("e-mail incorrecto. Debe contener al menos un caracter de @")
        elif opcion == 2:
            print("ATENCION PACIENTE")

        elif opcion == 3:
            print("CONSULTAR DATOS PACIENTE")

        elif opcion == 4:
            os.system("cls")
            print("SALIR")
            break
            
            
    except:
        print("Opción ingresa no existe...")
    