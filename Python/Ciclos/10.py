altura = 7  

print("*" * altura)

for i in range(1, altura - 1):
    espacios = altura - i - 1
    print(" " * espacios + "*")

for i in range(1, altura - 1):
    print(" " * i + "*")

print("*" * altura)
