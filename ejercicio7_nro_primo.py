print("\n" * 50)

#Ejercicio 8
inicio = 1 
fin = 10 
desde = 1 
hasta = 10 
##########
for x in range(inicio, fin + 1):  #range con 2 argumentos por que debo recorrer del 1 al 10 (10+1)
	print(f"Tabla del {x}:") 
	for y in range(desde, hasta + 1):
		print(f'{x} x {y} = {x * y}')
	print() ##aca solo pongo un espacio para darle orden xD