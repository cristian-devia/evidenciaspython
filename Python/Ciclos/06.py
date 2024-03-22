alto = 9
cont = 1

for column in range(1, alto + 1):

    for fil in range(1, cont + 1):
        print("* ", end=" ")

    if column < 5:
        cont += 1
    else:
        cont -= 1

    print()
