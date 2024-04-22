try:
    numero = int(input("Introduzca un número: "))
except ValueError:
    print ("Por favor, introduzca un número válido")
else:    
    print ("Número válido:", numero)
