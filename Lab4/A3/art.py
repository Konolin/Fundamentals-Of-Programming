def rock(art):
    print(art[0])
    return 'rock'


def paper(art):
    print(art[1])
    return 'paper'


def scissors(art):
    print(art[2])
    return 'scissors'


def read_art():
    with open('art.txt') as f:
        art = f.read().split('#')
    return art
