import turtle
from predef_symbols import symb_dict
from symbol_creation import create_custom_symbols_dict, recreate_symbol_graphics


# Citeste un cuvant de la tastatura si il deseneaza
def read_word():
    word = input('Wort: ')
    max_length = max_word_length()
    custom_symbols_dict = create_custom_symbols_dict()
    word_exists = exists(word)

    # Verifica daca exista un simbol nedefinit in cuvant
    if error_symbol(word, custom_symbols_dict):
        print('Der Wort enthalt ein Symbol der nicht definiert ist')
        return

    # Afiseaza un cuvant pe ecran
    # Verifica daca noul cuvant poate sa incapa pe ecran
    if len(word) <= max_length:
        draw_word(word, max_length, custom_symbols_dict)
        if not exists:
            write_word_in_file(word)
    else:
        print('Der Wort ist zu lang.')
        read_word()


# Salveaza cuvantul desenat in fisier
def write_word_in_file(word):
    f = open('words.txt', 'a')
    f.write(f'{word}\n')
    f.close()


# Deseneaza un cuvant pe ecran
def draw_word(word, max_length, custom_symbols_dict):
    t = turtle.Turtle()
    # Genereaza pozitia de inceput a creionului
    position = -max_length // 2 * 25

    for c in word:
        # Muta creionul pentru a incepe desenarea unei noi litere
        t.up()
        t.setposition(position, 0)
        t.down()

        # Verifica daca simbolul 'c' este predefinit sau custom
        if c in symb_dict:
            symb_dict[c](t)
        else:
            recreate_symbol_graphics(custom_symbols_dict[c], t)

        # Reseteaza directia creionului si creste pozitia laterala
        t.setheading(0)
        position += 25

    input('Fertig, drucke eine Taste')
    turtle.bye()


# Returneaza lungimea maxima a unui cuvant, care poate incapea
# pe un singur rand
def max_word_length():
    width = turtle.screensize()[0]
    # 50 - pentru a nu afisa literele chiar pe marginea ecranuli
    # 25 - latimea maxima a unei litere
    max_length = (width * 2 - 50) / 25
    return max_length


# Verifica daca un cuvant a mai fost scris deja
# Returneaza o valoare booleana corespunzatopare
def exists(word):
    f = open('words.txt', 'r')

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == word:
            return True

    f.close()
    return False


# Verifica daca un simbol este definit (predefinit/custom)
# Returneaza o valoare booleana corespunzatopare
def error_symbol(word, custom_symbols_dict):
    for c in word:
        if c not in symb_dict and c not in custom_symbols_dict:
            return True
    return False
