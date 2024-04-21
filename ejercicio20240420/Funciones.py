# suma = 7 + 6 + 5
# media = suma / 3
# print ("El promedio de la clase es: ", media)

# suma = 7 + 7 + 7
# media = suma / 3
# print ("El promedio de la clase es: ", media)

# def puntuacion(alumno1, alumno2, alumno3):
#     suma = alumno1 + alumno2 + alumno3
#     return suma / 3

# promedio = puntuacion(7, 5, 6)
# print ("El promedio de la clase es: ", promedio)

# promedio = puntuacion(7, 7, 7)
# print ("El promedio de la clase es: ", promedio)

def puntuacion(clase):
    return sum(clase) / len(clase)

clase = [7, 5.5, 6]
promedio = puntuacion(clase)
print ("El promedio de la clase es: ", promedio)

clase = [7, 7, 7, 1]
promedio = puntuacion(clase)
print ("El promedio de la clase es: ", promedio)

