
cantidad = int(input("Ingrese la cantidad de productos: "))
precio = int(input("Ingrese el precio: "))


valor = precio * cantidad
valoriva = valor * 0.16
total = valor + valoriva

print(f"El valor total de la compra con IVA incluido es: {total}")