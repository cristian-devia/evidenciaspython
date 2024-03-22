
cuenta = float(input("Valor del monto: "))

if cuenta < 150000:
    print ("El pago debe ser en efectivo")
elif   150000 <= cuenta <= 300000:
    print ("El pago debe ser con el celular")
elif 300000 < cuenta <= 600000:
    print ("El pago debe ser con tarjeta débito")
else:
    print("El pago deber ser con tarjeta crédito")