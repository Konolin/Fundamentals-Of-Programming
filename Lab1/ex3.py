def ex_a(nrRanduri):

    if nrRanduri == 0:
        return
    rand_anterior = [1]
    print(" " * nrRanduri, *rand_anterior)

    for i in range(nrRanduri - 1):
        rand_anterior.insert(0, 0)
        rand_anterior.append(0)
        rand_nou = []

        for j in range(1, len(rand_anterior)):
            rand_nou.append(rand_anterior[j - 1] + rand_anterior[j])
        print(" " * (nrRanduri - i - 1), *rand_nou)
        rand_anterior = rand_nou


def prim(n):
    if n == 0 or n == 1:
        return False
    for divizor in range(2, n // 2 + 1):
        if n % divizor == 0:
            return False
    return True


def ex_b():
    vector = [6, 1, 2, 2, 2, 2, 4, 3, 7, 8, 11, 11, 17, 11, 11]
    rezultat = []
    temp = []

    for i in range(len(vector)):
        if prim(vector[i]):
            temp.append(vector[i])
        else:
            temp = []

        if len(temp) > len(rezultat):
            rezultat = temp

    print(*rezultat)


#ex_a(10)
ex_b()
