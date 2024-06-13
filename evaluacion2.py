#repaso evaluacion 2 30%
#crear un menú
#opción tengo que registrar un alumno
#validar todos los campos
#opción 2 tengo que ver el resumen de la ficha
#tengo que validar 1: que el usuario sea admin, 2: que el rut exista en el formulario
#además, tengo que condicionar el NEM para enviar un mensaje
#opción salir
import time, os
user = "admin"
password = "admin"
while True:
    print("\t\tSistema de Gestión de Alumnos")
    print("1. Registrar Alumno")
    print("2. Consultar Datos de Alumno")
    print("3. Salir")
    try:
        opcion = int(input("Ingrese una opción:\n"))
        if opcion == 1:
            os.system("cls")
            print("REGISTRO ALUMNO")
            #solicitar nombre y validar que no venga vacío
            nombre = input("Ingrese su nombre\n")
            while nombre == " ":
                nombre = input("Ingrese su nombre, no acepta cadena vacía")
            #solicitar dirección y validar que no venga vacío 
            direccion = input("Ingrese su dirección\n")
            while direccion =="":
                direccion = input("Ingrese su dirección, no acepta cadena vacía\n")
            #solicitar y validar rut que esté entre los valores mencionados
            rut = int(input("Ingrese su RUT\n"))
            while rut <= 5000000 or rut >=39999999:
                rut = int(input("Ingrese su RUT, >= a 5000000 y =< 39999999\n"))
            #solicitar edad y validar rangos etarios
            edad = int(input("Ingrese edad\n"))
            while edad < 17 or edad >90:
                edad = int(input("Ingrese edad\n"))
            #solicitar correo y validar que exista al menos 1 arroba(@)
            correo = input("Ingrese su correo")
            while "@" not in correo:
                correo = input("Ingrese su correo\n")
                #solicitar NEM (debe ser decimal)
                nem = float(input("Ingrese NEM\n"))
                           
        elif opcion ==2:
            os.system("cls")
            print("CONSULTA DATOS DEL ALUMNO")
            username = input("Ingrese usuario\n")
            psswrd = input("Ingrese password")
            if(user == username and password == psswrd):
                rut_alumno = int(input("ingrese rut de alumno a buscar\n"))
                if rut_alumno == rut:
                    print(f"Nombre: {nombre}")
                    print("Dirección: ", direccion)
                    print(f"Edad: {edad}")
                    print("Correo: ", correo)
                    print(f"NEM: {nem}")
                    if nem <= 520:
                        print("Alumno no cumple con requisito")
                    else:
                        print("Alumno cumple con requisito")    
                else:
                    print("El RUT ingresado no existe")      

        elif opcion == 3:
            os.system("cls")
            print("SALIR")
            print("Ha salido del sistema")    
    except:
        print("Opción no existe")
