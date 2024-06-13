
numero = input(int("Ingrese un número:\n"))
#función de tipo type para comprobar si un número es entero o no

if type (numero) == int:
    return True
# try except python ejemplos

#else para generar una excepción valueError en Python. en este caso, f significa que la cadena siguiente, la que está entre corchetes, está formateada.

else:
    raise ValueError (f"{numero} debe ser un número entero")

# python value error

#esta misma función también puede determinarse de la siguiente forma:

raise ValueError ("{} debe ser un número entero".format(numero))
