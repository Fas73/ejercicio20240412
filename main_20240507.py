#repaso evaluacion 2 30%
#importar os y time 
import time, os

#crear menu (cabecera y su cuerpo)
banderaMenu = True
banderaRut = True
banderaEdad = True
banderaPaciente = True
while banderaMenu:
    os.system("cls")
    print("1) Registrar Paciente")
    print("2) Atencion Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion == 1:
            os.system("cls")
            print("***Registrar Paciente***")
            while banderaRut:
                try:
                    rut = int(input("ingrese su rut\n"))
                    while rut < 5000000 or rut > 99999999:
                        rut = int(input("ingrese su rut, entre el rango 5000000 y 99999999\n"))
                    banderaRut = False #que el rut esta correcto
                except:
                    print("en el campo rut no se permiten caracteres especiales ni letras")
            nombre = input("ingrese su nombre\n")
            while nombre == "" or nombre == " ":
                nombre = input("ingrese su nombre, recuerde que no puede venir vacio\n")
            direccion = input("ingrese su direccion\n")
            while direccion == "" or direccion == " ":
                direccion = input("ingrese su direccion, recuerde que no puede venir vacio\n")
            correo = input("ingrese su correo\n")
            while '@' not in correo:
                correo = input("ingrese su correo, recuerde poner un @\n")
            while banderaEdad:
                try:
                    edad = int(input("ingrese su edad\n"))
                    while edad < 0 or edad > 110:
                        edad = int(input("ingrese su edad, debe estar en rango 0 y 110\n"))
                    banderaEdad = False
                except:
                    print("para el campo edad no se permiten caracteres especiales ni letras")
            sexo = input("ingrese su sexo (f o m)\n")
            while sexo != 'm' and sexo != 'M' and sexo != 'f' and sexo != 'F':
                sexo = input("ingrese su sexo (f o m)\n")
            registro = ""
            ps = input("ingrese su prevision de salud\n")
            while ps != "fonasa" and ps != "isapre":
                ps = input("ingrese su prevision de salud, opciones: isapre o fonasa\n")

        elif opcion == 2:
            os.system("cls")
            print("***Atencion Paciente***")
            while banderaPaciente:
                try:
                    rutPaciente = int(input("ingrese rut del paciente"))
                    if rutPaciente == rut:
                        registro = input("ingrese fecha dd/mm/aaaa y observaciones del paciente\n")
                        banderaPaciente = False
                    else:
                        print("rut ingresado no existe en la ficha ")
                except:
                    print("en el campo rut no acepta caracteres especiales ni letras")
            
        elif opcion == 3:
            os.system("cls")
            print("***Consultar Datos Paciente***")
            while banderaPaciente:
                try:
                    rutPaciente = int(input("ingrese rut del paciente"))
                    if rutPaciente == rut:
                        print(f"RUT: {rut}")
                        print(f"NOMBRE: {nombre}")
                        print(f"EDAD: {edad}")
                        print(f"CORREO: {correo}")
                        print(f"DIRECCION: {direccion}")
                        print(f"PREVISION SALUD: {ps}")
                        print(f"INDICACIONES: {registro}")
                        x = input("presione enter para continuar")
                        banderaPaciente = False
                    else:
                        print("rut ingresado no existe en la ficha ")
                except:
                    print("en el campo rut no acepta caracteres especiales ni letras")
            
        elif opcion == 4:
            os.system("cls")
            print("Ha salido del sistema…")
            x = input("presione enter para continuar")
            banderaMenu = False
    except:
        print("opcion ingresada no es valida")