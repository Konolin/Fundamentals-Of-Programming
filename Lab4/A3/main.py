from art import *
from random import choice


def main(scor):
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    user_input = input('Choose a move: ')

    art = read_art()
    user = user_move(user_input, art)
    comp = comp_move(art)

    scor = compare(user, comp, scor)
    if scor[0] + scor[1] < 3:
        main(scor)
    elif scor[0] + scor[1] == 3:
        if scor[0] > scor[1]:
            print('You won')
        else:
            print('You lost')


def comp_move(art):
    moves = [rock, paper, scissors]
    return choice(moves)(art)


def user_move(user_input, art):
    if user_input == '1':
        user = rock(art)
    elif user_input == '2':
        user = paper(art)
    else:
        user = scissors(art)
    return user


def compare(user, comp, scor):
    print(f"Computer: {comp} | User: {user}")
    if user == comp:
        print('Round drawn')
    elif (
            user == 'rock' and comp == 'scissors' or
            user == 'scissors' and comp == 'paper' or
            user == 'paper' and comp == 'rock'
    ):
        print('Round won')
        scor = (scor[0] + 1, scor[1])
    else:
        print('Round lost')
        scor = (scor[0], scor[1] + 1)
    return scor


scor = (0, 0)
main(scor)
