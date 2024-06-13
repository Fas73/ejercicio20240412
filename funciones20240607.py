import os

def cls():
    os.system("cls")

#Función para calcular el total de una factura con IVA del 19%
def calcular_total_factura(cantidad_sin_iva):
    iva = 0.19
    total = cantidad_sin_iva * (1 + iva)
    print(f"La factura con el 19% de IVA incluido es: {total}")

#Función para calcular el área de un círculo
import math

def area_circulo(radio):
    return math.pi * radio ** 2

#Función que recibe una muestra de números en una lista y devuelve su media
def media_lista(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

#Función que recibe una muestra de números en una lista y devuelve otra lista con sus cuadrados
def cuadrados_lista(numeros):
    return [numero ** 2 for numero in numeros]

#Función que recibe una cadena de caracteres y devuelve la cantidad de palabras
def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

#Función que recibe una cadena de caracteres y devuelve la cantidad de letras que contiene la frase:
def contar_letras(cadena):
    letras = [caracter for caracter in cadena if caracter.isalpha()]
    return len(letras)
