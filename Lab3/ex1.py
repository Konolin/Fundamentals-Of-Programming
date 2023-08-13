import turtle


def rechteck():
    t = turtle.Pen()

    # desenare dreptunghi 100x200
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)

    # muta pixul in dreptunghi
    t.up()
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.down()

    # desenare dreptunghi 25x50
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)


def herz():
    t = turtle.Pen()
    t.left(45)
    t.forward(70)
    for i in range(100):
        t.left(2)
        t.forward(1)
    t.right(135)
    for i in range(100):
        t.left(2)
        t.forward(1)
    t.forward(70)


def hauser():
    t1 = turtle.Pen()
    t2 = turtle.Pen()

    # pune testoasele in pozitie
    t1.up()
    t1.backward(300)
    t1.left(90)
    t1.forward(100)
    t1.right(180)
    t1.down()

    t2.up()
    t2.forward(100)
    t2.left(90)
    t2.forward(100)
    t2.right(180)
    t2.down()

    # casa
    t1.forward(120)
    t2.forward(120)
    t1.left(90)
    t2.left(90)
    t1.forward(100)
    t2.forward(100)
    t1.left(90)
    t2.left(90)
    t1.forward(120)
    t2.forward(120)
    t1.left(90)
    t2.left(90)
    t1.forward(100)
    t2.forward(100)

    # acoperis
    t1.right(135)
    t2.right(135)
    t1.forward(70)
    t2.forward(70)
    t1.right(90)
    t2.right(90)
    t1.forward(70)
    t2.forward(70)

    # usa
    t1.up()
    t1.right(45)
    t1.forward(120)
    t1.right(90)
    t1.forward(30)
    t1.right(90)
    t1.down()

    t2.up()
    t2.right(45)
    t2.forward(120)
    t2.right(90)
    t2.forward(30)
    t2.right(90)
    t2.down()

    t1.forward(50)
    t2.forward(50)
    t1.left(90)
    t2.left(90)
    t1.forward(40)
    t2.forward(40)
    t1.left(90)
    t2.left(90)
    t1.forward(50)
    t2.forward(50)

    # geam
    t1.up()
    t1.right(180)
    t1.forward(70)
    t1.down()

    t2.up()
    t2.right(180)
    t2.forward(70)
    t2.down()

    t1.forward(20)
    t2.forward(20)
    t1.right(90)
    t2.right(90)
    t1.forward(40)
    t2.forward(40)
    t1.right(90)
    t2.right(90)
    t1.forward(20)
    t2.forward(20)
    t1.right(90)
    t2.right(90)
    t1.forward(40)
    t2.forward(40)


print('Wahlen Sie eine Zeichung aus:')
print('   1. Rechteck')
print('   2. Herz')
print('   3. Hauser')
print()
choice = input('Wahl: ')

if choice == '1':
    rechteck()
elif choice == '2':
    herz()
else:
    hauser()

input()
