def ex_a(n):
    t = 1
    while t * t < n:
        t += 1
    t -= 1
    print(t, n)


def ex_b():
    lista = [4, 5, 12, 15, 8, 11, 13, 9, 3]
    rezultat = []
    temp = [lista[0]]

    for i in range(1, len(lista)):
        if prim(lista[i - 1] - lista[i]):
            temp.append(lista[i])
        else:
            temp = [lista[i]]
        if len(temp) > len(rezultat):
            rezultat = temp

    if len(rezultat) > 1:
        print(rezultat)
    else:
        print([])


def prim(n):
    if n <= 1:
        return False
    for divizor in range(2, n // 2 + 1):
        if n % divizor == 0:
            return False
    return True


#ex_a(67.5)
ex_b()