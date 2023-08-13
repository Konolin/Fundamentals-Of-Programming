def filtru(lista, ec_str):
    ec_lista = ec_str.split('=')
    print(ec_lista)

    for nr in lista:
        x = nr // 10
        y = nr % 10

        ec_st = calcul(ec_lista[0], x, y)
        ec_dr = calcul(ec_lista[1], x, y)

        if ec_st == ec_dr:
            print(lista[nr])


def calcul(ec, x, y):
    rez = 0
    if ec.find('+'):
        ec.split('+')
    elif ec.find('-'):
        ec.split('-')
    elif ec.find('*'):
        ec.split('*')
    elif ec.find('/'):
        ec.split('/')

    return rez


lista = [10, 13, 89, 94, 21, 55, 34, 40, 42, 43, 12]
ec_str = 'x=y^4-12'
filtru(lista, ec_str)
