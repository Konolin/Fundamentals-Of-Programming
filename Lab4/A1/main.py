from symbol_creation import create_symbol
from word_printing import read_word


def menu():
    print('1. Textnachricht zeichnen')
    print('3. Neues Symbol definieren')

    choice = input('Auswahl: ')

    if choice == '1':
        read_word()
    elif choice == '2':
        create_symbol()
    else:
        print('~~Falsches Input~~')
        menu()


menu()
