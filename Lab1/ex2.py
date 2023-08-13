def ex_a(n):
    x = 2
    i = 1
    while i <= n:
        if prim(x):
            print(x)
            i += 1
        x += 1


def prim(n):
    if n == 0 or n == 1:
        return False
    for divizor in range(2, n // 2 + 1):
        if n % divizor == 0:
            return False
    return True


def ex_b():
    lista = [4, 3, 12, 15, 7, 11, 13, 9, 3]
    rezultat = []
    temp = [lista[0]]

    for i in range(1, len(lista)):
        if relativ_prim(lista[i - 1], lista[i]):
            temp.append(lista[i])
        else:
            temp = [lista[i]]
        if len(temp) > len(rezultat):
            rezultat = temp

    if len(rezultat) > 1:
        print(rezultat)
    else:
        print([])


def relativ_prim(x, y):
    d = 2
    while d <= x and d <= y:
        if x % d + y % d == 0:
            return False
        d += 1
    return True


#ex_a(6)
ex_b()