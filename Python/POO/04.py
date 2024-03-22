def pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return 1 / pow(x, -n)
    else:
        return x * pow(x, n - 1)