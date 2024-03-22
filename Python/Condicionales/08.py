
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 <= num2 <= num3:
    ascent = (num1, num2, num3)
elif num1 <= num3 <= num2:
    ascent = (num1, num3, num2)
elif num2 <= num1 <= num3:
    ascente = (num2, num1, num3)
elif num2 <= num3 <= num1:
    ascent = (num2, num3, num1)
elif num3 <= num1 <= num2:
    ascent = (num3, num1, num2)
else:
    ascent = (num3, num2, num1)


if num1 >= num2 >= num3:
    descent = (num1, num2, num3)
elif num1 >= num3 >= num2:
    descent = (num1, num3, num2)
elif num2 >= num1 >= num3:
    descent = (num2, num1, num3)
elif num2 >= num3 >= num1:
    descent = (num2, num3, num1)
elif num3 >= num1 >= num2:
    descent = (num3, num1, num2)
else:
    descent = (num3, num2, num1)

print("Números en orden ascendente:", ascent)
print("Números en orden descendente:", descent)