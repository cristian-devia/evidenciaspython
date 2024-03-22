numllantas = int(input("Ingrese el número de llantas compradas: "))

precio1 = 240000  
precio2 = 221000  
precio3 = 180000  


if numllantas < 6:
    valort = numllantas * precio1
elif numllantas >= 6 and numllantas <= 7:
   valort = numllantas * precio2
else:
    valort = numllantas * precio3

print(f"El valor total a pagar es: ${valort}")
