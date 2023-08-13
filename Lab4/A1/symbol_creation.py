import turtle
from predef_symbols import symb_dict


# Creaza un simbol nou si il salveaza in fisier
def create_symbol():
    custom_symbols_dict = create_custom_symbols_dict()

    symbol_name = input('Name der Symbol: ')
    # Opreste utilizatorul din a aduaga un nou simbol, a carui nume este deja folosit
    while symbol_name in symb_dict or symbol_name in custom_symbols_dict:
        symbol_name = input('Der Symbol existiert schon, verwende ein anderer Name: ')

    creation_steps = create_symbol_graphics()

    add_symbol(symbol_name, creation_steps)


# Citeste informatiile din 'custom_symbols.txt' si returneaza
# un dictionar cu toate simbolurile
def create_custom_symbols_dict():
    f = open('custom_symbols.txt', 'r')
    custom_symbols_dict = {}

    lines = f.readlines()
    for line in lines:
        line = line.strip().split(' ')
        # Primul element dintr-un rand este cheiea, al doi-lea este valoarea
        custom_symbols_dict[str(line[0])] = str(line[1])

    f.close()
    return custom_symbols_dict


# Permite utilizatorului sa-si creeze un simbol
# Returneaza pasii folositi in creatia unui nou simbol
def create_symbol_graphics():
    # Input-urile vor fi salvate in ordine aici
    creation_steps = ''
    possible_inputs = ['W', 'S', 'D', 'A', 'F', 'G', 'w', 's', 'd', 'a', 'f', 'g']
    t = turtle.Turtle()

    user_input = input('Steuerungstaste: ')
    while user_input in possible_inputs:
        creation_steps += user_input

        if user_input == 'W' or user_input == 'w':
            t.forward(10)
        if user_input == 'S' or user_input == 's':
            t.backward(10)
        if user_input == 'D' or user_input == 'd':
            t.right(45)
        if user_input == 'A' or user_input == 'a':
            t.left(45)
        if user_input == 'F' or user_input == 'f':
            t.up()
        if user_input == 'G' or user_input == 'g':
            t.down()

        user_input = input('Steuerungstaste: ')

    print('Abbruch der Zeichnung')
    turtle.bye()

    return creation_steps


# Afiseaza un simbol custom
# Parcurge fiecare pas din procesul de desenare (din string-ul creation_steps)
def recreate_symbol_graphics(creation_steps, t):
    for step in creation_steps:
        if step == 'W' or step == 'w':
            t.forward(10)
        if step == 'S' or step == 's':
            t.backward(10)
        if step == 'D' or step == 'd':
            t.right(45)
        if step == 'A' or step == 'a':
            t.left(45)
        if step == 'F' or step == 'f':
            t.up()
        if step == 'G' or step == 'g':
            t.down()


# Salveaza simbolul creat de utilizator in fisier
def add_symbol(name, steps):
    f = open('custom_symbols.txt', 'a')
    f.write(name + ' ' + steps + '\n')
    f.close()
