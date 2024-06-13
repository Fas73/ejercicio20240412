import time, os


# ejercicio1

nombres = []
nombreLargo = ""
for x in range(3):
    nombre=input("Ingrese su nombre\n")
    nombres.append(nombre)
    if len(nombre) > len(nombreLargo):
        nombreLargo = nombre
print(f"El nombre más largo es: {nombreLargo}")


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


