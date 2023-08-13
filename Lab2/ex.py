def func1(lista):
    rezultat = []
    for i in range(len(lista)):
        cnt = 1
        for j in range(i):
            if lista[i] == lista[j]:
                cnt += 1
        if cnt == 1:
            rezultat.append(lista[i])
    return rezultat


def func2(lista):
    cnt = 0
    temp = func1(lista)
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] % 10 == temp[j] // 10 and temp[i] // 10 == temp[j] % 10:
                cnt += 1
                break
    print(cnt)


def func3(lista):
    temp = lista
    temp.sort(reverse=True)
    print(*temp, sep='')
    temp = [1,2,3]
    print(1,2,3, sep='')


def func4(lista):
    rezultat = [lista[0]]
    for i in range(0, len(lista)):
        rezultat.append(lista[i] * rezultat[0])
    print(*rezultat)


def func6(lista):
    temp = [lista[0]]
    rezultat = []

    for i in range(len(lista) - 1):
        if lista[i] % 10 == lista[i + 1] // 10:
            temp.append(lista[i + 1])
        else:
            temp = [lista[i + 1]]
        if 1 < len(temp) and len(temp) > len(rezultat):
            rezultat = temp

    print(*rezultat)


def kgv(x, y):
    k = max(x, y)
    while k % x + k % y > 0:
        k += 1
    return k


def func7(lista, f, t):
    k = 1
    for i in range(f, t + 1):
        k = kgv(k, lista[i])
    print(k)


lista = [10, 13, 89, 94, 43, 21, 55, 34, 40, 10, 42, 43, 43, 12, 21]


print(func1(lista))
#func2(lista)
#func3(lista)
#func4(lista)
#func6(lista)
#func7(lista, 3, 5)