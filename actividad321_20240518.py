import os
os.system

# ejercicio1 - actividad 3.2.1

def nombre_extenso(): #defino la funcion nombre_extenso - Sin argumentos
    nombres = [] # inicializo la lista nombres vacía, se usará para almacenar los nombres que entre el usuario
    for x in range(3): #inicio el bucle for, que se ejecuta 3 veces range(3)
        nombre = input(f"Ingrese el nombre {x + 1}: ") #{x + 1} se usa para que muestra el nro 1, luego el 2
        nombres.append(nombre) #nombre se agrega a la lista nombres con .append

    nombre_max = max(nombres, key=len) #el nombre mas largo se almacena en la variable nombre_max
    #funcion max() encuentra la linea con más caracteres
    # key=len compara elementos de lista, basdo en longitud de caracteres. 
    # la funcion len() devuelve la longitud de una cadena
    print(f"\nEl nombre más largo es: {nombre_max}")

nombre_extenso() #invoco a la función nombre_extenso() para que se ejecute



# nombres1 = input("Ingrese nombre: \n")
# nombres2 = input("Ingrese nombre: \n")
# nombres3 = input("Ingrese nombre: \n")

# nombres_lista = [nombres1, nombres2, nombres3]

# nombres_lista.sort(key=len)

# print(nombres_lista)


# ejercicio2
# nom1 = input("Ingrese nombre: \n")
# ape1 = input("Ingrese nombre: \n")
# nom2 = input("Ingrese nombre: \n")
# ape2 = input("Ingrese nombre: \n")
# nom3 = input("Ingrese nombre: \n")
# ape3 = input("Ingrese nombre: \n")

# nom_lista = [nom1, nom2, nom3]
# ape_lista = [ape1, ape2, ape3]

# concatenada = nom_lista + ape_lista
# concatenada.sort
# print(concatenada)

# ejercicio3


