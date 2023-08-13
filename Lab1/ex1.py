def ex_a(n):
    for x in range(2, n):

        prim = True
        for d in range(2, x // 2 + 1):
            if x % d == 0:
                prim = False

        if prim:
            print(x)


def ex_b():
    vector = [6, 1, 4, 3, 7, 8, 11, 11, 17, 4]
    rezultat = []
    temp = [vector[0]]

    for i in range(1, len(vector)):
        if vector[i] > vector[i - 1]:
            temp.append(vector[i])
        else:
            temp = [vector[i]]

        if len(temp) > len(rezultat):
            rezultat = temp

    print(rezultat)

ex_a(10)
#ex_b()