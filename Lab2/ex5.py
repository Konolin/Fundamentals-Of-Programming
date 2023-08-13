# afiseaza doar numerele din lista a caror cifre respecta ecuatia string
def filtru(lista, ec_str):
    global i
    for nr in lista:
        x = nr // 10
        y = nr % 10

        i = 0
        a = calcul(x, y, ec_str)    # a: partea ecuatiei pana la '='
        b = calcul(x, y, ec_str)    # b: partea ecuatiei dupa '='

        if a == b:
            print(nr)


# calculeaza o parte din ecuatie (inainte sau dupa '=')
def calcul(x, y, ec_str):
    # i parcurge fiecare element al ecuatiei string
    global i

    # se initializeaza ecuatia formata din numere
    ec_nr = conversie(x, y, ec_str)

    while i < len(ec_str) and ec_str[i] != '=':
        # se modifica ecuatia in functie de simbolul si de numarul care urmeaza
        if ec_str[i] == '+':
            i += 1
            ec_nr += conversie(x, y, ec_str)
        elif ec_str[i] == '-':
            i += 1
            ec_nr -= conversie(x, y, ec_str)
        elif ec_str[i] == '*':
            i += 1
            ec_nr *= conversie(x, y, ec_str)
        elif ec_str[i] == '/':
            i += 1
            ec_nr /= conversie(x, y, ec_str)
        elif ec_str[i] == '^':
            i += 1
            ec_nr **= conversie(x, y, ec_str)

    # in cazul in care se calculeaza 'a', 'i' creste pentru a sari peste '='
    if i < len(ec_str) and ec_str[i] == '=':
        i += 1
        
    return ec_nr


# transforma x/y/nr din ecuatia string in int
def conversie(x, y, ec_str):
    global i
    ec_str = ec_str.replace('x', str(x))
    ec_str = ec_str.replace('y', str(y))

    rez = 0
    while i < len(ec_str) and ec_str[i] in '0123456789':
        rez = rez * 10 + int(ec_str[i])
        i += 1

    return rez


lista = [10, 13, 89, 94, 21, 55, 34, 40, 42, 43, 12]
ec_str = 'x=y^4-12'
filtru(lista, ec_str)
