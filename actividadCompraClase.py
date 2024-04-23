import time, os

#Actividad2
#ejercicio1

contadorProductos = 0
acumuladorPrecio = 0
opcion = int(input("¿Desea lleva Agua por $ 600?    1. Si   2. no"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 600
opcion = int(input("¿Desea llevar Azúcar por $1200? 1. Si   2.no"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1200
opcion = int(input("¿Desea llevar Aceite por $1500? 1. Si   2.no"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1500
opcion = int(input("¿Desea llevar Arroz por $1250?\n 1.Si    2.No\n"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1250
opcion = int(input("¿Desea llevar Fideos por $790? 1. Si    2.no"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 790    
opcion = int(input("¿Desea llevar Bebida por $1780? 1. Si    2.no"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1780
opcion = int(input("¿Desea llevar Chocolate por $2500? 1. Si    2.no"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 2500
opcion = int(input("¿Desea llevar Pan molde por $1340? 1. Si    2.no"))
if opcion == 1:
    contadorProductos += 1
    acumuladorPrecio += 1340

print(f"Cantidad de productos: {contadorProductos}")
print(f"Tptal acumulado: $ {acumuladorPrecio}")
time.sleep(2)
preferencial = int(input("¿Es cliente preferencia?    1.si 2.no"))
if preferencial == 1:
    total = acumuladorPrecio * 0.75
    descuento = acumuladorPrecio * 0.25
else:
    total = acumuladorPrecio
    descuento = 0
print(f"Descuento: $ {descuento}")
print(f"Total a pagar: $ {total}")
pago = int(intput("Ingrese forma de pago:   1. Efectivo  2. Crédito-débito\n"))
if pago == 1:
    efectivo = int(input("Ingrese valor efectivo"))
    if efectivo < total:
        print("Saldo insuficiente... Guardias!!!")
    else:
        vuelto = efectivo - total
        print("Muchas gracias")
        print(f"Su vuelto es: $ {vuelto}")
else:
    print("No olvide su voucher")
       